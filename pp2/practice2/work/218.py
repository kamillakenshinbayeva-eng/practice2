n = int(input())
strings = [input().strip() for _ in range(n)]

first_index = {}

for i, s in enumerate(strings, start=1):
    if s not in first_index:
        first_index[s] = i

for s in sorted(first_index):
    print(s, first_index[s])
