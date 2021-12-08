import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from googletrans import Translator

# Defining global variables
translator = Translator()
text_file = open('p_tags.txt', 'a', encoding='utf-8')
all_links = set()

def check_language(url):
  translator.detect()

def get_outlinks(links, url):
  outlinks = set()
  for link in links:
    try:
      outlink = urljoin(url, link['href'])
      check_language()
      outlinks.add(urljoin(url, link['href']))
    except:
      print('Error joining URL')
  return outlinks

def crawl(url):
  try:
    req = requests.get(url)
  except:
    print(f'An error occured trying to crawl {url}')
    crawl(all_links.pop(0))

  soup = BeautifulSoup(req.text, 'html.parser')
  p_tags = soup('p')
  for p in soup('p'):
    text_file.write(p.getText())
  outlinks = get_outlinks(soup('a'), url)
  
  
def main():
  seed = 'https://en.wikipedia.org/wiki/Yugoslav_gunboat_Beli_Orao'
  crawl(seed)

if __name__ == '__main__':
  main()