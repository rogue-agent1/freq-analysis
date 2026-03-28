#!/usr/bin/env python3
"""freq_analysis - Character and word frequency analysis."""
import sys, collections, re

def analyze(text, mode='words', top=20):
    if mode == 'chars':
        counts = collections.Counter(text)
    elif mode == 'bigrams':
        words = text.lower().split()
        counts = collections.Counter(zip(words, words[1:]))
        counts = {f'{a} {b}': c for (a,b), c in counts.items()}
        counts = collections.Counter(counts)
    else:
        counts = collections.Counter(re.findall(r'\b\w+\b', text.lower()))
    total = sum(counts.values())
    for item, count in counts.most_common(top):
        pct = count / total * 100
        bar = '█' * int(pct * 2)
        print(f"  {count:>6} ({pct:5.1f}%) {bar} {repr(item) if mode=='chars' else item}")
    print(f"\n  Unique: {len(counts)} | Total: {total}")

def main():
    args = sys.argv[1:]
    mode = 'words'
    top = 20
    for a in args:
        if a in ('chars','words','bigrams'): mode = a
        elif a == '--top': pass
        elif a.isdigit(): top = int(a)
    files = [a for a in args if not a.startswith('-') and a not in ('chars','words','bigrams') and not a.isdigit()]
    text = open(files[0]).read() if files else sys.stdin.read()
    analyze(text, mode, top)

if __name__ == '__main__': main()
