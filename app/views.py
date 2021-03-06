from django.shortcuts import render,redirect
from forms import componentForm, tutorialForm
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from models import *
# Create your views here.
def index(request):
    template="app/index.html"
    context={}
    
    tutorials=tutorialModel.objects.all()
    context["tutorials"]=tutorials
    
    tags=tagModel.objects.all()
    context["tags"]=tags
        
    
    return render(request,template,context)

def viewTutorial(request,tutorial):
    template="app/view.html"
    context={}
    
    tutorial=tutorialModel.objects.get(id=tutorial)
    context["tutorial"]=tutorial
    components=[]
    for i in tutorial.component.all().order_by("order"):
        components.append(i)
    context["components"]=components
    
    return render(request,template,context)

def addTutorial(request):
    template="app/addTutorial.html"
    context={}
    if request.method=="POST":
        form=tutorialForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            title=instance.title
            instance.save()
            tutorial=tutorialModel.objects.filter(title=title)[0]
            return redirect(reverse('app:view', kwargs={'tutorial': tutorial.id}))
        else:
            print "form invalid?"
    else:
        form=tutorialForm()
        context["form"]=form
    
    return render(request,template,context)
    
@staff_member_required    
def editTutorial(request,tutorial):
    template="app/edit.html"
    context={}
    
    #c1=componentModel(componentType="text",order=0,componentContent="this is the second tutorial")
    #c2=componentModel(componentType="text",order=1,componentContent="This comes second")
    #c3=componentModel(componentType="image",image="http://lazypenguins.com/wp-content/uploads/2015/08/Red-Panda-Surprise.jpg",imageCaption="this is a red panda")
    #c1.save()
    #c2.save()
    #c3.save()
    #t1=tutorialModel(title="how to do stuff2,electric boogaloo")
    #t1.save()
    #t1.component.add(c1,c2,)#c3)
    #t1.save()
    try:
        a=tutorial=tutorialModel.objects.get(id=tutorial)
    except:
        a=tutorialModel(title=tutorial)
    context["tutorial"]=a
    components=[]
    for i in a.component.all().order_by("order"):
        components.append(i)
        
    
    
    forms=[]
    for i in components:
        forms.append(componentForm(instance=i))
        
    
        
    context["components"]=components
    context["forms"]=forms
    zipList=zip(components,forms)
    context["zipList"]=zipList    

    
    
    return render(request,template,context)
@staff_member_required
def addComponent(request,tutorial):
        
        component=componentModel(order=0)
        component.save()
        tutorial=tutorialModel.objects.filter(id=tutorial)[0]
        tutorial.component.add(component)
        tutorial.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
@staff_member_required    
def editComponent(request,primaryKey):
    try:
        component=componentModel.objects.filter(id=primaryKey)[0]
    except:
        component=componentModel(order=0)
        component.save()
    
    if request.method=="POST":
        form = componentForm(request.POST,instance=component)
        if form.is_valid:
            form.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
def searchView(request):
    template="app/search.html"
    context={}
    #searchTerm=request.POST
    searchTerm= request.POST["searchParam"]
    results=tutorialModel.objects.filter(title__contains=searchTerm)
    context["results"]=results
    return render(request,template,context)

def addTag(request,tag,tutorial):
    
    try:
        tag=tagModel.objects.get(tag=tag)
    except:
        tag=tagModel(tag=tag)
        tag.save(commit=False)
        
    tutorial=tutorialModel.objects.get(id=tutorial)
    tag.tutorials.add(tutorial)
    tag.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        