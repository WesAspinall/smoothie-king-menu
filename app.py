import requests
import bs4
import json

url = 'https://www.smoothieking.com/menu/smoothies'
res = requests.get(url)

menu_list = list()

webpage = res.content

soup = bs4.BeautifulSoup(webpage, "html.parser")

smoothie_titles = soup.select(".smoothies-grid")

for category in smoothie_titles:
    for smoothie in category:
        if type(smoothie) is bs4.element.Tag:
                title = smoothie.attrs['title'].replace('<sup>', '').replace('</sup>', '')
                category =  smoothie.attrs['blend']

                menu_list.append({'title': title, 'category': category})


with open('menu.js', 'w', encoding='utf8') as fout:
    json.dump(menu_list, fout, ensure_ascii=False)