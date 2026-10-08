from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("edit/<int:cid>/", views.customer_edit, name="customer_edit"),
    path("delete/<int:cid>/", views.customer_delete, name="customer_delete"),
]