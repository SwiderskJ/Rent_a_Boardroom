from django.shortcuts import render
from rooms_app.models import Room
from rooms_app.forms import CreateRoomForm
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse


class DemoView(View):

    def get(self, request):

        return render(request, 'demo_view.html')


class ListRoomsView(View):

    def get(self, request):
        all_room_list = Room.objects.all().order_by('name')
        return render(request, 'rooms_list.html', context={'rooms': all_room_list})


class RoomDetailsView(View):

    def get(self, request, room_id):
        room = Room.objects.get(id=room_id)
        return render(request, 'room_detail.html', context={'room': room})


class AddRoomView(View):

    def get(self, request):
        form = CreateRoomForm()
        return render(request, 'add_room.html', context={'form': form})

    def post(self, request):
        form = CreateRoomForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            room = Room.objects.create(
                name=data.get('name'),
                description=data.get('description'),
                city=data.get('city'),
                street=data.get('street'),
                street_number=data.get('street_number'),
                local_number=data.get('local_number'),
                post_code_first=data.get('post_code_first'),
                post_code_second=data.get('post_code_second'),
                level=data.get('level'),
                capacity=data.get('capacity'),
                projector=data.get('projector'),
                seats=data.get('seats'),
                tables=data.get('tables'),
                catering=data.get('catering'),
                private_parking=data.get('private_parking'),
                sound_system=data.get('sound_system'),
            )

            return redirect(reverse('room_detail', kwargs={'room_id': room.id}))
