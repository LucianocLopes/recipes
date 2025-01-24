from django.urls import path

from recipes import views

app_name = 'recipes'

urlpatterns = [
    # path('', views.home, name='home')
    path('', views.HomeView.as_view(), name='home'),
]
