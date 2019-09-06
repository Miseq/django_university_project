from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey  # importuje 2 razy bo pycharm wywala blad
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    UserID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=30, blank=True)
    Surname = models.CharField(max_length=50, blank=True)
    Email = models.EmailField(max_length=254)
    IsPrivate = models.NullBooleanField()
    IsOrganisation = models.NullBooleanField()
    IsAdmin = models.BooleanField(default=False)
    AvatarURL = models.CharField(max_length=3000, default='http://fastestlaps.com/ui_images/default_avatar.png')
    Description = models.CharField(max_length=1000, blank=True)
    JoinDate = models.DateField(auto_now_add=True)
    Score = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Route(models.Model):
    RouteID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50, blank=True)
    Points = models.TextField()
    Description = models.CharField(max_length=1000, blank=True)
    IsPublic = models.BooleanField(default=True)
    InsertDate = models.DateField(auto_now_add=True)
    UserID = ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class Place(models.Model):
    PlaceID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=1000, blank=True)
    IconURL = models.URLField(max_length=3000)
    IsPublic = models.BooleanField(default=False)
    InsertDate = models.DateField(auto_now_add=True)
    UserID = ForeignKey(User, on_delete=models.CASCADE)
    Latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    Longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)

    def __str__(self):
        return self.Name


class Tag(models.Model):
    TagID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Kind = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class RoutePhoto(models.Model):
    RoutePhotoID = models.AutoField(primary_key=True)
    PhotoURL = models.CharField(max_length=3000)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    RouteID = models.ForeignKey(Route, on_delete=models.CASCADE)

    def __str__(self):
        return self.RouteID


class TagRoute(models.Model):
    TagRouteID = models.AutoField(primary_key=True)
    RouteID = models.ForeignKey(Route, on_delete=models.CASCADE)
    TagID = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.RouteID


class TagPlace(models.Model):
    TagPlaceID = models.AutoField(primary_key=True)
    PlaceID = models.ForeignKey(Place, on_delete=models.CASCADE)
    TagID = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.PlaceID


class PlaceComment(models.Model):
    PlaceCommentID = models.AutoField(primary_key=True)
    Content = models.CharField(max_length=1000)
    InsertDate = models.DateField(auto_now_add=True)
    PlaceID = models.ForeignKey(Place, on_delete=models.CASCADE)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.PlaceID


class PointOfRoute(models.Model):
    PointOfRouteID = models.AutoField(primary_key=True)
    Latitude = models.IntegerField()
    Longitude = models.IntegerField()
    IsPlace = models.CharField(max_length=1)
    RouteID = models.ForeignKey(Route, on_delete=models.CASCADE)
    PlaceID = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.PlaceID


class PlaceNote(models.Model):
    PlaceNoteID = models.AutoField(primary_key=True)
    Note = models.SmallIntegerField()
    InsertDate = models.DateField(auto_now_add=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    PlaceID = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return self.PlaceID


class PlacePhoto(models.Model):
    PlacePhoto = models.AutoField(primary_key=True)
    PhotoURL = models.CharField(max_length=3000)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    PlaceID = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return self.PlaceID


class RouteComment(models.Model):
    RouteCommentID = models.AutoField(primary_key=True)
    Content = models.CharField(max_length=1000)
    InsertDate = models.DateField(auto_now_add=True)
    RouteID = models.ForeignKey(Route, on_delete=models.CASCADE)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.RouteID


class RouteNote(models.Model):
    RouteNoteID = models.AutoField(primary_key=True)
    Note = models.SmallIntegerField()
    InsertDate = models.DateField(auto_now_add=True)
    RouteID = models.ForeignKey(Route, on_delete=models.CASCADE)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.RouteID
