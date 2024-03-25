from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.sign_up, name='sign_up'),
    path('signin/', views.sign_in, name='sign_in'),
    path('profile/', views.profile, name='profile'),
    path('artists/', views.artists, name='artists'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
