import nltk
from nltk.stem import PorterStemmer
wd_stem= PorterStemmer()
print(wd_stem.stem('eating'))
words = ["program", "programs", "programmer", "programming", "programmers"]
for w in words:
    print(w, " : ", wd_stem.stem(w))
