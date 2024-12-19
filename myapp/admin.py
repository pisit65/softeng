from django.contrib import admin
from .models import Device, BorrowRecord

# Register your models here.
admin.site.register(Device)
admin.site.register(BorrowRecord)