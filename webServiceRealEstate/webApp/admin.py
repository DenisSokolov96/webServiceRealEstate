from django.contrib import admin
from .models import Sellers, Buyers, Directory


admin.site.register(Sellers)
admin.site.register(Buyers)
admin.site.register(Directory)
