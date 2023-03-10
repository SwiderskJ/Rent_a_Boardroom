from django.shortcuts import render
from rooms_app.models import Room
from rooms_app.forms import CreateRoomForm
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.contrib.auth.models import User


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


class ManageRoomsView(View):

    def get(self, request):
        rooms = Room.objects.filter(owner=request.user.id)
        return render(request, 'manage.html', context={'rooms': rooms})


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
                owner=User.objects.get(id=request.user.id),
            )

            return redirect(reverse('room_detail', kwargs={'room_id': room.id}))


class EditRoomView(View):

    def get(self, request, room_id):
        room = Room.objects.filter(id=room_id)[0]
        data = {
            'name': room.name,
            'description': room.description,
            'city': room.city,
            'street': room.street,
            'street_number': room.street_number,
            'local_number': room.local_number,
            'post_code_first': room.post_code_first,
            'post_code_second': room.post_code_second,
            'level': room.level,
            'capacity': room.capacity,
            'projector': room.projector,
            'seats': room.seats,
            'tables': room.tables,
            'catering': room.catering,
            'private_parking': room.private_parking,
            'sound_system': room.sound_system,
        }
        form = CreateRoomForm(data)
        return render(request, 'edit_room.html', context={'form': form})

    def post(self, request, room_id):
        form = CreateRoomForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            room = Room.objects.get(id=room_id)

            room.name = data.get('name')
            room.description = data.get('description')
            room.city = data.get('city')
            room.street = data.get('street')
            room.street_number = data.get('street_number')
            room.local_number = data.get('local_number')
            room.post_code_first = data.get('post_code_first')
            room.post_code_second = data.get('post_code_second')
            room.level = data.get('level')
            room.capacity = data.get('capacity')
            room.projector = data.get('projector')
            room.seats = data.get('seats')
            room.tables = data.get('tables')
            room.catering = data.get('catering')
            room.private_parking = data.get('private_parking')
            room.sound_system = data.get('sound_system')
            room.save()

            return redirect(reverse('room_detail', kwargs={'room_id': room.id}))


class DeleteRoomView(View):
    def get(self, request, room_id):
        room = Room.objects.get(id=room_id)
        room.delete()
        return redirect("room_list")


class AvaiableRoomView(View):

    def get(self, request):
        pass



