# views.py
from django.shortcuts import render, redirect
from .forms import MemberForm
from .models import Member

def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'member_form.html', {'form': form})

def member_list(request):
    members = Member.objects.all()
    return render(request, 'member_list.html', {'members': members})
