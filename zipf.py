import matplotlib.pyplot as plt
from string import ascii_letters
from collections import Counter
from math import log10

def get_word_list():
  text = open('p_tags.txt', 'r', encoding='utf-8').read()
  lines = text.split('\n')  # necessary for splitting words at beginning and end of new lines
  transformed_text = ''
  for line in lines:
    transformed_text += ''.join(c for c in line if c in ascii_letters+' ').lower()
    transformed_text += ' '
  
  words = transformed_text.split()
  return words


def main():
  # Web crawl plot
  most_common_words = Counter(get_word_list()).most_common()
  rank = [log10(x) for x in range(1, len(most_common_words)+1)]
  freq = [log10(word[1]) for word in most_common_words]
  plt.plot(rank, freq)

  # Rough Zipf's Law reference plot
  zipf_rank = [log10(1), log10(len(most_common_words)-1)]
  zipf_freq = [log10(most_common_words[0][1]), log10(most_common_words[-1][1])]
  plt.plot(zipf_rank, zipf_freq, color='gray', alpha=0.4)

  plt.legend(['Zipf\'s Law from Web Crawl', 'Expected line'])
  plt.show()

if __name__ == '__main__':
  main()