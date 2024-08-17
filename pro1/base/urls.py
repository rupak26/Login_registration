from django.urls import path
from .views import userRegistrationView,userLoginView,TodoView
urlpatterns = [
    path('login/',userLoginView.as_view(),name = 'Login'),
    path('register/',userRegistrationView.as_view(),name='Registration'),
    path('todos/', TodoView.as_view(), name='todos'),
]