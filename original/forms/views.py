from django.shortcuts import render, redirect
from .models import Drop, SaveDrop
from django.http import HttpResponse


def index(request):
    Select = Drop.objects.all()
    if request.method == 'POST':
            UserName = request.POST.get('text')
            print(UserName)
            UserNumber = request.POST.get('number')
            dropdown = request.POST.get('SelectOptionClass')
            SaveValue = SaveDrop()
            SaveValue.UserName = UserName
            SaveValue.UserNumber = UserNumber
            SaveValue.DataSave = dropdown

            SaveValue.save()
            return redirect('/')
    else:
        return render(request, 'form.html', {'Select': Select})


