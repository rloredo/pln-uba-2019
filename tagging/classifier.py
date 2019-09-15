from sklearn.pipeline import Pipeline
from sklearn.feature_extraction import DictVectorizer
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from tqdm import tqdm

classifiers = {
    'lr': LogisticRegression,
    'svm': LinearSVC,
    'nbc': MultinomialNB,
}


def feature_dict(sent, i):
    """Feature dictionary for a given sentence and position.

    sent -- the sentence.
    i -- the position.
    """
    # WORK HERE!!
    
    feature_dict = {}  #This is the dictionary that will be returned

    #Features for all words
    features = {'lw': str.lower, 'tw': str.istitle, 'uw': str.isupper, 'wd': str.isdigit}
    
    #Current word
    words = {'current': sent[i][0]}
    
    #Previous word
    if i == 0:
        words['previous'] = ' '
    else:
        words['previous'] = sent[i-1][0]
    
    #Next word
    if i == len(sent)-1:
        words['next'] = ' '
    else:
        words['next'] = sent[i+1][0]
        
    #Apply features. key: current/prev/next _feature  value: value
    for key, value in words.items():
        for name, feature in features.items():
            feature_dict[key.lstrip()+'_'+name] = feature(value)            
    return feature_dict



class ClassifierTagger:
    """Simple and fast classifier based tagger.
    """

    def __init__(self, tagged_sents, clf='lr'):
        """
        clf -- classifying model, one of 'svm', 'nbc', 'lr' (default: 'lr').
        """
        self.word_set = set()
        
        self.pipeline = Pipeline([
            ('vect', DictVectorizer()),
            ('clf', classifiers[clf]()),])

        self.fit(tagged_sents)

    def fit(self, tagged_sents):
        """
        Train.

        tagged_sents -- list of sentences, each one being a list of pairs.
        """
        print('')
        print('extracting features')
        X, y = self.trainSet(tagged_sents)
        print('')
        print('fitting')
        self.pipeline.fit(X, y)

    def tag_sents(self, sents):
        """Tag sentences.

        sent -- the sentences.
        """
        return [self.tag(sent) for sent in sents]

    def tag(self, sent):
        """Tag a sentence.

        sent -- the sentence.
        """
        x = []
        for i in range(len(sent)):
            x.append(feature_dict(sent, i))
            
        tags = list(self.pipeline.predict(x))
        return tags

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        
        return not(w in self.word_set)
        
        
    def trainSet(self, tagged_sent):
        """
            Gets the features (Xs) and correct tag (y)
        
        """
        X = []
        y = []
        word_set = set()
        for sent in tqdm(tagged_sent):
            if not sent:
                continue
            s, t = zip(*sent)
            word_set.update(s)
            for i in range(len(sent)):
                X.append(feature_dict(s, i))
                y.append((t[i]))
        self.word_set = word_set
        return X, y
        
        
        
        
        
        
        
        
