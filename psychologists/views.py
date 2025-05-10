from django.shortcuts import render, redirect
from .models import Psychologist
from .forms import PsychologistForm

def psychologists_list(request):
    psychologists = Psychologist.objects.filter(country='Казахстан')  # Фильтруем психологов по Казахстану

    if request.method == 'POST':
        form = PsychologistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('psychologists_list')
    else:
        form = PsychologistForm()

    return render(request, 'psychologists/list.html', {
        'psychologists': psychologists,
        'form': form
    })



