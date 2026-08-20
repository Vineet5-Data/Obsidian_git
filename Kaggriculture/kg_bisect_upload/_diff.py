import difflib
a = open('main.py').readlines()
b = open('v97_cap70.py').readlines()
diffs = list(difflib.unified_diff(a, b, fromfile='main.py', tofile='v97_cap70.py', lineterm='', n=2))
for d in diffs:
    print(d)
print(f"\nTotal diff lines: {len(diffs)}")
