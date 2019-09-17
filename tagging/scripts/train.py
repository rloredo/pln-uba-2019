"""Train a sequence tagger.

Usage:
  train.py [options] -c <path> -o <file>
  train.py -h | --help

Options:
  -m <model>    Model to use [default: badbase]:
                  badbase: Bad baseline
                  base: Baseline
                  class: Classifier
  -c <path>     Ancora corpus path.
  -t <classifier> If model classifier is selected [default: lr]:
                  lr: logistic regression
                  svm: linear SVC
                  mnb: MultinomialNB
  -o <file>     Output model file.


  -h --help     Show this screen.
"""
from docopt import docopt
import pickle

from tagging.ancora import SimpleAncoraCorpusReader
from tagging.baseline import BaselineTagger, BadBaselineTagger
from tagging.classifier import *
import time


models = {
    'badbase': BadBaselineTagger,
    'base': BaselineTagger,
    'class': ClassifierTagger,
}

classifiers = {
    'lr': 'lr',
    'svm': 'svm',
    'mnb': 'mnb',
}



if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the data
    files = 'CESS-CAST-(A|AA|P)/.*\.tbf\.xml'
    corpus = SimpleAncoraCorpusReader(opts['-c'], files)
    sents = corpus.tagged_sents()

    model_class = models[opts['-m']]

    # train the models

    #If classifier train with -t opt
    if opts['-m'] == 'class':
        classToUse = classifiers[opts['-t']]
        print('training classifier with:',classToUse,' model')
        start = time.time()
        sents_list = list(sents)
        model = model_class(sents_list, classToUse)
        end = time.time()
        print('Training time', end - start)

    #Else train baseline or base
    else:
        start = time.time()
        model = model_class(sents)
        end = time.time()
        print('Training time', end - start)

    # save it
    print('Saving...')
    filename = opts['-o']
    f = open(filename, 'wb')
    pickle.dump(model, f)
    f.close()
    print('All done!')
