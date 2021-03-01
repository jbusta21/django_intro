from django.urls import path
from . views import index, new, create, show, edit, destroy

urlpatterns = [
    path('', index),
    path('new', new),
    path('create', create),
    path('<int:number>', show),  # /number.../21
    path('<int:number>/edit', edit),
    path('<int:number>/delete', destroy)
]
