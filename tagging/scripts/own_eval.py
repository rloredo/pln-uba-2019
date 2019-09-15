import pickle
from collections import defaultdict
from tagging.ancora import SimpleAncoraCorpusReader

#For plotting confussion matrix
#import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# load the model
filename = 'baselineTag' #Name of pickle model (main wd)
f = open(filename, 'rb')
model = pickle.load(f)
f.close()  

# load the data
path = 'ancora-3.0.1es' #Path to corpus
files = '3LB-CAST/.*\.tbf\.xml'
corpus = SimpleAncoraCorpusReader(path, files)
sents = list(corpus.tagged_sents())

# tag and evaluate
hits, total = 0, 0
unk_hits, unk_total = 0, 0
error_count = defaultdict(lambda: defaultdict(int))
error_sents = defaultdict(lambda: defaultdict(set))
y_tags = []
pred_tags = []

n = len(sents)

for i, sent in enumerate(sents):
    word_sent, gold_tag_sent = zip(*sent)
    model_tag_sent = model.tag(word_sent)
    assert len(model_tag_sent) == len(gold_tag_sent), i
    
    y_tags.append(gold_tag_sent)
    pred_tags.append(model_tag_sent)
    
    # global score
    hits_sent = [m == g for m, g in zip(model_tag_sent, gold_tag_sent)]
    hits += sum(hits_sent)
    total += len(sent)
    acc = float(hits) / total * 100

    # score over unknown words
    unk_hits_sent = [hs for w, hs in zip(word_sent, hits_sent) if model.unknown(w)]
    unk_hits += sum(unk_hits_sent)
    unk_total += len(unk_hits_sent)
    unk_acc = float(unk_hits) / unk_total * 100

    # score over known words
    if total == unk_total:
        k_acc = 0.0
    else:
        k_acc = float(hits - unk_hits) / (total - unk_total) * 100

    # confusion matrix
    for t1, t2 in zip(model_tag_sent, gold_tag_sent):
        error_count[t2][t1] += 1
        if t2 != t1:
            # save index of the sentence for error analysis
            error_sents[t2][t1].add(i)

    format_str = '{:3.1f}% ({:2.2f}% / {:2.2f}% / {:2.2f}%)'



#Get accuracy
acc = float(hits) / total * 100
if total == unk_total:
    k_acc = 0.0
else:
    k_acc = float(hits - unk_hits) / (total - unk_total) * 100
unk_acc = float(unk_hits) / unk_total * 100

print('')
print('Accuracy: {:2.2f}% / {:2.2f}% / {:2.2f}% (total / known / unk)'.format(acc, k_acc, unk_acc))


# print confusion matrix
print('')

# basic check
assert total == sum(sum(d.values()) for d in error_count.values())

# select most frequent tags
sorted_error_count = sorted(error_count.keys(),
                          key=lambda t: -sum(error_count[t].values()))
entries = sorted_error_count[:10]



#Print table for github markdown
# print table header
print('|g \ m ', end='')
for t in entries:
    print('\t|{}'.format(t), end='')
print('')
print('|:-------:', end='')
for t in entries:
    print('\t|:-----------:'.format(t), end='')
print('')

# print table rows
for t1 in entries:
    print('|**{}**|\t'.format(t1), end='')
    for t2 in entries:
        if error_count[t1][t2] > 0:
            acc = error_count[t1][t2] / total
            print('{:2.2f}|\t'.format(acc * 100), end='')
        else:
            print('-|\t'.format(acc * 100), end='')
    print('')


plt.matshow(confusion_matrix(y_tags, pred_tags))
plt.colorbar()
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.title('Confusion matrix')
