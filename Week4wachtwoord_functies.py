import random
import string

# functie om te kiezen tussen de verschillende manieren van genereren van een wachtwoord, afhankelijk van de complexiteit
def genereer_wachtwoord(lengte, complexiteit):
    functies = [genereer_met_cijfers, genereer_met_hoofdletters, genereer_met_kleineletters, genereer_met_leestekens]
    wachtwoord = ''

    for i in range(complexiteit):
        wachtwoord += functies[i % 4](lengte // complexiteit)
        # iedere keer dat de lus wordt doorlopen, wordt er een functie gekozen uit de lijst functies. % 4 is modulo vier en zorgt dat als je een grote complexiteit hebt, je niet buiten de lijst functies komt.
        # lengte // complexiteit geeft aan de functie mee dat er een deel van het wachtwoord gemaakt wordt.
        # +=  doet het zelfde als wachtwoord = wachtwoord + functies[_ % 4](lengte // complexiteit) maar is korter.
        # je kan ook als volgt doen
        # deel_wachtwoord = functies[_ % 4](lengte // complexiteit)
        # wachtwoord = wachtwoord + deel_wachtwoord

    # Als het wacthwoord nog niet lang genoeg is, wordt er een willekeurige functie gekozen

    while len(wachtwoord) < lengte:
        wachtwoord += random.choice(functies)(lengte - len(wachtwoord))

    # Ten slotte wordt de volgorde van de karakters in het wachtwoord gemengd met behulp van random.sample() om een wachtwoord te genereren dat geen voorspelbaar patroon heeft.
    return ''.join(random.sample(wachtwoord, len(wachtwoord)))

def genereer_met_cijfers(lengte)
    return ''.join(random.choice(string.digits) for i in range(lengte))

def genereer_met_hoofdletters(lengte):
return ''.join(random.choice(string.ascii_uppercase) for i in range(lengte))

def genereer_met_kleineletters(lengte):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(lengte))

def genereer_met_leestekens():
     ''.join(random.choice(string.punctuation) for i in range(lengte))