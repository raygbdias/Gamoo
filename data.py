from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json

url = Request("https://www.gamerpower.com/giveaways/pc", headers = {'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(url).read()
bs = BeautifulSoup(webpage, 'html.parser')
#print(webpage)
dados = bs.find_all('main')
#print(dados) ('h1', {'class':'offer-title text-truncate mb-1'})
#print(dados)
for i in dados:
    nomes = i.findChildren("a", {'class':'card-title'})[0]
    title = nomes.text
    print(title)

    dados = i.findChildren('div', {'class':'thumbnail'})
    link = dados[0].findChildren("a")
    url_game = 'https://www.gamerpower.com/' + link[0]["href"]
    print(url_game)

    preco = i.findChildren('div',{'class':'p-3'})[0]
    #print(preco)
    for item in preco('span', {'class': 'text-muted'}):
        print(item.text)
    #price = preco
        


    """url = Request('https://www.gamerpower.com/'+ link[0]["href"], headers = {'User-Agent': 'Mozilla/5.0'})
    bs = BeautifulSoup(webpage, 'html.parser')
    data = bs.find('meta', {'property':'og:title'})
    '''loader = json.loads(data)
    print (data)
    pretty = json.dumps(loader,indent=4)'''
    #name = data[0].findChildren('title')
    print(data.attrs['content'])
    """
