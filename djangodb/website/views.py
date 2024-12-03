from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages


# Create your views here.
def home(request):
    all_members = Member.objects.all()
    return render(request, "home.html", {"all": all_members})


def join(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            fname = request.POST["fname"]
            lname = request.POST["lname"]
            email = request.POST["email"]
            passwd = request.POST["passwd"]
            age = request.POST["age"]

            messages.success(request, "Member not added, please try again!")
            return render(
                request,
                "join.html",
                {
                    "fname": fname,
                    "lname": lname,
                    "email": email,
                    "passwd": passwd,
                    "age": age,
                },
            )

        messages.success(request, "Member added successfully")
        return redirect("home")
    else:
        return render(request, "join.html", {})
