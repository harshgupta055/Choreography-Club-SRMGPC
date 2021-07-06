from django.contrib import messages
from django.shortcuts import redirect, render

from .models import CarouselItem, OngoingEventCarousel,YoutubeUpdate,OngoingEvent,Coordinator,VeteranCoordinator,AbhivyaktiEvent,AbhivyaktiPerformingEvent,Team,ControlVolunteer,ControlVeteran,Gallery,OngoingEventRegisteration
from .tasks import contact_mail,self_contact_mail,ongoing_event_mail,sending_mail

from django.core.paginator import Paginator


# Create your views here.

def home(request):
    carouselItem = CarouselItem.objects.all()
    youtubeUpdate = YoutubeUpdate.objects.all()
    ongoingEvent = OngoingEvent.objects.all()
    coordinators = Coordinator.objects.all()
    veteranCoordinators = VeteranCoordinator.objects.all()
    context = {
        'carouselItem':carouselItem,
        'youtubeUpdate':youtubeUpdate,
        'ongoingEvent':ongoingEvent,
        'coordinators':coordinators,
        'veteranCoordinators':veteranCoordinators,
    }
    return render(request,'home.html',context)

def eventPage(request):
    ongoingEvent = OngoingEvent.objects.all()
    abhivyaktiEvent = AbhivyaktiEvent.objects.all()
    abhivyaktiPerforming = AbhivyaktiPerformingEvent.objects.all()
    context = {
        'ongoingEvent':ongoingEvent,
        'abhivyaktiEvent':abhivyaktiEvent,
        'abhivyaktiPerforming':abhivyaktiPerforming,
    }
    return render(request,'event.html',context)

def galleryPage(request):
    gallery = Gallery.objects.all().order_by("id")
    paginator = Paginator(gallery, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj,
    }
    return render(request,"gallery.html",context)

def volunteerPage(request):
    controlVolunteer = ControlVolunteer.objects.all()
    volunteers = Team.objects.all()
    context = {
        'controlVolunteer':controlVolunteer,
        'volunteers':volunteers,
    }
    return render(request,"volunteer.html",context)

def veteranPage(request):
    controlVeteran = ControlVeteran.objects.all()
    veterans = Team.objects.all()
    context = {
        'controlVeteran':controlVeteran,
        'veterans':veterans,
    }
    return render(request,"veterans.html",context)

def contactPage(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query')
        page = request.POST.get('page')
        contact_mail(name=name,email=email)
        self_contact_mail(name=name,query=query)
        messages.success(request, 'Your query has been submitted!')
        if page == "contact":
            return redirect("contactPage")
        elif page == "home":
            return redirect("homePage")
    return render(request,'contact.html')

def aboutPage(request):
    return render(request,"about.html")

def ongoingEvent(request):
    carousel = OngoingEventCarousel.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        college = request.POST.get("college")
        # form = OngoingEventRegisteration(name=name,email=email,phone=phone,college=college)
        # form.save()
        ongoing_event_mail(name=name,email=email)
        return render(request,'thankyou.html',{'user':name})
        
    context = {
        'carousel':carousel,
    }
    return render(request,'ongoingEvent.html',context)


def viewOngoingEventRegisteration(request):
    registerations = OngoingEventRegisteration.objects.all()
    total = registerations.count()
    context = {
        'registerations':registerations,
        'total':total,
    }
    return render(request,'registerations.html',context)


def sendingEmailPage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        sending_mail(name=name,email=email)
        return redirect('sendingEmailPage')

    registerations = OngoingEventRegisteration.objects.all()
    context ={
        'registerations':registerations,
    }
    return render(request,'sendingEmailPage.html',context)