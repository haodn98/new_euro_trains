from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.urls import reverse_lazy
from django.views.generic import (DetailView, CreateView, UpdateView, DeleteView, ListView)

from .forms import TrainForm
from .models import Train

__all__ = ('TrainListView', 'TrainDetailView', 'TrainCreateView', 'TrainUpdateView', 'TrainDeleteView',)


# Create your views here.

# def home(request, pk=None):
#     if request.method == "POST":
#         form = TrainsForm(request.POST)
#         if form.is_valid():
#             form.save()
#     form = TrainsForm()
#     qs = Trains.objects.all()
#     lst = Paginator(qs, 3)
#     page_number = request.GET.get('page')
#     page_obj = lst.get_page(page_number)
#     context = {'trains': qs, 'form': form, 'page_obj': page_obj, }
#     return render(request, 'trains/all_trains.html', context)


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/detail.html'


class TrainCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:all_trains')


class TrainUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:all_trains')
    success_message = "Trains was updated successfully"


class TrainDeleteView(LoginRequiredMixin, DeleteView):
    model = Train
    form_class = TrainForm
    success_url = reverse_lazy('trains:all_trains')

    def get(self, request, *args, **kwargs):
        messages.success(request, "Trains was deleted successfully")
        return self.delete(request, *args, **kwargs)


class TrainListView(ListView):
    paginate_by = 6
    model = Train
    template_name = 'trains/all_trains.html'
    ordering = ['from_city']
