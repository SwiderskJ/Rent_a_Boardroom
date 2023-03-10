"""Rent_a_boardroom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from reservation_app.views import ReservationView
from rooms_app.views import DemoView, ListRoomsView, RoomDetailsView, AddRoomView, AvaiableRoomView, EditRoomView, \
    DeleteRoomView, ManageRoomsView
from user_app.views import UserCreateView, LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DemoView.as_view(), name='demo_page'),
    path('room_list/', ListRoomsView.as_view(), name='room_list'),
    path('room_details/<int:room_id>/', RoomDetailsView.as_view(), name='room_detail'),
    path('manage/', ManageRoomsView.as_view(), name='rooms_management'),
    path('add_room/', AddRoomView.as_view(), name="add_room"),
    path('edit_room/<int:room_id>/', EditRoomView.as_view(), name='edit_room'),
    path('delate_room/<int:room_id>/', DeleteRoomView.as_view(), name='delete_room'),
    path('rooms_to_rent/', AvaiableRoomView.as_view(), name="rooms_to_rent"),
    path('registration/', UserCreateView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reservations/', ReservationView.as_view(), name='user_reservation')
]
