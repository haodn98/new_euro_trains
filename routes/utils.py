from trains.models import Train


def dfs_paths(graph, from_city, to_city):
    """To find all possible routes between 2 cities"""
    stack = [(from_city, [from_city])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == to_city:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))


def get_graph(qs):
    graph = {}
    for q in qs:
        graph.setdefault(q.from_city_id, set())
        graph[q.from_city_id].add(q.to_city_id)

    return graph


def get_routes(request, form) -> dict:
    context = {'form': form}
    qs = Train.objects.all().select_related("from_city", "to_city")
    qs = Train.objects.all()
    graph = get_graph(qs)
    data = form.cleaned_data
    from_city = data['from_city']
    to_city = data['to_city']
    cities = data['cities']
    traveling_time = data['traveling_time']
    all_routes = list(dfs_paths(graph, from_city.id, to_city.id))
    if not len(all_routes):
        raise ValueError('There is no available routes')
    if cities:
        _cities = [city.id for city in cities]
        routes_with_cities = []
        for route in all_routes:
            if all(city in route for city in _cities):
                routes_with_cities.append(route)
        if not routes_with_cities:
            raise ValueError(f'There is no available routes by your conditions')
    else:
        routes_with_cities = all_routes

    final_routes = []
    all_trains = {}
    # create dict with pair (from_city;to_city)(train):time of the trip
    for q in qs:
        all_trains.setdefault((q.from_city_id, q.to_city_id), [])
        all_trains[(q.from_city_id, q.to_city_id)].append(q)

    for route in routes_with_cities:
        tmp = {}
        tmp['trains'] = []
        total_time = 0
        for i in range(len(route) - 1):
            qs = all_trains[(route[i], route[i + 1])]
            q = qs[0]
            total_time += q.travel_time
            tmp['trains'].append(q)
        tmp['total_time'] = total_time
        if total_time <= traveling_time:
            final_routes.append(tmp)
    if not final_routes:
        raise ValueError("Travel time in all routes is bigger then you ask")
    final_routes.sort(key=lambda x: x['total_time'])
    context['routes'] = final_routes
    context['cities'] = {'from_city': from_city, 'to_city': to_city}
    return context
