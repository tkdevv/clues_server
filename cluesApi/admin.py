from django.contrib import admin
from .models import LatestVersion, Card

# Register your models here.
admin.site.register(Card)
admin.site.register(LatestVersion)
