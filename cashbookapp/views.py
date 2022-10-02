from django.contrib import messages
import datetime
from .models import Cashbook
from django.utils import timezone
from email import message
from multiprocessing import context, reduction
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CashbookForm
# Create your views here.


def main(request):
    return render(request, 'main.html')

def write(request):
    context = {}
    if request.method == 'POST':
        form = CashbookForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.created_at = timezone.now()
            form.save()
            return redirect('read')
        
        else:
            context = {
                'form':form,
            }
            return render(request, 'write.html', context)
    else:
        form = CashbookForm
        # context['form'] = form
        return render(request, 'write.html', {'form': form})


def read(request):
    cashbooks = Cashbook.objects
    return render(request, 'read.html', {'cashbooks': cashbooks})


def detail(request, id):
    cashbooks = get_object_or_404(Cashbook, id=id)
    return render(request, 'detail.html', {'cashbooks': cashbooks})


def edit(request, id):
    cashbooks = get_object_or_404(Cashbook, id = id)
    if request.method == "POST":
        form = CashbookForm(request.POST,request.FILES, instance=cashbooks,)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('read')
        
    else:
        form= CashbookForm(instance=cashbooks)
        return render(request, 'edit.html', {'form':form,'cashbooks':cashbooks})


def delete(request, id):
    cashbooks = get_object_or_404(Cashbook, id= id)
    cashbooks.delete()
    return redirect('read')
