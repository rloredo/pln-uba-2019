"""Train a sequence tagger.

Usage:
  train.py [options] -c <path> -m <model> -v <version> -t <classifier> -o <file>
  train.py -h | --help

Options:

  -c <path>     Ancora corpus path.
  
  -m <model>    Model to use [default: badbase]:
                  badbase: Bad baseline
                  base: Baseline
                  classifier: Classifier

  -v <version>   version of classifier to use [default: v1]
                  1: Only base features
                  2: added ending in -s
                  3: added ending in -mente
                  
  -t <classifier> If model classifier is selected [default: lr]:
                  lr: logistic regression
                  svm: linear SVC
                  mnb: MultinomialNB
                  
  -o <file>     Output model file.


  -h --help     Show this screen.
  
  
  Version 2
"""
from docopt import docopt
import pickle

from tagging.ancora import SimpleAncoraCorpusReader
from tagging.baseline import BaselineTagger, BadBaselineTagger
from tagging.classifierV1 import *
import time


models = {
    'badbase': BadBaselineTagger,
    'base': BaselineTagger,
}


classTypes = {
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
    

    # train the models

    #If classifier train with -t opt
    if opts['-m'] == 'classifier':
        if int(opts['-v']) == 1:
            from tagging.classifierV1 import *
        elif int(opts['-v']) == 2:
            from tagging.classifierV2 import *
        else:
            from tagging.classifierV3 import *
            
        model_class = ClassifierTagger
        classToUse = classTypes[opts['-t']]
        print('training classifier with:',classToUse,' model')
        start = time.time()
        sents_list = list(sents)
        model = model_class(sents_list, classToUse)
        end = time.time()
        print('Training time', end - start)

    #Else train baseline or base
    else:
        model_class = models[opts['-m']]
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
