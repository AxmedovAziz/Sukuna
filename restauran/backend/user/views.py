# user/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from .models import Profile


@login_required
def profile(request):
    try:
        profile = request.user.profile
        current_user = request.user
    except Profile.DoesNotExist:
        # Create a profile if it does not exist
        profile = Profile.objects.create(user=request.user)

    if request.method == "POST":
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if p_form.is_valid():
            p_form.save()
            return redirect("profile")
    else:
        p_form = ProfileUpdateForm(instance=profile)

    context = {"p_form": p_form, "current_user": current_user}
    return render(request, "profile.html", context)
