from django.urls import path
from application.views import (
    ObjectListView, ObjectDetailView,
    ObjectCreateView, ObjectUpdateView, ObjectDeleteView,
)

urlpatterns = [
    path('', ObjectListView.as_view(template_name = 'list.html'), name='ObjectListView'),
    path('create/', ObjectCreateView.as_view(template_name = 'form.html'), name='ObjectCreateView'),
    path('object/<pk>/', ObjectDetailView.as_view(template_name = 'object.html'), name='ObjectObjectView'),
    path('detail/<pk>/', ObjectDetailView.as_view(template_name = 'detail.html'), name='ObjectDetailView'),
    path('update/<pk>/', ObjectUpdateView.as_view(template_name = 'form.html'), name='ObjectUpdateView'),
    path('delete/<pk>/', ObjectDeleteView.as_view(), name='ObjectDeleteView'),   
]