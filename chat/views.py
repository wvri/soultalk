from .models import Room, Message
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

@login_required
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'chat/rooms.html', {'rooms': rooms})

@login_required
def room_detail(request, room_name):
    room = get_object_or_404(Room, name=room_name)

    if request.method == 'POST':
        content = request.POST.get('text', '').strip()  # <-- здесь заменили 'content' на 'text'
        if content:
            Message.objects.create(room=room, user=request.user, content=content)
            return redirect('room_detail', room_name=room.name)

    messages = room.messages.order_by('timestamp')
    return render(request, 'chat/room_detail.html', {
        'room': room,
        'room_name': room.name,
        'messages': messages,
    })




