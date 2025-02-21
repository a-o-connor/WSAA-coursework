import requests 
import statistics

def readbooks(url):
    response = requests.get(url)
    return response.json()


def readbookid(url, id):
    get_url = url + "/" + str(id)
    response = requests.get(get_url)
    return response.json()


def createbook(url, book):
    response = requests.post(url, json = book)
    return response.json()

def updatebook(url, book, id):
    puturl = url + "/" + str(id)
    response = requests.put(puturl, json = book)
    return response.json()

def deletebook(url, id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()

def extract_mean_price(url):
    response = requests.get(url)
    books = response.json()
    prices = [book['price'] for book in books]
    mean_price = statistics.mean(prices)
    return mean_price





