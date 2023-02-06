from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse_lazy
from json import dumps
from .forms import ObjectForm
from .models import Person as Object


from django.views.generic.list import ListView
class ObjectListView(ListView):
    model = Object
    paginate_by = settings.PAGINATE_BY

    def get_template_names(self):
        if self.request.htmx:
            return 'objects.html'
        return self.template_name


from django.views.generic.detail import DetailView
class ObjectDetailView(DetailView):
    model = Object

    def get_queryset(self):
        get_queryset = super().get_queryset().filter(pk=self.kwargs['pk'])
        return get_queryset

    def get_context_data(self, **kwargs):
        _get_context_data = super().get_context_data(**kwargs)
        _get_context_data['create'] = self.request.GET.get('create')
        return _get_context_data


class FormValidMixin:

    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponse(headers={'HX-Trigger': dumps({self.object_name: self.object.pk})})


from django.views.generic.edit import CreateView
class ObjectCreateView(FormValidMixin, CreateView):
    model = Object
    form_class = ObjectForm
    success_url = reverse_lazy('doNothing')
    object_name = 'create_pk'


from django.views.generic.edit import UpdateView
class ObjectUpdateView(FormValidMixin, UpdateView):
    model = Object
    form_class = ObjectForm
    success_url = reverse_lazy('doNothing')
    object_name = 'update_pk'


from django.views.generic.edit import DeleteView
class ObjectDeleteView(DeleteView):
    model = Object
    success_url = reverse_lazy('doNothing')

    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponse('<tr></tr>')