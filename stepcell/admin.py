from django.contrib import admin
from .models import CarouselItem,YoutubeUpdate,OngoingEvent,Coordinator,VeteranCoordinator,AbhivyaktiEvent,AbhivyaktiPerformingEvent,Team,ControlVolunteer,ControlVeteran,Gallery,OngoingEventCarousel,OngoingEventRegisteration

# Register your models here.
admin.site.register(CarouselItem)
admin.site.register(YoutubeUpdate)
admin.site.register(OngoingEvent)
admin.site.register(Coordinator)
admin.site.register(VeteranCoordinator)
admin.site.register(AbhivyaktiEvent)
admin.site.register(AbhivyaktiPerformingEvent)
admin.site.register(Team)
admin.site.register(ControlVolunteer)
admin.site.register(ControlVeteran)
admin.site.register(Gallery)
admin.site.register(OngoingEventCarousel)
admin.site.register(OngoingEventRegisteration)