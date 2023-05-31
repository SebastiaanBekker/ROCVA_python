
#function that returns a random url and page

import random
def random_urls_and_pages(number_of_urls=3):
    url_list = []
    for i in range(number_of_urls):
        sites = ['google', 'facebook', 'twitter', 'linkedin', 'youtube', 'instagram']
        pages = ['home', 'about', 'contact', 'products', 'services']
        extensions = ['.html', '.php', '.asp', '.aspx', '.jsp']
        site = random.choice(sites)
        page = random.choice(pages)
        extension = random.choice(extensions)

        url = "https://www." + site + ".com/" + page + extension
        url_list.append(url)
    return url_list

#random_urls_and_pages(5)

print(random_urls_and_pages())
