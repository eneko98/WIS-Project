from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.sign_up, name='sign_up'),
    path('lognin/', views.log_in, name='log_in'),
    path('profile/', views.profile, name='profile'),
    path('artists/', views.artists, name='artists'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
