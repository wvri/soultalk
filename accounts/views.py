from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import PsychologyTip, Feedback
from .forms import ProfileUpdateForm, FeedbackForm
from .models import Psychologist

def home(request):
    return render(request, 'home.html')

def psychologists(request):
    return render(request, 'psychologists/list.html', {'psychologists': psychologists})


@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш профиль был успешно обновлен!')
            return redirect('profile')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form})

@login_required
def remove_avatar(request):
    user = request.user
    user.avatar = None
    user.save()
    messages.success(request, 'Аватар удалён.')
    return redirect('profile')

def psychology_tips(request):
    tips = PsychologyTip.objects.all()
    return render(request, 'accounts/psychology_tips.html', {'tips': tips})

def feedback_view(request):
    form = FeedbackForm(request.POST or None)
    feedbacks = Feedback.objects.order_by('-created_at')

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('feedback')

    return render(request, 'accounts/feedback.html', {
        'form': form,
        'feedbacks': feedbacks
    })


def psychologists_view(request):
    psychologists = Psychologist.objects.all()
    return render(request, 'psychologists.html', {'psychologists': psychologists})