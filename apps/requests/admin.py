from django.contrib import admin

from .models import Request

class RequestAdmin(admin.ModelAdmin):
	list_display = ['date', 'method', 'path']

admin.site.register(Request, RequestAdmin)
