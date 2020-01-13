from django.shortcuts import render
from myapp.models import *
from django.forms import modelformset_factory
# Create your views here.
def index(request,id):
    topic=Topic.objects.get(id=id)
    webpage_form=modelformset_factory(Webpage,exclude=("top_name",),extra=0)
    if request.method=="POST":
        form=webpage_form(request.POST,queryset=Webpage.objects.filter(top_name_id=id))
        if form.is_valid():
            instances=form.save(commit=False)
            for i in instances:
                i.top_name_id=id
                i.save()
        
    form=webpage_form(queryset=Webpage.objects.filter(top_name_id=id))
    return render(request,"index.html",context={"form":form})
    

