from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json

url = Request("https://www.gamerpower.com/giveaways/pc", headers = {'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(url).read()
bs = BeautifulSoup(webpage, 'html.parser')
#print(webpage)
dados = bs.find_all("div", {'class':'p-3'})
#print(dados) ('h1', {'class':'offer-title text-truncate mb-1'})
#print(dados)
#nomes = dados.find_all("a", {'class':'card-title'})
class gamoo:
    games = {}
    for i in dados:
        #print(i)
        price = i.findChildren('span', {'class': 'text-muted'})[0].text
        #print(price)
        fprice = price.replace('$', '')
        valor = float(fprice)
        if valor > 0.1:
            title = i.findChildren("a", {'class':'card-title'})[0]
            with open("db_games.json", 'r') as file:
                json_file = json.load(file)
                file.close()
                #print(json_file)
            if title.text not in json_file: 
                #print(title.text) 
                url_game = 'https://www.gamerpower.com/' + title['href']
                title = title.text
                print(title)
                print(url_game)
                print(price)
                print('Gamoo has just found a free game for you :)')
                games [title] = [url_game, price ] 
                db = open("db_games.json", 'w')
                json.dump(games, db, indent=2)
                db.close()
            print()



    #dados = i.findChildren('div', {'class':'thumbnail'})
    #link = dados[0].findChildren("a")
    #url_game = 'https://www.gamerpower.com/' + link[0]["href"]

    #preco = bs.find_all('div', {'class': 'p-3'})[0]
    #print(preco.findChildren('span', {'class': 'text-muted'}))
    #for item in preco('span', {'class': 'text-muted'}):
    #    numero = item.text
    #    #print(type(numero))-
    #    number = numero.replace('$', '')
    #    valor = float(number)
    #    #print(valor)
    #    if valor > 0.1:
    #        print('Gamoo has just found a free game for you :)')
        

    
        


    """url = Request('https://www.gamerpower.com/'+ link[0]["href"], headers = {'User-Agent': 'Mozilla/5.0'})
    bs = BeautifulSoup(webpage, 'html.parser')
    data = bs.find('meta', {'property':'og:title'})
    '''loader = json.loads(data)
    print (data)
    pretty = json.dumps(loader,indent=4)'''
    #name = data[0].findChildren('title')
    print(data.attrs['content'])
    """

