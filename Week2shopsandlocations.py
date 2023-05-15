import random

# List of existing Dutch shop names and cities for demonstration purposes
existing_shop_names = ['Albert Heijn', 'Kruidvat', 'Jumbo', 'Hema', 'Gall & Gall']
existing_cities = ['Amsterdam', 'Rotterdam', 'Utrecht', 'Den Haag', 'Eindhoven']

shops = {}

# Generate 98 entries with normal size
for i in range(1, 99):
    shop_name = random.choice(existing_shop_names)
    location = random.choice(existing_cities)
    amount = random.randint(100, 10000)
    shops[shop_name] = {
        'location': location,
        'amount': amount
    }

# Add two standout entries
shops['Faude?'] = {
    'location': random.choice(existing_cities),
    'amount': random.randint(10000, 50000)
}
shops['Ook Fraude? '] = {
    'location': random.choice(existing_cities),
    'amount': random.randint(10000, 50000)
}

# Print the dictionary
for shop_name, shop_info in shops.items():
    amount = shop_info['amount']
    print(f"{shop_name}: {shop_info}")

### Kun je de fraudegevallen vinden?
## en wat als de bedragen veranderen?

