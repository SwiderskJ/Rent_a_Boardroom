from django.shortcuts import render
from rooms_app.models import Room
from rooms_app.forms import RoomForm
from django.shortcuts import render, redirect
from django.views import View


class DemoView(View):

    def get(self, request):

        return render(request, 'demo_view.html')


class ListRoomsView(View):

    def get(self, request):
        all_room_list = Room.objects.all().order_by('name')
        return render(request, 'rooms_list.html', context={'rooms': all_room_list})


class RoomDetailsView(View):

    def get(self, request, room_id):
        room = Room.objects.filter(id=room_id)
        return render(request, 'room_detail.html', context={'room': room})
