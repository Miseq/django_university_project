# Zaplanuj swój projekt
Oficjalny GitHub projektu. Grupa L01 2EF-DI.

## Skład zespołu:
 1. Krzysztof Nowakowski *Lider*
 2. Łukasz Bartoszek *Architekt*
 3. Łukasz Barański
 4. Jakub Radziwiński
 5. Łukasz Bizoń
 6. Szymon Wawrzaszek
 7. Mateusz Popera
 8. Dawid Burdzy
 9. Paweł Balwierczak
 10. Rafał Bednarczuk
 11. Mateusz Zawadzki
 12. Mateusz Zyga
 13. Mariusz Bigos
 14. Damian Bielenda
 15. Karol Baran
 
 ## Zadania
1. login - Krzysztof Nowakowski
2. strona główna - Łukasz Bartoszek
3. rejestracja- Mateusz Zawadzki 
4. Zapomniałem hasła/loginu/nazwy użytkowniak - Dawid Burdzy
5. Miejsca - Jakub Radziwinski
6. Pasek nawigacji - Łukasz Bizon    
7. Widok mapy - Rafał Bednarczuk 
8. Widok trasy - Mateusz Zyga
9. Widok trendów - Szymon Wawrzaszek
10. O nas - Paweł Balwierczak 
11. Strona konkretnego miejsca - Mariusz Bigos	
12. Strona edycji miejsca - Łukasz Baranski
13. Konto - Damian Bielenda 
14. Edycja konta - Karol Baran 
15. Kontakt - Mateusz Popera 
 
 
## Wprowadzenie
**Jak uruchomić projekt?**
 1. Pobieramy oraz instalujemy Git
 2. Tworzymy folder, w którym ma się znajdować nasz projekt
 3. Klikamy w folderze prawy przycisk myszy trzymając wciśnięty klawisz Shift i wybieramy Otwórz okno polecenia/PowerShell tutaj.
 4. Wpisujemy komendę i zatwierdzamy enterem:
   `git clone https://github.com/PRz-IO/l01-nr-2-zaplanuj-swoj-wyjazd-gr-l01-2018.git`
 5. Pobieramy i instalujemy Python, najnowszą wersję: 
    https://www.python.org/
 6. Pobieramy ten plik i zapisujemy go do innego folderu:
	https://bootstrap.pypa.io/get-pip.py
 7. W tym folderze otwieramy konsolę, tak jak poprzednio i wpisujemy `python get-pip.py` i enter.
 8. Wpisujemy `pip install django` i enter.
 9. Wpisujemy kolejno:
    * `pip install djangorestframework`
	* `pip install markdown`
	* `pip install django-filter`
 10. Wchodzimy do folderu w którym mamy nasz projekt. Powinien tam być plik manage.py. Odpalamy tu konsolę i wpisujemy:
	`python manage.py runserver`
 11. W przeglądarce nasza strona powinna być pod adresem:
	http://localhost:8000
 12. Aby zakończyć działanie serwera wciskamy CTRL+C w konsoli.
	
**Przed rozpoczęciem pracy:**
 1. Robimy pull requesta z głównego brancha (master) do naszego. Branch każdej osoby powinien wyglądać wg wzoru imie-nazwisko. Aby zrobić pull requesta wchodzimy na stronę główną projektu na GitHubie i naciskamy pull request. Następnie jako base wybieramy nasz brach (`imie-nazwisko`) a jako compare `master`. Nazwa każdego pulla z mastera do nas powinna mieć nazwę `pull-imie-nazwisko`. Na koniec klikamy Create pull request. 
 2. Wchodzimy w pull requests na stronie głównej projektu w GitHubie i wybieramy nasz pull request (`pull-imie-nazwisko`). Następnie wybieramy Merge pull request oraz confirm merge.
 3. Upewniamy się, że git pracuje w naszym branchu za pomocą polecenia `git checkout imie-nazwisko`. To polecenie wystarczy wykonać tylko raz, na samym początku.
 4. Robimy pulla: `git pull`.
 5. Wszystko gotowe do pracy.

**Zasady pracy**
 1. Po skończonej pracy nad danym elementem robimy commit. Commit ma być możliwie jak najkrótszym opisem dokonanych przez nas zmian.
 2. Po skończonej pracy nad wszystkimi elementami robimy pull requesta z naszego brancha do mastera.

**Robienie commitów i pull requestów:**
 1. Wpisujemy `git add .` w głównym katalogu projektu.
 2. Wpisujemy `git commit -m "tekst"`. W ten sposób tworzy się commita. "tekst" to jego nazwa.
 3. Po dodaniu wszystkich commitów jakie chcieliśmy robimy pusha: `git push`.
 4. Wchodzimy na GitHuba i robimy pull requesta z naszego brancha do mastera i czekamy na zatwierdzenie przez admina.
