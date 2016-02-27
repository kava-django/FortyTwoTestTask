from django.contrib import admin

from apps.hello.models import MyContacts

class MyContactsAdmin(admin.ModelAdmin):
	list_display = ['name', 'surname', 'email', 'skype']

admin.site.register(MyContacts, MyContactsAdmin)


