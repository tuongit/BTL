from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class User(AbstractUser):
    avatar = models.ImageField(null=True, upload_to='users/%Y/%m')


class ModelBase(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tour(ModelBase):
    name = models.TextField(max_length=255, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='toursImage/%Y/%m')
    price = models.TextField(null=True)
    numberPerson = models.IntegerField(null=True)
    numberDay = models.IntegerField(null=True)
    locations = models.ManyToManyField('Location', blank=True, related_name='transports')

    def __str__(self):
        return self.name


class Transport(ModelBase):
    name = models.TextField(max_length=255, null=True)
    price = models.TextField(null=True)
    description = models.TextField(null=True)
    tours = models.ManyToManyField('Tour', blank=True, related_name='transports')

    def __str__(self):
        return self.name


class Location(ModelBase):
    name = models.TextField(max_length=255, null=True)
    description =models.TextField(null=True)

    def __str__(self):
        return self.name


class ActionBase(ModelBase):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'tour')
        abstract = True


class Like(ActionBase):
    active = models.BooleanField(default=False)


class Rating(ActionBase):
    rate = models.SmallIntegerField(default=0)
