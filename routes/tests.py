from django.db import IntegrityError
from django.forms import ValidationError
from django.test import TestCase
from django.urls import reverse
from routes.utils import dfs_paths, get_graph

import cities.views
from cities.models import City
from routes import views as routes_view
from trains.models import Train
from routes.forms import RouteForm


# Create your tests here.
class AllTestsCase(TestCase):
    def setUp(self) -> None:
        self.city_A = City.objects.create(name="A")
        self.city_B = City.objects.create(name="B")
        self.city_C = City.objects.create(name="C")
        self.city_D = City.objects.create(name="D")
        self.city_E = City.objects.create(name="E")
        lst = [
            Train(name="t1", from_city=self.city_A, to_city=self.city_E, travel_time=4),
            Train(name="t2", from_city=self.city_B, to_city=self.city_E, travel_time=3),
            Train(name="t3", from_city=self.city_A, to_city=self.city_B, travel_time=5),
            Train(name="t4", from_city=self.city_B, to_city=self.city_C, travel_time=2),
            Train(name="t5", from_city=self.city_D, to_city=self.city_E, travel_time=7),
            Train(name="t6", from_city=self.city_E, to_city=self.city_A, travel_time=6),
            Train(name="t7", from_city=self.city_E, to_city=self.city_D, travel_time=4),
            Train(name="t8", from_city=self.city_C, to_city=self.city_A, travel_time=2),
            Train(name="t9", from_city=self.city_D, to_city=self.city_C, travel_time=5),
            Train(name="t10", from_city=self.city_D, to_city=self.city_A, travel_time=3),
        ]
        Train.objects.bulk_create(lst)

    def test_model_city_duplicate(self):
        city = City(name="A")
        with self.assertRaises(ValidationError):
            city.full_clean()

    def test_model_train_duplicate(self):
        train = Train(name="t1", from_city=self.city_A, to_city=self.city_E, travel_time=20)
        with self.assertRaises(ValidationError):
            train.full_clean()

    def test_model_train_time_duplicate(self):
        train = Train(name="t12", from_city=self.city_A, to_city=self.city_E, travel_time=4)
        with self.assertRaises(ValidationError):
            train.full_clean()

        try:
            train.full_clean()
        except ValidationError as e:
            self.assertIn('Change time in a trip', e.messages)

    def test_home_routes_views(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, template_name='routes/home.html')
        self.assertEquals(response.resolver_match.func, routes_view.home)

    def test_cbv_detail_views(self):
        response = self.client.get(reverse('cities:city_detail', kwargs={'pk': self.city_A.pk}))

        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, template_name='cities/detail.html')
        self.assertEquals(response.resolver_match.func.__name__, cities.views.CityDetailView.as_view().__name__)

    def test_find_all_routes(self):
        qs = Train.objects.all()
        graph = get_graph(qs)
        all_routes = dfs_paths(graph, self.city_A.id, self.city_E.id)
        self.assertEquals(len(list(all_routes)), 2)

    def test_valid_route_form(self):
        data = {'from_city': self.city_A.id, 'to_city': self.city_B.id, 'traveling_time': 15}
        form = RouteForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_route_form(self):
        data = {'from_city': self.city_A.id, 'to_city': self.city_B.id, 'traveling_time': 15.3}
        form = RouteForm(data=data)
        self.assertFalse(form.is_valid())
        data = {'from_city': self.city_A.id, 'to_city': self.city_B.id, }
        form = RouteForm(data=data)
        self.assertFalse(form.is_valid())

    def test_message_error_more_time(self):
        data = {'from_city': self.city_A.id, 'to_city': self.city_C.id, 'cities': [self.city_B.id], 'traveling_time': 5}
        response = self.client.post('/routes/find_routes/', data)
        self.assertContains(response, 'Travel time in all routes is bigger then you ask', 1, 200)

    def test_message_error_from_cities(self):
        data = {'from_city': self.city_E.id, 'to_city': self.city_A.id, 'cities': [self.city_B.id], 'traveling_time': 20}
        response = self.client.post('/routes/find_routes/', data)
        self.assertContains(response, "There is no available routes by your conditions", 1, 200)