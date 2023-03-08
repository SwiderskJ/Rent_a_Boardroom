from django.shortcuts import render
from rooms_app.models import Room
from rooms_app.forms import RoomForm
from django.shortcuts import render, redirect
from django.views import View


class DemoView(View):

    def get(self, request):
        all_room_list = Room.objects.all().order_by('name')
        return render(request, 'demo_view.html', context={'rooms': all_room_list})

