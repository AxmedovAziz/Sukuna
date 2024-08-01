from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservationForm, UpdateReservation
from .models import Reservation


def reservation_view(request):
    if request.method == "POST":
        form = ReservationForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("blog")
    else:
        form = ReservationForm(user=request.user)

    return render(request, "reservation.html", {"form": form})


def blog(request):
    reservations = Reservation.objects.all()
    context = {"reservations": reservations}
    return render(request, "blog.html", context)


def update_reservation_view(request, pk: int):
    reservation = get_object_or_404(Reservation, id=pk)
    if request.method == "POST":
        form = UpdateReservation(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect("blog")
    else:
        form = UpdateReservation(instance=reservation)

    context = {"form": form}
    return render(request, "update_reservation.html", context)


def delete_reservation_view(request, pk: int):
    reservation = get_object_or_404(Reservation, id=pk)
    if request.method == "POST":
        reservation.delete()
        return redirect("blog")
    return render(request, "confirm_delete.html", {"reservation": reservation})
