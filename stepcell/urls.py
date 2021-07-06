from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="homePage"),
    path("events/",views.eventPage,name="eventPage"),
    path("gallery/",views.galleryPage,name="galleryPage"),

    path("volunteers/",views.volunteerPage,name="volunteerPage"),
    path("veterans/",views.veteranPage,name="veteranPage"),

    path("contact/",views.contactPage,name="contactPage"),
    path("about/",views.aboutPage,name="aboutPage"),

    path('namaskaram/',views.ongoingEvent,name="ongoingEvent"),

    path('viewOngoingEventRegisteration/',views.viewOngoingEventRegisteration,name="viewOngoingEventRegisteration"),
    path('sendingEmail/',views.sendingEmailPage,name="sendingEmailPage"),
]