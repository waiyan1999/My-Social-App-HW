from django.shortcuts import render

# Create your views here.

def baseindex(request):
    return render(request,"baseindex.html")

def footer(request):
    return render(request,'footer.html')

def post(request):
    return render(request, 'post.html')

def user(request):
    return render(request,'user.html')