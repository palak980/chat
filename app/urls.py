from django.urls import path
from . import views
app_name = 'chat' 
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('chat_rooms/', views.chat_rooms, name='chat_rooms'),  # List of chat rooms
    path('chat_rooms/<str:room_name>/', views.chat_room_messages, name='chat_room_messages'),  # View messages for a chat room

    
]