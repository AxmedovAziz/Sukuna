from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservationForm, UpdateReservation
from .models import Reservation
from django.contrib.auth.decorators import permission_required, login_required


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


# @permission_required("reservation.edit_mymodel")
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


# @permission_required("reservation.delete_mymodel")
@login_required
def delete_reservation_view(request, pk: int):
    # Get the reservation object
    reservation = get_object_or_404(Reservation, id=pk)

    if request.method == "POST":
        # Check if the user is either the owner of the reservation or has the delete permission
        if reservation.name == request.user.username or request.user.has_perm(
            "reservation.delete_reservation"
        ):
            # Delete the reservation if allowed
            reservation.delete()
            return redirect("blog")

    # Render the delete confirmation page
    return render(request, "confirm_delete.html", {"reservation": reservation})
