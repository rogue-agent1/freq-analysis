import argparse, sys, collections, string

def analyze(text, case_sensitive=False):
    if not case_sensitive: text = text.upper()
    total = sum(1 for c in text if c.isalpha())
    freq = collections.Counter(c for c in text if c.isalpha())
    return {c: (count, count/total*100 if total else 0) for c, count in freq.most_common()}

ENGLISH_FREQ = {"E":12.7,"T":9.1,"A":8.2,"O":7.5,"I":7.0,"N":6.7,"S":6.3,"H":6.1,"R":6.0,"D":4.3,"L":4.0,"C":2.8,"U":2.8,"M":2.4,"W":2.4,"F":2.2,"G":2.0,"Y":2.0,"P":1.9,"B":1.5,"V":1.0,"K":0.8,"J":0.15,"X":0.15,"Q":0.10,"Z":0.07}

def main():
    p = argparse.ArgumentParser(description="Frequency analysis")
    p.add_argument("file", nargs="?")
    p.add_argument("-t", "--text")
    p.add_argument("--bar-width", type=int, default=40)
    p.add_argument("--compare", action="store_true", help="Compare with English")
    args = p.parse_args()
    if args.text: text = args.text
    elif args.file: text = open(args.file).read()
    else: text = sys.stdin.read()
    freq = analyze(text)
    max_pct = max(pct for _, pct in freq.values()) if freq else 1
    print(f"Total letters: {sum(c for c, _ in freq.values())}")
    print(f"{'Char':>4} {'Count':>6} {'%':>6} {'Bar'}")
    for char, (count, pct) in sorted(freq.items(), key=lambda x: -x[1][1]):
        bar = "█" * int(pct / max_pct * args.bar_width)
        eng = f" (eng: {ENGLISH_FREQ.get(char, 0):.1f}%)" if args.compare else ""
        print(f"   {char} {count:6d} {pct:5.1f}% {bar}{eng}")

if __name__ == "__main__":
    main()
