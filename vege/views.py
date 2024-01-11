from django.shortcuts import render,redirect
from.models import *
# from django.http import HttpResponse
# Create your views here.


def receipes(request):
    # return HttpResponse("hello ")
     data = request.POST
     if request.method == "POST":
        # print(data)
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        Receipe.objects.create(
            receipe_image = receipe_image,
            receipe_name = receipe_name,
            receipe_description = receipe_description,
        )
        # print(receipe_name)
        # print(receipe_description)
        # print(receipe_image)
        # receipe_image = data.get(receipe_image)
        return redirect('/')
     queryset = Receipe.objects.all()
     context = {'receipes': queryset}
     return render(request, 'receipes.html',context)