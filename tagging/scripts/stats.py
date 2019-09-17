"""Print corpus statistics.

Usage:
  stats.py -c <path>
  stats.py -h | --help

Options:
  -h --help     Show this screen.
"""
from docopt import docopt
from collections import defaultdict

from tagging.ancora import SimpleAncoraCorpusReader


class POSStats:
    """Several statistics for a POS tagged corpus.
    """

    def __init__(self, tagged_sents):
        """
        tagged_sents 
        -- corpus (list/iterable/generator of tagged sentences)
        """
        #List of tagged sentences
        self.corpus = list(tagged_sents) #Load lazyMap into memory... Takes time but I don't know very well how to work with this ADT
              
        #
        #
        #Create a word dict (keys are words and values are POS tags + n of occurencies)
        self.word_dict = defaultdict(lambda: defaultdict(int))
        #Create a tag dict (keys are tags and values are words + n of occurencies)
        self.tag_dict = defaultdict(lambda: defaultdict(int))
        #Create a tag dict (keys are tags and values n of occurencies)
        self.freq_tag_dict = defaultdict(int)
        #Create a freq dict (keys are words and values are n of occurencies)
        self.freq_word_dict = defaultdict(int)
        #Create token counter
        self.tokenCount = 0
        
        for sent in self.corpus:
                for word, tag in sent:
                   
                    self.word_dict[word][tag] += 1
                    self.tag_dict[tag][word] += 1
                    self.freq_tag_dict[tag] += 1
                    self.freq_word_dict[word] += 1
                    self.tokenCount += 1
                    
        #Convert dicts back to normal dicts            
        self.word_dict = dict(self.word_dict)                   
        self.tag_dict = dict(self.tag_dict)        
        self.freq_word_dict = dict(self.freq_word_dict) 
        self.freq_tag_dict = dict(self.freq_tag_dict) 
   
        
    def sent_count(self):
        """Total number of sentences."""
        return len(self.corpus)

    def token_count(self):
        """Total number of tokens."""
        return self.tokenCount
                
    def words(self):
        """Vocabulary (set of word types)."""
        return list(self.freq_word_dict.keys())

    def word_count(self):
        """Vocabulary size."""
        return len(self.words())

    def word_freq(self, w):
        """Frequency of word w."""                    
#        return self.freq_dict[w] / self.tokenCount
        return self.freq_word_dict[w]

    def unambiguous_words(self):
        """List of words with only one observed POS tag."""
        return [key for key in self.word_dict.keys() if len(self.word_dict[key].keys()) == 1]

    def ambiguous_words(self, n):
        """List of words with n different observed POS tags.

        n -- number of tags.
        """      
        return [key for key in self.word_dict.keys() if len(self.word_dict[key].keys()) == n]
              
    def tags(self):
        """POS Tagset."""
        return list(self.freq_tag_dict.keys())

    def tag_count(self):
        """POS tagset size."""
        return len(self.tags())

    def tag_freq(self, t):
        """Frequency of tag t."""                   
#        return self.tag_dict[t] / self.tokenCount  
        return self.freq_tag_dict[t]

    def tag_word_dict(self, t):
        """Dictionary of words and their counts for tag t."""         
        return dict(self.tag_dict[t])

#Esto corre el programa
if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the data
    corpus = SimpleAncoraCorpusReader(opts['-c']) 
    sents = corpus.tagged_sents()

    # compute the statistics
    stats = POSStats(sents)

    print('Basic Statistics')
    print('================')
    print('sents: {}'.format(stats.sent_count()))
    token_count = stats.token_count()
    print('tokens: {}'.format(token_count))
    word_count = stats.word_count()
    print('words: {}'.format(word_count))
    print('tags: {}'.format(stats.tag_count()))
    print('')
    print('Example of word frequency')
    print('================')
    print('Frequency of "presidente": {}'.format(stats.word_freq('presidente')))
    print('')
    print('Example of tag frequency')
    print('================')
    print('Frequency of "nc0s000": {}'.format(stats.tag_freq('nc0s000')))
    print('')
    print('Most Frequent POS Tags')
    print('======================')
    tags = [(t, stats.tag_freq(t)) for t in stats.tags()]
    sorted_tags = sorted(tags, key=lambda t_f: -t_f[1])
    print('tag\tfreq\t%\ttop')
    for t, f in sorted_tags[:10]:
        words = stats.tag_word_dict(t).items()
        sorted_words = sorted(words, key=lambda w_f: -w_f[1])
        top = [w for w, _ in sorted_words[:5]]
        print('{0}\t{1}\t{2:2.2f}\t({3})'.format(t, f, f * 100 / token_count, ', '.join(top)))
    print('')
    print('Word Ambiguity Levels')
    print('=====================')    
    print('n\twords\t%\ttop')
    for n in range(1, 10):
        words = stats.ambiguous_words(n)
        m = len(words)
        
        # most frequent words:
        sorted_words = sorted(words, key=lambda w: -stats.word_freq(w))
        top = sorted_words[:5]
        print('{0}\t{1}\t{2:2.2f}\t({3})'.format(n, m, m * 100 / word_count, ', '.join(top)))
