# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
from sentence_transformers import SentenceTransformer, util

import pickle
import configparser
config = configparser.ConfigParser()
# config = ConfigParser()

model = SentenceTransformer("stsb-roberta-large")
filename = "roberta.sav"
#model=pickle.load(open(filename, 'rb'))
pickle.dump(model, open(filename, 'wb'))