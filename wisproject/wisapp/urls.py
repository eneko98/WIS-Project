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
    path('artists/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('add-to-favorites/<int:artist_id>/', views.add_artists_to_favorites, name='add-artists-to-favorites'),
    path('remove-from-favorites/<int:artist_id>/', views.remove_artists_from_favorites, name='remove-artists-from-favorites'),
    path('add-album-to-favorites/<int:album_id>/', views.add_album_to_favorites, name='add-album-to-favorites'),
    path('remove-album-from-favorites/<int:album_id>/', views.remove_album_from_favorites, name='remove-album-from-favorites'),
    path('events/', views.events, name='events'),   
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('add-to-upcoming/<int:event_id>/', views.add_to_upcoming, name='add_to_upcoming'),
    path('remove-from-upcoming/<int:event_id>/', views.remove_from_upcoming, name='remove_from_upcoming'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('contact/', views.contact, name='contact'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
