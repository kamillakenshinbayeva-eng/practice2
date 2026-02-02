n = int(input())
a = list(map(int, input().split()))

minimum = min(a)
maximum = max(a)

for i in range(n):
    if a[i] == maximum:
        a[i] = minimum

print(*a)
