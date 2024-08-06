# user/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from .models import Profile


@login_required
def profile_view(request):
    user_profile = request.user.profile
    if request.method == "POST":
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
        if p_form.is_valid():
            p_form.save()
            return redirect("profile")
    else:
        p_form = ProfileUpdateForm(instance=user_profile)

    context = {
        "p_form": p_form,
        "current_user": request.user,
    }
    return render(request, "profile.html", context)
