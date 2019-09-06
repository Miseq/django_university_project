from django.contrib import admin

from .models import *

admin.site.register(Route)
admin.site.register(Place)
admin.site.register(Tag)
admin.site.register(RoutePhoto)
admin.site.register(TagRoute)
admin.site.register(TagPlace)
admin.site.register(PlaceComment)
admin.site.register(PointOfRoute)
admin.site.register(PlaceNote)
admin.site.register(PlacePhoto)
admin.site.register(RouteComment)
admin.site.register(RouteNote)
admin.site.register(Profile)
# Register your models here.
