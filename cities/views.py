from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from .models import City
from .forms import CityForm

__all__ = ('CityDetailView', 'CityCreateView', 'CityUpdateView', 'CityDeleteView', 'CityListView')


# Create your views here.

# def home(request, pk=None):
#     if request.method == "POST":
#         form = CityForm(request.POST)
#         if form.is_valid():
#             form.save()
#     form = CityForm()
#     qs = City.objects.all()
#     lst = Paginator(qs, 3)
#     page_number = request.GET.get('page')
#     page_obj = lst.get_page(page_number)
#     context = {'cities': qs, 'form': form, 'page_obj': page_obj, }
#     return render(request, 'cities/all_cities.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'


class CityCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:all_cities')
    success_message = "City was added successfully"


class CityUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:all_cities')
    success_message = "City was updated successfully"


class CityDeleteView(LoginRequiredMixin, DeleteView):
    model = City
    success_url = reverse_lazy('cities:all_cities')

    def get(self, request, *args, **kwargs):
        messages.success(request, "City was deleted successfully")
        return self.delete(request, *args, **kwargs)


class CityListView(ListView):
    paginate_by = 6
    model = City
    template_name = 'cities/all_cities.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CityForm()
        context['form'] = form
        return context
