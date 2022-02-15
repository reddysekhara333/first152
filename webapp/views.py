from django.shortcuts import render

# Create your views here.
from webapp import forms
from django.http import  HttpResponseRedirect
def emp_view(request):
    fr=forms.formmodel()
    if request.method=='POST':
        fr=forms.formmodel(request.POST)
        if fr.is_valid():
            fr.save(commit=True)
            return HttpResponseRedirect('/bye')
    else:
        fr=forms.formmodel()
        return render(request,'myapp/h.html',{'fr':fr})
def thanks(request):
    return render(request,'myapp/t.html')