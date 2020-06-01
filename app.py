from flask import Flask, render_template, request, redirect, url_for, session
import random, math, pprint, re

app = Flask(__name__)

def keyFinder(grid, val):  #znajdowanie numeru pola na którym jest dana litera
    for key, value in grid.items():
        if val == value:
            return key
    
    return ""

def openFile():
    #f = open("slowa_scrabble.txt","r", encoding='utf-8')
    f = open("skrocone_baza.txt","r", encoding='utf-8')
    lines = f.read().splitlines()
    return lines

# wylosowac pare linijek i je przeslac dopiero do wyswietlenia
def selectWords():
    
    words = []
    for x in range(random.randint(0,200),400):    # dodać losowość
        words.append(openFile()[x])
    return words



# list list z literami poszczególnych słów

# dict word: list(word)  thisdict["year"] = 2018

def splitWords():
    wordsToSplit = sorted(selectWords(), key=len, reverse=True)
    wordDict = {}
    i = 1
    for x in wordsToSplit:
        wordDict[i] = list(x)
        i = i+1
    return wordDict
    # wyszczególnić 1 słowo bo ono i tak zawsze pójdzie (ok zrobione we flasku)

def mixWords(splitList): # trzeba tak przekazać inaczej losuje 2 osobne listy
    
    # splitlist[1-10] to kolejne slowa (listy liter)
    # jak ktoraś litera 2 słowa w 1 to zaznacz pozycje i od niej co 13 w dół pisać
    match = ''
    start = 2

    for x in splitList[1]:    # szukanie słowa zaczynającego się od litery w 1 położonym
        if x == splitList[start][0]:
            match = x
            break
        start = start+1

    return match
    #roznica o 1 pole gora/dol wynosi 13 przy wyswietlaniu

def insertWords(grid, splitList):  #słownik z planszą i lista słów (w formie listy list)
    licznik = 2 # do skakania po słowach
    match = ""
    kierunek = ""  # V/H vertical/horizontal
    plansza = [x for x in grid.values()] # lista liter znajdujacych sie na planszy

    for x in plansza:  # gdy znajdzie sie w danym słowie sprawdzić te wszystkie warunki (czy sie zmieści pasuje itd.)
        if x in splitList[licznik]:
            if x == splitList[licznik][0]:  #przypadek gdy litera w znalezionym slowie jest jego 1 literą
                if plansza.index(x) < 13 or plansza[plansza.index(x)-13] == "":  #jeśli w 1 rzędzie lub nad tym nic nie ma
                    kierunek = "V"
                    iterator = plansza.index(x)
                    for letter in splitList[licznik]:
                        if not re.match("^[a-z]+$",str(grid[iterator+12])):  #+12 to bo 1 w lewo od +13
                            plansza[iterator] = letter     # trzeba wyszukiwać żeby obok nic nie było bo się zlepiają
                            iterator = iterator+13
                        else:
                            pass

                elif plansza.index(x)+1: #poziomo od 1 litery zaczynając
                    kierunek = "H"   
                    # jak tylko którys nie jest spełniony to wtedy przeskoczyć do kolejnego słowa w liście 
        else: # gdy nie ma zadnej literki w slowie
            licznik += 1
    return plansza   #chyba trzeba bedzie zwracać planszę po prostu ze zmianami





def makeGrid(splitList):
    # grid w formie dictionary
    # trzeba to zamienić żeby mogło korzystać z tego co zwróci funkcja insertWords
    grid = {}
   
    for i in range(169):
        if (i<len(splitList[1])):   # wpisuj 1 slowo w 1 linijkę krzyzowki
            grid[i]=splitList[1][i]
        else:
            grid[i]=i
    return grid

def makeMixedGrid(plansza):
    grid = {}

    for i in range(169):
        grid[i] = plansza[i]

    return grid

@app.route('/')
def index():
    polskieZnaki = "ążłęó"
    words = selectWords()
    data = openFile()[5]
    splitList = splitWords()
    

    grid = makeGrid(splitList)

    found = keyFinder(grid, "a")
    
    match = mixWords(splitList)

    grid = makeMixedGrid(insertWords(grid, splitList))
    #jest = insertWords(grid, splitList)
    return render_template('index.html', data=data,  
    words=words, polskieZnaki=polskieZnaki, 
    grid=grid, 
    splitList=splitList,
    match=match,
    found=found,
    #jest=jest
    )





if __name__ == "__main__":
    app.run(debug=True)
