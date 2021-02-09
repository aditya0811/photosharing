from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from memes.models import *
from django.http import Http404
from django.http import HttpResponse
from memes.forms import *
# Create your views here.
def index(request):
    req_memes=100
    endp=min(req_memes,len(Meme.objects.all()))
    memes=Meme.objects.all().order_by('-id')[:endp]
    form =MemeForm()

    if request.method=="POST":
        form=MemeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context={'memes':memes,'form':form}
    return render(request,'memefr/list.html',context)

#FAULTY
def search(request,id):
    temp = Meme.objects.filter(id__icontains=id)
    return render(request, 'memefr/search_results.html',{'temp': temp, 'id': id})

def ed(request,id):
    return render(request, 'memefr/ed.html',{'id': id})
    # temp = Meme.objects.filter(id__icontains=id)
    # return render(request, 'memefr/search_results.html',{'temp': temp, 'id': id})