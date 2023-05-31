from bs4 import BeautifulSoup
from collections import Counter
import re

# de tekst van de website wordt opgehaald
def get_webpage_text(url):
    # response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text(separator=' ')
    return text

# alle tekst wordt in kleine letters gezet
def normalize_text(text):
    return text.lower()

# de tekst wordt opgesplitst in losse woorden
def split_into_words(text):
    text = re.sub(r'\W+', ' ', text)
    text.split()

# de woorden worden geteld. Counter is een python module die dit voor je doet en is een onderdeel van dict.
def count_words(words):
    return Counter(words)

def calculate_word_frequency(url):
    text = get_webpage_text(url)
    normalized_text = normalize_text(text)
    words = split_into_words(normalized_text)
    word_count = count_words(words)
    return word_count

urls = ['http://books.toscrape.com/catalogue/category/books/science_22/index.html',
        'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html',
        ]

for url in urls:
    print(f"Word frequencies for {url}:\n", calculate_word_frequency(url))
