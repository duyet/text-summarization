#import logging
#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim.summarization import summarize as summ

def summarize(text, ratio=0.5):
	return summ(text, ratio)

