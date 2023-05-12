import urllib.request
import re

url = 'https://quke.ru/shop/smartfony/apple?page-size=72'

response = urllib.request.urlopen(url)
html_content = response.read()
pattern = r'<a class="b-card2-v2__name".*?>(.*?)</a>.*?<span class="b-card2-v2__price-val">(\d[\d\s]*)</span>'
matches = re.findall(pattern, str(html_content))

prices = [int(match[1].replace(' ', '')) for match in matches]
max_price = max(prices)
min_price = min(prices)
average_price = sum(prices) / len(prices)
print(f'Самый дорогой смартфон: {matches[prices.index(max_price)][0]}, цена: {max_price} руб.')
print(f'Самый дешевый смартфон: {matches[prices.index(min_price)][0]}, цена: {min_price} руб.')
print(f'Средняя цена смартфонов: {average_price} руб.')

with open('catalog.txt', 'w', encoding='utf-8') as f:
    f.write('Название смартфона | Цена в рублях\n')
    for match in matches:
        f.write(f'{match[0]} | {match[1]}\n')