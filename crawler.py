import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
# might have to do "pip install googletrans==3.1.0a0"
# "if pip install googletrans" doesn't work
from googletrans import Translator

# Defining global variables
translator = Translator()
text_file = open('p_tags.txt', 'a', encoding='utf-8')
links_to_crawl = []
crawled_links = []

def crawl_next_link(remove_last: bool):
  if remove_last: crawled_links.pop()
  new_url = links_to_crawl.pop(0)
  crawled_links.append(new_url)
  crawl(new_url)

def get_outlinks(links, url):
  outlinks = set()
  for link in links:
    try:
      outlinks.add(urljoin(url, link['href']))
    except:
      print('Error joining URL')
  return outlinks

def crawl(url):
  try:
    req = requests.get(url)
  except:
    print(f'An error occured trying to crawl {url}')

  soup = BeautifulSoup(req.text, 'html.parser')
  p_tags = soup('p')
  try:  # crawl next link if language isn't english or can't detect language
    if translator.detect(p_tags[0].get_text()).lang != 'en':
      crawl_next_link(remove_last=True)
  except:
      crawl_next_link(remove_last=True)

  for p in p_tags:
    text_file.write(p.get_text())

  outlinks = get_outlinks(soup('a', limit=10), url)
  # LOL
  links_to_crawl.extend(
    [outlink for outlink in outlinks if outlink not in links_to_crawl and outlink not in crawled_links]
  )
  if len(crawled_links) < 10: # max number of links to get p tags from
    crawl_next_link(remove_last=False)

def main():
  seed = 'https://en.wikipedia.org/'
  crawl(seed)

if __name__ == '__main__':
  main()