# vraag de gebruiker om een getal in te voeren
# als het getal kleiner is dan 10, print dan "kleiner dan 10"
# als het getal groter is dan 10, print dan "groter dan 10"
# als het getal gelijk is aan 10, print dan "gelijk aan 10"

# vraag de gebruiker om een getal in te voeren
getal = int(input("Voer een getal in: "))

# als het getal kleiner is dan 10, print dan "kleiner dan 10"
if getal < 10:
    print("kleiner dan 10")

# als het getal groter is dan 10, print dan "groter dan 10"
if getal > 10:
    print("groter dan 10")

# als het getal gelijk is aan 10, print dan "gelijk aan 10"
if getal == 10:
    print("gelijk aan 10")

    ## A function that returns the BMI category, given heught and weight
def get_bmi_category(height, weight):
