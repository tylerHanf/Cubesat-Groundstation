from django.urls import path
from . import views


urlpatterns = [
    path("/", views.index_view),
    path("/example", views.template_example),
    path("/create_dataref", views.create_dataref)
]