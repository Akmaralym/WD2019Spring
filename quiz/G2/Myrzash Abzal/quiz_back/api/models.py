from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ContactManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = ContactManager()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone
        }