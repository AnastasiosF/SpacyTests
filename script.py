import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("""
Baltic index falls on weaker capesize, supramax rates
in Dry Bulk Market,International Shipping News 08/02/2020


The Baltic Exchange’s main sea freight index declined on Friday as lower rates for capesize and supramax segments offset gains in the panamax category.

The Baltic index, which tracks rates for capesize, panamax and supramax vessels to ferry dry bulk commodities, dropped 16 points, or 3.7%, to 415.

The main index has lost nearly 14.8% this week, its ninth consecutive week of decline.

The capesize index fell 47 points to a negative 234, down for the 41st straight session.

Average daily earnings for capesizes, which typically transport 170,000-180,000 tonne cargoes including iron ore and coal, lost $361 to $2,660.

The panamax index rose 11 points, or 2.1%, to 541.

However, the index has declined over 5.7% this week and registered its third consecutive week of losses.

Average daily earnings for panamaxes, which usually carry coal or grain cargoes of about 60,000 tonnes to 70,000 tonnes, increased $98 to $4,871.

Australian iron ore miners such as Rio Tinto and BHP Group, who are among China’s biggest suppliers, said they were preparing for a tropical cyclone that will hit Australia over the weekend.

Port Hedland, which is the world’s biggest export point for iron ore, and Port of Dampier will be shutting down operations due to the cyclone in Australia.

The supramax index fell 15 points to 491.
Source: Reuters (Reporting by Anjishnu Mondal in Bengaluru; Editing by Krishna Chandra Eluri)
""")
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

displacy.serve(doc, style='ent', host='localhost', page=True)

