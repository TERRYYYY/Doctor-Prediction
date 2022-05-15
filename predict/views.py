from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
# from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
import pandas as pd

# Create your views here.
# @login_required(login_url='login')
def home(request):
    return render(request, 'predict.html')

def index(request):
    return render (request, 'index.html' )

def registerPage(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account Successfully created for ' + user)
            return redirect('login')
            
    context = {'form':form}
    return render(request,'registration/register.html',context)

def loginPage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            
    
    context = {}
    return render(request, 'registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login') 

def predict_chances(request):
    if request.POST.get('action') == 'POST':
        #receive data from user
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))
        
        model = pd.read_pickle(r"C:\Users\HP\Downloads\new_model.pickle")
        
        #Make prediction
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

        classification = result[0]
        
        return JsonResponse({'result': classification, 'sepal_length': sepal_length, 'sepal_width': sepal_width, 'petal_length': petal_length, 'petal_width': petal_width}, safe=False)

    # if request.POST.get('action') == 'post':
    
    #     # Receive data from client
    #     sepal_length = float(request.POST.get('sepal_length'))
    #     sepal_width = float(request.POST.get('sepal_width'))
    #     petal_length = float(request.POST.get('petal_length'))
    #     petal_width = float(request.POST.get('petal_width'))

    #     # Unpickle model
    #     model = pd.read_pickle(r"C:\Users\azander\Downloads\new_model.pickle")
    #     # Make prediction
    #     result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

    #     classification = result[0]

    #     PredResults.objects.create(sepal_length=sepal_length, sepal_width=sepal_width, petal_length=petal_length,
    #                                petal_width=petal_width, classification=classification)

    #     return JsonResponse({'result': classification, 'sepal_length': sepal_length,
    #                          'sepal_width': sepal_width, 'petal_length': petal_length, 'petal_width': petal_width},
    #                         safe=False)
