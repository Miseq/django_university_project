from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.urls import reverse
from rest_framework import viewsets

from .forms import *
from .models import *
from .serializers import PlaceSerializer


def index(request):
    return render(request, 'index.html');


def kontakt(request):
    q = Profile.objects.filter(user=request.user)
    Prof = get_object_or_404(q)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = request.POST.get('form_message', '')
            template = get_template('email.txt')
            context = {
                'message': message,
            }
            wiadomosc = template.render(context)
            email = EmailMessage(
                "Wiadomosc zostala wyslana",
                wiadomosc,
                "Projekt" + '',
                ['testing@example.com'],
                headers={'Odpowiedz': Prof.Email}
            )
            email.send()
            return redirect('kontakt')
    return render(request, 'kontakt.html', {'Profile': Prof})


def konto(request):
    q = Profile.objects.filter(user=request.user)
    Prof = get_object_or_404(q)
    return render(request, 'konto.html', {'Profile': Prof})


@login_required(login_url='/logowanie/')
def konto_edycja(request):
    q = User.objects.filter(pk=request.user.pk)
    gu = get_object_or_404(q)
    if (request.user.username != gu.username):
        return redirect('/')
    forms1 = NicknameChangeForm()
    forms2 = PasswordChangeForm()
    forms3 = PrivacyChangeForm()
    if (request.method == 'POST'):
        error = False
        if (request.POST.get("c") == "b1"):
            formularz = NicknameChangeForm(request.POST)
            if (formularz.is_valid()):
                message = "Twoja nazwa użytkownika została zmieniona"
                cd = formularz.cleaned_data
                wu = User.objects.filter(username=cd['username'])
                if not wu:
                    gu.username = cd['username']
                else:
                    error = True
                    message = "Użytkownik o takim nicku już jest w bazie"
        elif (request.POST.get("c") == "b2"):
            message = 'Twoje hasło zostało zmienione'
            formularz = PasswordChangeForm(request.POST)
            if (formularz.is_valid()):
                cd = formularz.cleaned_data
                if (gu.check_password(cd['old_pass']) and cd['new_pass'] == cd['new_pass1']):
                    if (len(cd['new_pass']) >= 8):
                        ml = False
                        for i in cd['new_pass']:
                            if (i >= '0' and i <= '9'):
                                ml = True
                        if (ml):
                            gu.set_password(cd['new_pass'])
                        else:
                            error = True
                            message = 'Hasło powinno zawierać przynajmniej jedną cyfrę'
                    else:
                        error = True
                        message = "Hasło jest za krótkie"
                else:
                    error = True
                    message = "Hasła nie są takie same lub stare haslo nie jest poprawne"
        else:
            formularz = PrivacyChangeForm(request.POST)
            if (formularz.is_valid()):
                message = 'Twoje ustawienia prywatności zostały zmienione'
                cd = formularz.cleaned_data
                if (cd['accountVisible'] == 1):
                    gu.IsPrivate = True
                else:
                    gu.IsPrivate = False
        gu.save()
    return render(request, 'konto_edycja.html', locals())


def logowanie(request):
    username = ''
    password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    return render(request, 'logowanie.html')


def miejsca(request):
    places = Place.objects.all()
    if request.method == 'POST':
        sort = request.POST['sort']
        if sort == 'nazwar':
            places = places.order_by('Name')
        elif sort == 'nazwam':
            places = places.order_by('-Name')

    else:
        context_dict = {}
    return render(request, 'miejsca.html', locals())


def miejsce_id(request, PlaceID):
    place = Place.objects.filter(PlaceID=PlaceID)
    GotPlace = get_object_or_404(place)
    placeNotes = PlaceNote.objects.order_by('InsertDate').filter(PlaceID=PlaceID)
    sum = 0
    quantity = 0
    counterOfNotes = 0
    for note in placeNotes:
        sum = sum + note.Note
        quantity = quantity + 1
    if quantity != 0:
        notePlace = sum / quantity
    else:
        notePlace = 0
    for rate in placeNotes:
        if rate.UserID_id == request.user.id:
            counterOfNotes += 1
    placeComment = PlaceComment.objects.order_by('InsertDate').filter(PlaceID=PlaceID)
    username = request.user
    placeID = GotPlace.PlaceID
    isAuthor = False
    if request.user.id == GotPlace.UserID_id:
        isAuthor = True
    listOfUsers = []
    listOfProfiles = []
    for comment in placeComment:
        use = User.objects.filter(id=comment.UserID_id)
        GetUse = get_object_or_404(use)
        listOfUsers.append(GetUse)
    for oneUser in listOfUsers:
        profile = Profile.objects.filter(user=oneUser).get()
        listOfProfiles.append(profile)
    commentsAndProfiles = zip(placeComment, listOfProfiles)
    if request.method == 'POST':
        formComment = PlaceCommentForm(request.POST)
        if formComment.is_valid():
            obj = PlaceComment()
            obj.PlaceID_id = PlaceID
            obj.UserID_id = username.id
            obj.Content = formComment.cleaned_data['place_comment']
            obj.save()
        formNote = PlaceNoteForm(request.POST)
        if counterOfNotes:
            if formNote.is_valid():
                noteExist = PlaceNote.objects.filter(UserID_id=request.user.id)
                GetNote = get_object_or_404(noteExist)
                GetNote.Note = int(formNote.cleaned_data['place_note'])
                GetNote.save()
        elif formNote.is_valid():
            note = PlaceNote()
            note.PlaceID_id = PlaceID
            note.UserID_id = username.id
            note.Note = formNote.cleaned_data['place_note']
            note.save()
        redirect_to = reverse('miejsce_id', kwargs={'PlaceID': PlaceID})
        return redirect(redirect_to)
    return render(request, 'miejsce_id.html', locals())


