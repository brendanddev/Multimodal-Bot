
import spacy
from spacy.matcher import Matcher
from textblob import TextBlob
import random

nlp = spacy.load("en_core_web_md")
matcher = Matcher(nlp.vocab)
