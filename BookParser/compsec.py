import requests
from bs4 import BeautifulSoup
from IO.FileIO import Writer, Reader


def FindAllBDU(report):
    book = []
    book.clear()
    with open(report, 'r') as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        for bdu in soup.find_all('td', class_='bdu'):
            book.append(bdu.text.strip())
            print(bdu.text)
    return book


Writer.WriteVector('BDUs.txt', FindAllBDU('report.html'), sep='\n')
# bdus = Reader.ReadLine('BDUs.txt', '\n', convert=str)
# cvecwe = []
# for bdu in bdus[:2]:
#     s = FindCVEandCWE(bdu[-10:])
#     print(s)
#     cvecwe.append(s)
# Writer.WriteVector('CVECWE.txt', cvecwe, sep='\n')
#Writer.WriteVector('links.txt', CheckPage("https://www.chitai-gorod.ru/product/blagoslovenie-nebozhiteley-tom-5-2996776?productShelf=&shelfIndex=0&productIndex=0"), sep='\n')