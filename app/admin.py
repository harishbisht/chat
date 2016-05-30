from django.contrib import admin

# Register your models here.
from .models import NewPerson, Waiting , Pairing,Message

admin.site.register(NewPerson)
admin.site.register(Waiting)
admin.site.register(Pairing)
admin.site.register(Message)
