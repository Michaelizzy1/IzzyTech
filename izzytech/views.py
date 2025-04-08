from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    form = MessageModelForm()
    if request.method == 'POST':
        form = MessageModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    context = {
        'form': form,
    }
    return render(request, 'izzytech/index.html', context)


def graphics_page(request):
    graphics = GraphicsModel.objects.all()
    context = {
        'graphics': graphics,
    }
    return render(request, 'izzytech/graphics_page.html', context)


def web(request):
    web = WebModel.objects.all()
    print(web)
    context = {
        'web': web,
    }
    return render(request, 'izzytech/web.html', context)


def software(request):
    software = SoftwareModel.objects.all()
    context = {
        'software': software,
    }
    return render(request, 'izzytech/software.html', context)


def mobile(request):
    mobile = MobileModel.objects.all()
    context = {
        'mobile': mobile,
    }
    return render(request, 'izzytech/mobile.html', context)


def about(request):
    return render(request, 'izzytech/about.html')


def contact(request):
    return render(request, 'izzytech/contact.html')


def message(request):
    form = MessageModelForm()
    if request.method == 'POST':
        form = MessageModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    context = {
        'form': form,
    }
    return render(request, 'izzytech/message.html', context)

def message_alert(request):
    return render(request, 'izzytech/message_alert.html')