def miejsce_id_edytuj(request, PlaceID):
    obiektPlace = Place.objects.filter(PlaceID=PlaceID)
    error = 0
    username = request.user
    GotPlace = get_object_or_404(obiektPlace)
    if (GotPlace.UserID != username):
        error = 1
        message = "Nie jesteś autorem miejsca"
        return render(request, 'miejsce_id_edytuj.html', locals())
    else:
        if (request.method == 'POST'):
            form1 = PlaceNameForm(request.POST)
            if form1.is_valid():
                obiektNazwa = form1.cleaned_data
                GotPlace.Name = obiektNazwa['place_name']

            form2 = PlaceDescriptionForm(request.POST)
            if form2.is_valid():
                obiektOpis = form2.cleaned_data
                GotPlace.Description = obiektOpis['place_desc']

            form3 = PlacePhotoForm(request.POST)
            if form3.is_valid():
                obiektZdjecie = form3.cleaned_data
                GotPlace.IconURL = obiektZdjecie['place_photo']
        GotPlace.save()

    return render(request, 'miejsce_id_edytuj.html', locals())


def miejsce_dodaj(request):
    if request.method == 'POST':
        form = AddPlaceForm(request.POST)
        if form.is_valid():
            place = Place()
            place.UserID_id = request.user.id
            place.Name = form.cleaned_data['place_name']
            place.Description = form.cleaned_data['place_desc']
            place.IconURL = form.cleaned_data['place_photo']
            place.Location = "123"
            place.save()
        return HttpResponseRedirect('/miejsca')
    return render(request, 'miejsce_dodaj.html')


def o_nas(request):
    if (request.user.is_authenticated):
        error = 0
    else:
        error = 1
    ilosc_adminow = User.objects.all()
    ad = []
    for i in ilosc_adminow:
        if (i.is_superuser):
            ad.append(i)
    return render(request, 'o_nas.html', locals())


def rejestracja(request):
    username = ''
    email = ''
    password = ''
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    if request.method == 'POST':
        if (User.objects.filter(username=username).exists()):
            return render(request, 'rejestracja.html/',
                          {'registrationError': "Użytkownik o podanej nazwie już istnieje"})

        if (User.objects.filter(email=email).exists()):
            return render(request, 'rejestracja.html/',
                          {'registrationError': "Użytkownik o podanym adresie e-mail już istnieje"})

        if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
            User.objects.create_user(username, email, password)
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')

    return render(request, 'rejestracja.html')


def trasa_id(request, RouteID):
    try:
        places = PointOfRoute.objects.filter(RouteID=RouteID)
    except PointOfRoute.DoesNotExist:
        places = None
    routeFilter = Route.objects.filter(RouteID=RouteID)
    route = get_object_or_404(routeFilter)
    addRoutePointForm = AddRoutePointForm()
    if (route.UserID != request.user):
        AuthorError = 1
    if request.method == 'POST':
        form = AddRoutePointForm(request.POST)
        if form.is_valid():
            obj = PointOfRoute()
            obj.IsPlace = True
            obj.Latitude = 0
            obj.Longitude = 0
            obj.PlaceID_id = form.cleaned_data['place'].PlaceID
            obj.RouteID_id = RouteID
            obj.save()
    return render(request, 'trasa_id.html', locals())


def trasa_id_edytuj(request, RouteID):
    routeFilter = Route.objects.filter(RouteID=RouteID)
    route = get_object_or_404(routeFilter)
    error = 0
    username = request.user
    if (route.UserID != username):
        error = 1
        message = "Nie jesteś autorem miejsca"
        return render(request, 'trasa_id_edytuj.html', locals())
    else:
        if (request.method == 'POST'):
            form1 = RouteNameForm(request.POST)
            if form1.is_valid():
                obiektNazwa = form1.cleaned_data
                route.Name = obiektNazwa['route_name']

            form2 = RouteDescriptionForm(request.POST)
            if form2.is_valid():
                obiektOpis = form2.cleaned_data
                route.Description = obiektOpis['route_desc']

        route.save()
    return render(request, 'trasa_id_edytuj.html', locals())


def trasa_dodaj(request):
    if request.method == 'POST':
        form = AddRouteForm(request.POST)
        if form.is_valid():
            route = Route()
            route.UserID_id = request.user.id
            route.Name = form.cleaned_data['route_name']
            route.Description = form.cleaned_data['route_desc']
            route.Points = ""
            route.save()
            return HttpResponseRedirect('/trasy/')
    return render(request, 'trasa_dodaj.html')


def trasy(request):
    routes = Route.objects.all()
    if request.method == 'POST':
        sort = request.POST['sort']
        if sort == 'nazwar':
            routes = routes.order_by('Name')
        elif sort == 'nazwam':
            routes = routes.order_by('-Name')
        elif sort == 'lokalizacjar':
            routes = routes.order_by('Location')
        elif sort == 'lokalizacjam':
            routes = routes.order_by('-Location')
    else:
        context_dict = {}
    return render(request, 'trasy.html', locals())


def widok_trendow(request):
    places = Place.objects.all()[:6]
    return render(request, 'widok_trendow.html', locals())


# Create your views here.
class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


# Create your views here.
def RoutePlaces(request, pk):
    try:
        places = PointOfRoute.objects.filter(RouteID=pk).values_list('PlaceID', flat=True)
        queryset = Place.objects.filter(PlaceID__in=places)
    except Place.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PlaceSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
