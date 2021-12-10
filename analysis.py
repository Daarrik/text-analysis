import matplotlib.pyplot as plt
from string import ascii_letters
from collections import Counter
from math import log10
from scipy.optimize import curve_fit

def get_word_list():
  text = open('p_tags.txt', 'r', encoding='utf-8').read()
  lines = text.split('\n')  # necessary for splitting words at beginning and end of new lines
  transformed_text = ''
  for line in lines:
    transformed_text += ''.join(c for c in line if c in ascii_letters+' ').lower()
    transformed_text += ' '
  
  words = transformed_text.split()
  return words

def zipf(most_common_words: Counter):
  rank = [log10(x) for x in range(1, len(most_common_words)+1)]
  freq = [log10(word[1]) for word in most_common_words]
  plt.plot(rank, freq)

  # Rough Zipf's law reference plot
  zipf_rank = [log10(1), log10(len(most_common_words)-1)]
  zipf_freq = [log10(most_common_words[0][1]), log10(most_common_words[-1][1])]
  plt.plot(zipf_rank, zipf_freq, color='gray', alpha=0.4)

  plt.legend(['Zipf\'s law from Web Crawl', 'Expected line'])
  plt.show()

def heap(word_list: list):
  sub_docs = [word_list[0:x] for x in range(0, len(word_list))]
  sub_doc_lengths = [len(sub_doc) for sub_doc in sub_docs]
  num_unique_words = [len(set(unique_words)) for unique_words in sub_docs]

  plt.plot(sub_doc_lengths, num_unique_words)

  # Rough Heap's law reference plot
  params = curve_fit(lambda n, k, b: k * (n ** b), sub_doc_lengths, num_unique_words)
  k, b = params[0]
  plt.plot(sub_doc_lengths, k * (sub_doc_lengths ** b), color='gray', alpha=0.4)

  plt.legend(['Heap\'s law from Web Crawl', 'Expected curve'])
  plt.show()
  

def main():
  # Web crawl plot
  word_list = get_word_list()
  most_common_words = Counter(word_list).most_common()
  zipf(most_common_words)
  heap(word_list)
  

if __name__ == '__main__':
  main()