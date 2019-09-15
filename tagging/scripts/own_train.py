import pickle

from tagging.ancora import SimpleAncoraCorpusReader
from tagging.baseline import BaselineTagger, BadBaselineTagger
from tagging.classifier import *
import time

models = {
    'badbase': BadBaselineTagger,
    'base': BaselineTagger,
    'classifier': ClassifierTagger,
}

path = 'ancora-3.0.1es' #Path to corpus
filename = 'classifierNBC' #Name of pickle
selectedModel = 'classifier'

# load the data
files = 'CESS-CAST-(A|AA|P)/.*\.tbf\.xml'
corpus = SimpleAncoraCorpusReader(path, files)     
sents = corpus.tagged_sents()

# train the model
model_class = models[selectedModel]  

start = time.time()
model = model_class(sents, 'nbc')
end = time.time()
print(end - start)
(end-start)/60

# save it
f = open(filename, 'wb')
pickle.dump(model, f)
f.close()
