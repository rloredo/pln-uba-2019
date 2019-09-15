from collections import defaultdict

class BadBaselineTagger:

    def __init__(self, tagged_sents, default_tag='nc0s000'):
        """
        tagged_sents -- training sentences, each one being a list of pairs.
        default_tag -- tag for all words.
        """
        self._default_tag = default_tag

    def tag(self, sent):
        """Tag a sentence.

        sent -- the sentence.
        """
        return [self.tag_word(w) for w in sent]

    def tag_word(self, w):
        """Tag a word.

        w -- the word.
        """
        return self._default_tag

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        return True


class BaselineTagger:

    def __init__(self, tagged_sents, default_tag='nc0s000'):
        """
        tagged_sents -- training sentences, each one being a list of pairs.
        default_tag -- tag for unknown words.
        """
        
        self.default_tag = default_tag
        
        self.word_tags = defaultdict(lambda: defaultdict(int))
        
        for sent in list(tagged_sents):
            for word, tag in sent:
                self.word_tags[word][tag] += 1

        self.word_tags = dict(self.word_tags)

    def tag(self, sent):
        """Tag a sentence.

        sent -- the sentence.
        """
        return [self.tag_word(w) for w in sent]

    def tag_word(self, w):
        """Tag a word.

        w -- the word.
        """ 
        if self.unknown(w):
            return self.default_tag
        else:
           return max(self.word_tags[w], key=self.word_tags[w].get)
           

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        if w in self.word_tags:
            return False
        else:
            return True


