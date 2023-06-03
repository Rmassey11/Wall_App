from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('users/<int:UserId>', views.user),
    path('create_quote', views.create_quote),
    path('myaccount/<int:UserId>', views.myaccount),
    path('edit', views.edit),
    path('delete/<int:QuoteId>', views.delete),
    path('logout', views.logout),
    path('back', views.back),
]
