from email import message
from multiprocessing import context
from django.shortcuts import render
# from .models import DM
from django.contrib.auth.models import User
# Create your views here.

# def directmessage(request, pk):
#     user = User.objects.get(id=pk)
#     dmessage = user.dm.set.all()
#     context = {'user': user, 'message': dmessage}

#     return render(request, 'dms/messages.html', context)