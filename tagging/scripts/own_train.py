import pickle

from tagging.ancora import SimpleAncoraCorpusReader
from tagging.baseline import BaselineTagger, BadBaselineTagger


models = {
    'badbase': BadBaselineTagger,
    'base': BaselineTagger,
}

path = 'ancora-3.0.1es' #Path to corpus
filename = 'baselineTag'

# load the data
files = 'CESS-CAST-(A|AA|P)/.*\.tbf\.xml'
corpus = SimpleAncoraCorpusReader(path, files)     
sents = corpus.tagged_sents()

# train the model
model_class = models['base']  
model = model_class(sents)

# save it
f = open(filename, 'wb')
pickle.dump(model, f)
f.close()
