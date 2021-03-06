from django.db import models
from django.utils import timezone

from enum import Enum


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200, default='')
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Size(Enum):
    XS = 'XS'
    S = 'S'
    M = 'M'
    L = 'L'
    XL = 'XL'

class ITEM_TYPE_CHOICES(Enum):
    Unisex = 'Unisex'
    Man = 'Man'
    Woman = 'Woman'
    
class ACCESSORY_TYPE_CHOICE(Enum):
    Accessories = 'Accessories'
    Bracelets = 'Bracelets'


class Item(models.Model):
    code = models.CharField(max_length=10, default='')
    item_name = models.CharField(max_length=50, default='')
    item_type = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in ITEM_TYPE_CHOICES], default='')
    color = models.CharField(max_length=50, default='')
    tot_XS = models.PositiveSmallIntegerField(default=0)
    remaining_XS = models.PositiveSmallIntegerField(default=0)
    tot_S = models.PositiveSmallIntegerField(default=0)
    remaining_S = models.PositiveSmallIntegerField(default=0)
    tot_M = models.PositiveSmallIntegerField(default=0)
    remaining_M = models.PositiveSmallIntegerField(default=0)
    tot_L = models.PositiveSmallIntegerField(default=0)
    remaining_L = models.PositiveSmallIntegerField(default=0)
    tot_XL = models.PositiveSmallIntegerField(default=0)
    remaining_XL = models.PositiveSmallIntegerField(default=0)
    # image = models.ImageField(upload_to='media/%Y/%m/%d/', null=True, blank=True)

class AccessoryItem(models.Model):
    code = models.CharField(max_length=10, default='')
    item_name = models.CharField(max_length=50, default='')
    item_type = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in ACCESSORY_TYPE_CHOICE], default='')
    color = models.CharField(max_length=50, default='')
    tot = models.PositiveSmallIntegerField(default=0)
    tot_remaining = models.PositiveSmallIntegerField(default=0)


class Man(models.Model):
    code = models.CharField(max_length=10, default='')
    size = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in Size], default='')
    sold = models.PositiveSmallIntegerField(default=0)
    activity = models.CharField(max_length=50, default='')
    created_date = models.DateTimeField(default=timezone.now)

class Woman(models.Model):
    code = models.CharField(max_length=10, default='')
    size = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in Size], default='')
    sold = models.PositiveSmallIntegerField(default=0)
    activity = models.CharField(max_length=50, default='')
    created_date = models.DateTimeField(default=timezone.now)

class Unisex(models.Model):
    code = models.CharField(max_length=10, default='')
    size = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in Size], default='')
    sold = models.PositiveSmallIntegerField(default=0)
    activity = models.CharField(max_length=50, default='')
    created_date = models.DateTimeField(default=timezone.now)

class Accessories(models.Model):
    code = models.CharField(max_length=10, default='')
    sold = models.PositiveSmallIntegerField(default=0)
    activity = models.CharField(max_length=50, default='')
    created_date = models.DateTimeField(default=timezone.now)


