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
filename = 'classifierLR' #Name of pickle
selectedModel = 'classifier'

# load the data
files = 'CESS-CAST-(A|AA|P)/.*\.tbf\.xml'
corpus = SimpleAncoraCorpusReader(path, files)     
sents = list(corpus.tagged_sents())

# train the model
model_class = models[selectedModel]  

start = time.time()
model = model_class(sents, 'lr')
end = time.time()
print(end - start)
print((end-start)/60)

#sent = 'El gato come pescado .'.split()
#model.tag(sent)

# save it
f = open(filename, 'wb')
pickle.dump(model, f)
f.close()
