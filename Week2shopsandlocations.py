import random
import math

winkelketens = ['Albert Heijn', 'Kruidvat', 'Jumbo', 'Hema', 'Gall & Gall']
steden = ['Amsterdam', 'Rotterdam', 'Utrecht', 'Den Haag', 'Eindhoven']

transacties = {}

# deze code maakt een dictionary met 98 transacties, iedere transactie heeft een winkelnaam, locatie en bedrag en is een list
for i in range(1, 99):
    winkel_naam = random.choice(winkelketens) # random.choice kiest een willekeurig element uit de tuple met winkelketens
    locatie = random.choice(steden) # random.choice kiest een willekeurig element uit de tuple met steden
    bedrag = random.randint(100, 10000) # Dit zie je vaak met bedragen: zit zijn centen, geen euro's. Als je dit wil printen, moet je er een komma tussen zetten
    transacties[i] = (winkel_naam, locatie, bedrag)

# Twee rare gevollen toevoegen
bedrag99 = random.randint(500000, 100000000)
bedrag100 = random.randint(500000, 100000000)
transacties[99] =  ('Albert Heijn', 'Amsterdam', bedrag99)
transacties[100] =  ('Kruidvat', 'Eindhoven', bedrag100)

### Kun je zelf twee getallen kiezen en toevoegen aan de dictionary? Met bedragen die niet zo hoog zijn of juist heel hoog?
# Je code hieronder

assert len(transacties) == 102, "Je hebt geen 102 transacties in je dictionary"

# De hele dictionary
for transactie in transacties.items():
    print(transactie)

## hoe vinden we de rare gevallen?

# Begin met het gemiddelde te berekenen:
## Hier zitten twee fouten in de code, kun je die vinden?
totaal_bedrag = 0
# Haal de comment weg en maak de loop werkend:
#if transactie in transacties.items() # juiste loop?
#    totaal_bedrag = totaal_bedrag + transactie[1][2] # dit telt de bedragen op

print (totaal_bedrag)
## Als het bedrag voor het totaal nu klopt, kun je het gemiddelde berekenen? Kijk anders even op chatpgpt ;-)

gemiddelde = 0 # dit wordt dus een berekening die je nog moet maken ;-)

lengte = len(transacties)
assert  gemiddelde ==  totaal_bedrag/lengte, "Het gemiddelde is niet goed berekend" # dit is een test, als het gemiddelde niet klopt, stopt de code hier

# Om de niet-standaard getallen te vinden, gebruik je vaak wiskundige formules.Hier gaan we voor alle bedragen de afstand tot het gemiddelde berekenen
bedragen = []
for transactie in transacties.items():
    bedragen.append(transactie[1][2]) # dit voegt de bedragen toe aan een list

# Nu de standaard deviatie, hiermee kun je kijken of er uitschieters zijn. Je berekent de afstand tot het gemiddelde
# Dit is een functie.
def calculate_std_dev(gemiddelde, bedragen):
    variance = sum((bedrag - gemiddelde) ** 2 for bedrag in bedragen) / len(bedragen) # De afstand tot het gemiddelde, in het kwadraat
    ## Dus grotere getallen worden nog groter

    # Door te worteltrekken krijg je de standaard deviatie
    std_dev = math.sqrt(variance)
    return std_dev

standaard_afwijking = calculate_std_dev(gemiddelde, bedragen)

print("De rare bedragen zijn:")

aantal_rare_bedragen = 0
## een loop met weer een paar fouten ;-) Haal de comment weg en maak de loop werkend:
#for transactie in transacties.items():
#if transactie[1][2] > gemiddelde + standaard_afwijking * 2:
#print (transactie)
#aantal_rare_bedragen = aantal_rare_bedragen + 1

assert aantal_rare_bedragen == 4, "Er zijn geen 4 rare bedragen" # dit is een test, als het gemiddelde niet klopt, stopt de code hier

