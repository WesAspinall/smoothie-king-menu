import requests
import bs4

url = 'https://www.smoothieking.com/menu/smoothies'
res = requests.get(url)

webpage = res.content

soup = bs4.BeautifulSoup(webpage, "html.parser")

smoothie_titles = soup.select(".smoothies-grid")

for category in smoothie_titles:
    for smoothie in category:
        if type(smoothie) is bs4.element.Tag:
            print(smoothie.attrs['title']+ ' is in the ' + smoothie.attrs['blend'] + ' category.')