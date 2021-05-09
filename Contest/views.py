from django.shortcuts import render , redirect
from .models import MyContest
from .forms import ContestForm
def allcontest(request):
    contestre = MyContest.objects.all()
    form = ContestForm()
    if request.method == 'POST':
        form = ContestForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'allcontest.html', {'contestre': contestre, 'form' : form})

def deleteItem(request, pick):
    task =  MyContest.objects.get(id=pick)
    task.delete()
    return redirect('allcontest')
def updateItem(request , pick):
    todo = MyContest.objects.get(id=pick)
    updateForm = ContestForm(instance=todo)
    if request.method == 'POST':
        updateForm = ContestForm(request.POST , instance = todo)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('allcontest')
    return render(request , 'updateItem.html' , {'todo': todo, 'updateform': updateForm})

    
    
