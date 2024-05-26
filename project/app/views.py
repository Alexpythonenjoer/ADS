from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .models import Ad, Response
from .forms import NewUserForm, AdForm, ResponseForm

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request=request, template_name="main/register.html", context={"form":form})

    form = NewUserForm
    return render(request=request, template_name="main/register.html", context={"form":form})

@login_required
def create_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.owner = request.user
            ad.save()
            return redirect('ad_detail', ad.pk)
    else:
        form = AdForm()
    return render(request, 'create_ad.html', {'form': form})

@login_required
def ad_detail(request, pk):
    ad = Ad.objects.get(pk=pk)
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.ad = ad
            response.author = request.user
            response.save()
            send_mail(
                'You have a new response',
                'Go to your private page to see the details.',
                'from@example.com',
                [ad.owner.email],
                fail_silently=False,
            )
            return redirect('ad_detail', ad.pk)
    else:
        form = ResponseForm()
    return render(request, 'ad_detail.html', {'ad': ad, 'form': form})

@login_required
def private_page(request):
    responses = Response.objects.filter(ad__owner=request.user)
    return render(request, 'private_page.html', {'responses': responses})
