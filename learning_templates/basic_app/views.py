from django.shortcuts import render

def index(request):
    context_dic = {'name':"morteza eskandarian", 'eshgh':"asra abidaryan"}
    return render(request, 'basic_app/index.html', context=context_dic)

def other(request):
    return render(request, 'basic_app/other.html')

def relevent(request):
    return render(request, 'basic_app/relevent_page.html')

# Create your views here.
