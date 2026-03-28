#!/usr/bin/env python3
"""Frequency analysis — letter, bigram, trigram distribution."""
import sys, collections
ENGLISH_FREQ={"E":12.7,"T":9.1,"A":8.2,"O":7.5,"I":7.0,"N":6.7,"S":6.3,"H":6.1,"R":6.0,"D":4.3,"L":4.0,"C":2.8,"U":2.8,"M":2.4,"W":2.4,"F":2.2,"G":2.0,"Y":2.0,"P":1.9,"B":1.5,"V":1.0,"K":0.8,"J":0.2,"X":0.2,"Q":0.1,"Z":0.1}
def analyze(text):
    text_alpha="".join(c.upper() for c in text if c.isalpha())
    n=len(text_alpha)
    letters=collections.Counter(text_alpha)
    bigrams=collections.Counter(text_alpha[i:i+2] for i in range(n-1))
    trigrams=collections.Counter(text_alpha[i:i+3] for i in range(n-2))
    return letters, bigrams, trigrams, n
def cli():
    if len(sys.argv)>1 and sys.argv[1]=="--file":
        with open(sys.argv[2]) as f: text=f.read()
    else: text=" ".join(sys.argv[1:]) or "The quick brown fox jumps over the lazy dog multiple times each day"
    letters,bigrams,trigrams,n=analyze(text)
    print(f"  Letter frequencies ({n} chars):")
    for c,count in letters.most_common(10):
        pct=count/n*100; exp=ENGLISH_FREQ.get(c,0)
        bar="█"*int(pct); print(f"    {c}: {pct:5.1f}% {bar} (expected {exp}%)")
    print(f"  Top bigrams: {bigrams.most_common(5)}")
    print(f"  Top trigrams: {trigrams.most_common(5)}")
if __name__=="__main__": cli()
