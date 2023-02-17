import requests
import time

def load_time(url):
    start = time.time()
    link = requests.get(url)
    end = time.time()
    time_taken = end - start
    return time_taken

google = "https://www.google.com/"
ynet = "https://www.ynet.co.il/home/0,7340,L-8,00.html"
imdb = "https://www.imdb.com/"

print(load_time(google))
print(load_time(ynet))
print(load_time(imdb))
