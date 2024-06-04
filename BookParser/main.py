import requests
from bs4 import BeautifulSoup
from IO.FileIO import Writer

def CheckPage(link):
    print(link)
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")
    book = []
    book.append(''.join(filter(str.isdigit, soup.find('span', itemprop='isbn').text.strip())))
    book.append(soup.find('h1', itemprop='name').text.strip())
    book.append(soup.find('a', itemprop='author').text.strip())
    book.append(soup.find('a', itemprop='publisher').text.strip())
    book.append(soup.find('span', itemprop='datePublished').text.strip())
    book.append(soup.find_all('a', class_='breadcrumbs__link')[-1].text.strip())
    book.append(soup.find('span', itemprop='numberOfPages').text.strip())
    book.append('100')
    book.append(soup.find('span', itemprop='price')['content'].strip())
    return book


def FindIn(page, query):
    block = page.findAll('a', class_='product-card__title')
    ls = []
    i = 0
    for data in block:
        #ls.append(data['href'])
        try: ls.append(CheckPage('https://www.chitai-gorod.ru{0}'.format(data['href'])))
        except: continue
    return ls

def GetLinks(cnt):
    fulllist = []
    for i in range(1, cnt):
        url = 'https://www.chitai-gorod.ru/catalog/books-18030?page={0}&filters%5Bcategories%5D=18030&filters%5BonlyAvailable%5D=1'.format(i)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        fulllist += FindIn(soup,'product-card__title')
        print("Выполнено {0}%".format(i/cnt*100))

    return fulllist

Writer.WriteMatrix('links.txt', GetLinks(50), sep=';')
#Writer.WriteVector('links.txt', CheckPage("https://www.chitai-gorod.ru/product/blagoslovenie-nebozhiteley-tom-5-2996776?productShelf=&shelfIndex=0&productIndex=0"), sep='\n')