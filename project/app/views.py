from django.shortcuts import render

# Create your views here.
# def home(request):
#     return render(request,'home.html')
def integer(request,pk):
    data=pk
    return render(request,'home.html',{'key':data})

def  string(request,pk):
    data=pk
    return render(request,'home.html',{'key':data})

def  slug123(request,pk):
    data=pk
    return render(request,'home.html',{'key':data})

def  path123(request,pk):
    data=pk
    return render(request,'home.html',{'key':data})

def combination(request,pk,pk1,pk2,pk3):
    data= {
        'data1':pk,
        'data2':pk1,
        'data3':pk2,
        'data4':pk3,
    }
    return render(request,'home.html',{'key':data})