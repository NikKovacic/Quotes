from urllib2 import urlopen

from BeautifulSoup import BeautifulSoup

url = "http://quotes.yourdictionary.com/theme/motivational/"
topic_url = urlopen(url)
topic_html = topic_url.read()

topic_soup = BeautifulSoup(topic_html)
quotes = topic_soup.findAll("p", attrs={"class": "quoteContent"})

for quote in quotes:
    print quote.text
