from django.urls import path
from . import views

urlpatterns = [
    path('' , views.allcontest, name = 'allcontest'),
    path('delete_item/<int:pick>', views.deleteItem, name = 'deleteItem'),
    path('update_item<int:pick>', views.updateItem, name = 'updateItem'),
]