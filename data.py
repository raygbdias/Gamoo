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
        self.url_game = ""

    def search_game(self):
        for i in self.dados:
            #print(i)
            price = i.findChildren('span', {'class': 'text-muted'})[0].text
            #print(price)
            fprice = price.replace('$', '')
            valor = float(fprice)
            if valor > 0.1:
                title = i.findChildren("a", {'class':'card-title'})[0]
                try:
                    memory = open("db_games.json", 'r')
                    #memory.close()
                    
                    #print(json_file)
                except FileNotFoundError:
                    memory = open("db_games.json", 'w')
                    memory.write('{"nome jogo": ["", ""]}')
                    memory.close()
                        
                    memory = open("db_games.json", 'r')
                json_file = json.load(memory)
                #memory.close()
                #print(json_file)

                url = Request('https://www.gamerpower.com/' + title['href'], headers = {'User-Agent': 'Mozilla/5.0'})
                #print(url)
                webpage = urlopen(url)
                bs = BeautifulSoup(webpage, 'html.parser')
                dados = bs.findChildren('div', {'class': 'card px-5 px-md-3 px-lg-5 py-4'})[0]
                if title.text not in json_file: 
                    #print(title.text)
                    for a in dados('a', href=True):
                        self.url_game = 'https://www.gamerpower.com' + a['href']
                        #print(dados)
                        #self.url_game = 'https://www.gamerpower.com/' + title['href']
                        title = title.text
                        print(title)
                        print(self.url_game)
                        #print(price)
                        print('Gamoo has just found a free game for you :)')
                        if self.url_game not in json_file and title not in json_file and price not in json_file:
                            self.games [title] = [self.url_game, price] 
                        memory = open("db_games.json", 'r+', encoding="utf8")
                        json_file.update(self.games)
                        memory.seek(0)
                        json.dump(json_file, memory, indent=2, ensure_ascii=False)
                        memory.close()
                        if self.url_game:
                            return self.url_game
                        else:
                            return "There is no more free games, come back tomorrow"

                #else:
                #    return "There is no more free games, come back tomorrow"
                #    memory = open("db_games.json", 'w')
                #    json.dump(self.games, memory, indent=2)
                #    memory.close()
                #    for a in dados('a', href=True):
                #        self.url_game = 'https://www.gamerpower.com' + a['href']
                #    return self.url_game
    
        #yield url_game
            
        #def publish_game():
        #    memory = open("db_games.json", 'r')
        #    json_file = json.load(memory)
        #    #memory.close()
        #    if  len(json_file) == 0:
        #        return "there is no new free games, check the chat history"
        #    else:
        #        #return self.games.keys(), self.games.values()
        #        #return str(self.games).replace('{', '').replace('}', '').replace(']', '\n').replace('[','\n').replace('\'', '')
        #        def loop():
        #            for game, details in json_file.items():
        #                yield game, details[0], details[1]
        #                print(game, details[0], details[1])
        #        def inception():
        #            for v,k in loop():
        #                yield v, k
        #        
        #        yield inception()
        #            #return "**test**\n" + "https://www.gamerpower.com/open/free-copperbell-on-pc"
        ##print(f"{json_file['Slapshot Rebound In-Game Currency Key ($5 Value)'][0]}")
        #return publish_game()
                    
#print (Gamoo().search_game())