from sklearn.pipeline import Pipeline
from sklearn.feature_extraction import DictVectorizer
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression

classifiers = {
    'lr': LogisticRegression,
    'svm': LinearSVC,
    'mnb': MultinomialNB,
}

def feature_dict(sent, i):
    feat_dict = {}
    
    features = {
        "w": str.lower,
        "wu": str.isupper,
        "wt": str.istitle,
        "wd": str.isdigit,
    }
    
    #Current word, previous, next (add sentence start/finish as makers)
    words = {'currentW': sent[i]}
    if i == 0:
        words['prevW'] = '<s>'
    else:
        words['prevW'] = sent[i - 1]
    if i == len(sent) - 1:
        words['nextW'] = '</s>'
    else:
        words['nextW'] = sent[i + 1]
    
    # Extract features
    for key, value in words.items():
        if value == '<s>':
            feat_dict['pw'] = value.lower()
        elif value == '</s>':
            feat_dict['nw'] = value.lower()
        else:
            for name, feature in features.items():
                feat_dict[key.lstrip()+'_'+name] = feature(value)
    
    #Termina en s?
    feat_dict["endS"] = sent[i][-1] == 's'
                
    return feat_dict

class ClassifierTagger:
    """Simple and fast classifier based tagger.
    """

    def __init__(self, tagged_sents, clf='lr'):
        """
        clf -- classifying model, one of 'svm', 'lr' (default: 'lr').
        """
        self.pipeline = Pipeline(
                steps=[
                    ('vect', DictVectorizer(sparse=True)),
                    ('clf', classifiers[clf]())
                 ])

        self.fit(tagged_sents)

    def fit(self, tagged_sents):
        """
        Train.
        tagged_sents -- list of sentences, each one being a list of pairs.
        """
        print('Extracting features V2')
        self.getXY(tagged_sents)
        print('')
        print('Executing pipeline')
        self.pipeline.fit(self.X, self.y)

    def getXY(self, tagged_sents):
        X, y = [], []
        words = set()     
      
        for tagged_sent in tagged_sents:
            
            if not tagged_sents:
                continue
            if len(tagged_sent) == 0:
                continue
            
            sent_words, sent_tags = zip(*tagged_sent)
            y.extend(sent_tags)
            words.update(sent_words)
            
            for i in range(len(sent_words)):    
                X.append(feature_dict(sent_words, i))

        self.X, self.y, self.words = X, y, words

    def tag_sents(self, sents):
        """Tag sentences.
        sent -- the sentences.
        """
        return [self.tag(sent) for sent in sents]

    def tag(self, sent):
        """Tag a sentence.
        sent -- the sentence.
        """
        return [self.pipeline.predict(
                    [feature_dict(sent, i)for i in range(len(sent))] )][0]

    def unknown(self, w):
        """Check if a word is unknown for the model.
        w -- the word.
        """
        return not(w in self.words)