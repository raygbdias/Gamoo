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
                with open("db_games.json", 'r') as file:
                    json_file = json.load(file)
                    file.close()
                    #print(json_file)
                if title.text not in json_file: 
                    #print(title.text)
                    url = Request('https://www.gamerpower.com/' + title['href'], headers = {'User-Agent': 'Mozilla/5.0'})
                    #print(url)
                    webpage = urlopen(url)
                    bs = BeautifulSoup(webpage, 'html.parser')
                    dados = bs.findChildren('div', {'class': 'card px-5 px-md-3 px-lg-5 py-4'})[0]
                    for a in dados('a', href=True):
                        print ( 'https://www.gamerpower.com' + a['href'])
                    
                    #print(dados)
                    #url_game = 'https://www.gamerpower.com/' + title['href']
                    title = title.text
                    print(title)
                    #print(url_game)
                    print(price)
                    print('Gamoo has just found a free game for you :)')
                    #self.games [title] = [url_game, price ] 
                    db = open("db_games.json", 'w')
                    json.dump(self.games, db, indent=2)
                    db.close()
        if  len(self.games) == 0:
            return "there is no new free games, check the chat history"
        else:
            #return self.games.keys(), self.games.values()
            #return str(self.games).replace('{', '').replace('}', '').replace(']', '\n').replace('[','\n').replace('\'', '')
            return "**teste**\n" + "https://www.gamerpower.com//daemon-x-machina-prototype-arsenal-set-dlc"
Gamoo().game()