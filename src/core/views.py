from django.shortcuts import render
from .forms import ContactForm
from .models import PhoneBook
from django.http import HttpResponse
from .filters import UserFilter

# Create your views here.
def index(request):
    form = ContactForm()
    all_entries = PhoneBook.objects.all()
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            workplace = form.cleaned_data['workplace']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            age = form.cleaned_data['age']
            print(firstname+' '+lastname)
            form.save()
    form = ContactForm()
    return render(request,'index.html',{"form":form})

def search(request):
    all_entries = PhoneBook.objects.all()
    user_filter = UserFilter(request.GET, queryset=all_entries)
    return render(request,'search.html',{'filter': user_filter})

