from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.sign_up, name='sign_up'),
    path('lognin/', views.log_in, name='log_in'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('artists/', views.artists, name='artists'),
    path('events/', views.events, name='events'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('contact/', views.contact, name='contact'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
