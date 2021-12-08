import matplotlib.pylab as plt
from string import ascii_letters
from collections import Counter

def get_word_list():
  text = open('p_tags.txt', 'r', encoding='utf-8').read()
  lines = text.split('\n')  # necessary for splitting words at beginning and end of new lines @
  transformed_text = ''
  for line in lines:
    transformed_text += ''.join(c for c in line if c in ascii_letters+' ').lower()
    transformed_text += ' '
  
  words = transformed_text.split()
  return words


def main():
  word_count = Counter(get_word_list())
  print(word_count.most_common(100))

if __name__ == '__main__':
  main()