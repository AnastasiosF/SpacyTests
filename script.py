import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion. Hello world. Http")
for token in doc:
    print(token.text, token.pos_, token.dep_)
print("--------------------------------")
for token in doc:
    print("Text:{0}\tidx:{1}\tlemma_:{2}\tis_punct:{3}\tis_space:{4}\tshape_:{5}\tpos_:{6}\ttag_:{7}".format(
        token.text,
        token.idx,
        token.lemma_,
        token.is_punct,
        token.is_space,
        token.shape_,
        token.pos_,
        token.tag_
    ))
print("--------------------------------")
for sent in doc.sents:
    print(sent)

print("--------------------------------")

displacy.serve(doc, style='dep',host='localhost')
