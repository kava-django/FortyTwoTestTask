from django.db import models


class MyContacts(models.Model):
    name = models.CharField(max_length=70)
    surname = models.CharField(max_length=90)
    date_of_birth = models.DateField()
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length=50)
    other_contacts = models.TextField()


    def __unicode__(self):
        return self.name
