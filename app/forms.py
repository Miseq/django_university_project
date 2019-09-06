from django import forms

from .models import Place


class NicknameChangeForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', }))


class PasswordChangeForm(forms.Form):
    old_pass = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', }))
    new_pass = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', }))
    new_pass1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', }))


class PrivacyChangeForm(forms.Form):
    accountVisible = forms.BooleanField(required=False)


class PlaceNameForm(forms.Form):
    place_name = forms.CharField(max_length=50)


class PlaceDescriptionForm(forms.Form):
    place_desc = forms.CharField(max_length=1000)


class PlaceNoteForm(forms.Form):
    place_note = forms.IntegerField()


class PlacePhotoForm(forms.Form):
    place_photo = forms.CharField(max_length=3000)


class PlaceCommentForm(forms.Form):
    place_comment = forms.CharField(max_length=1000)


class RouteNameForm(forms.Form):
    route_name = forms.CharField(max_length=50)


class RouteDescriptionForm(forms.Form):
    route_desc = forms.CharField(max_length=1000)


class RouteNoteForm(forms.Form):
    route_note = forms.IntegerField()


class RouteCommentForm(forms.Form):
    route_comment = forms.CharField(max_length=1000)


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username',
        max_length=32
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        max_length=32,
    )
    password = forms.CharField(
        required=True,
        label='Password',
        max_length=32,
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        required=True,
        label='Password2',
        max_length=32,
        widget=forms.PasswordInput()
    )


class AddRouteForm(forms.Form):
    route_name = forms.CharField(max_length=50)
    route_desc = forms.CharField(max_length=50)


class AddRoutePointForm(forms.Form):
    place = forms.ModelChoiceField(queryset=Place.objects.all())


class AddPlaceForm(forms.Form):
    place_name = forms.CharField(max_length=50)
    place_desc = forms.CharField(max_length=50)
    place_photo = forms.URLField()


class ContactForm(forms.Form):
    form_message = forms.CharField(required=True, widget=forms.Textarea)
