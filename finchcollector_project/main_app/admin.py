from django.contrib import admin

from .models import Finch, Feeding, Toy

admin.site.register(Finch)
admin.site.register(Toy)
admin.site.register(Feeding)
