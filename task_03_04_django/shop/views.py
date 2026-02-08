from django.shortcuts import render
from .forms import RegistrationForm

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data  # тут уже все значения проверены
            return render(request, "shop/result.html", {"data": data})
    else:
        form = RegistrationForm()

    return render(request, "shop/register.html", {"form": form})
