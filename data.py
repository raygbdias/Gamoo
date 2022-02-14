from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json

class Gamoo :
    def __init__ (self):
        self.url = Request("https://www.gamerpower.com/giveaways/pc", headers = {'User-Agent': 'Mozilla/5.0'})
        self.webpage = urlopen(self.url).read()
        self.bs = BeautifulSoup(self.webpage, 'html.parser')
        #print(webpage)
        self.dados = self.bs.find_all("div", {'class':'p-3'})
        #print(dados) ('h1', {'class':'offer-title text-truncate mb-1'})
        #print(dados)
        #nomes = dados.find_all("a", {'class':'card-title'})

        self.games = {}

    def game(self):
        for i in self.dados:
            #print(i)
            price = i.findChildren('span', {'class': 'text-muted'})[0].text
            #print(price)
            fprice = price.replace('$', '')
            valor = float(fprice)
            if valor > 0.1:
                title = i.findChildren("a", {'class':'card-title'})[0]
                try: 
                    db = open("db_games.json", 'r')
                        #print(json_file)

                except FileNotFoundError:
                    db = open("db_games.json", 'w')
                    db.write('[]')
                    db = open("db_games.json", 'r')
                    db.close()
                json_file = json.load(db)
                db.close()
                if title.text not in json_file: 
                    #print(title.text) 
                    url = Request('https://www.gamerpower.com/' + title['href'], headers = {'User-Agent': 'Mozilla/5.0'})
                    print(url)
                    webpage = urlopen(url)
                    bs = BeautifulSoup(webpage, 'html.parser')
                    dados = bs.find_all('div', {'class': 'card px-5 px-md-3 px-lg-5 py-4'})
                    print(dados)
                    url_game ='s'


                    title = title.text
                    #print(title)
                    #print(url_game)
                    #print(price)
                    #print('Gamoo has just found a free game for you :)')
                    self.games [title] = [url_game, price ] 
                    json.dump(self.games, db, indent=2)
                    db.close()
                        
        if  len(self.games) == 0:
            return "there is no new free games, check the chat history"
        else:
            #return self.games.keys(), self.games.values()
            #return str(self.games).replace('{', '').replace('}', '').replace(']', '\n').replace('[','\n').replace('\'', '')
            return "**teste**\n" + "https://www.gamerpower.com//daemon-x-machina-prototype-arsenal-set-dlc"

Gamoo().game()
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
        

    
        


    #url = Request('https://www.gamerpower.com/'+ link[0]["href"], headers = {'User-Agent': 'Mozilla/5.0'})
    #bs = BeautifulSoup(webpage, 'html.parser')
    #data = bs.find('meta', {'property':'og:title'})
    #'''loader = json.loads(data)
    #print (data)
    #pretty = json.dumps(loader,indent=4)'''
    ##name = data[0].findChildren('title')
    #print(data.attrs['content'])
    

