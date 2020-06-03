from django.contrib import admin

# Register your models here.

from .models import (
Users, Register
)

admin.site.register(Users)
admin.site.register(Register)
