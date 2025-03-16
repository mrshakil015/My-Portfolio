from django.shortcuts import render

# Create your views here.
def home(request):
    
    return render(request,'frontend/home.html')
def home2(request):
    
    return render(request,'frontend/base2/base.html')