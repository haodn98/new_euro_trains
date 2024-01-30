from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from cities.models import City
from trains.models import Train
from .forms import RouteForm, RouteModelForm
from django.contrib import messages
from routes.utils import get_routes
from .models import Route

# Create your views here.
__all__ = ('home', 'find_routes', 'add_route','save_route', 'RouteDeleteView', 'RouteListView')


def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})


def find_routes(request):
    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routes/home.html', {'form': form})
            return render(request, 'routes/home.html', context)
        return render(request, 'routes/home.html', {'form': form})
    else:
        form = RouteForm()
        messages.error(request, "No data for search")
        return render(request, 'routes/home.html', {'form': form})


def add_route(request):
    if request.method == "POST":
        context = {}
        data = request.POST
        if data:
            overall_travel_time = int(data['total_time'])
            from_city_id = int(data['from_city'])
            to_city_id = int(data['to_city'])
            trains = data['trains'].split()
            trains_list = [int(train) for train in trains]
            trains_qs = Train.objects.filter(id__in=trains_list).select_related('from_city', 'to_city')
            cities = City.objects.filter(id__in=[from_city_id, to_city_id]).in_bulk()
            form = RouteModelForm(initial={'from_city': cities[from_city_id],
                                           'to_city': cities[to_city_id],
                                           'overall_travel_time': overall_travel_time,
                                           'trains': trains_qs})
            context['form'] = form

        return render(request, 'routes/create.html', context)
    else:
        form = RouteForm()
        messages.error(request, "Impossible to save non-existent route")
        return render(request, 'routes/home.html', {'form': form})


def save_route(request):
    if request.method == "POST":
        form = RouteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Route was saved")
            return redirect('/')
        return render(request, 'routes/create.html', {'form': form})
    else:
        messages.error(request, "Impossible to save non-existent route")
        return redirect('/')


class RouteListView(ListView):
    paginate_by = 6
    model = Route
    template_name = 'routes/all_routes.html'


class RouteDetail(DetailView):
    queryset = Route.objects.all()
    template_name = 'routes/detail.html'


class RouteDeleteView(LoginRequiredMixin, DeleteView):
    model = Route
    success_url = reverse_lazy('routes:all_routes')

    def get(self, request, *args, **kwargs):
        messages.success(request, "Route was deleted successfully")
        return self.delete(request, *args, **kwargs)
