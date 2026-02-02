n = int(input())

counts = {}

for _ in range(n):
    number = input().strip()
    counts[number] = counts.get(number, 0) + 1

answer = 0
for value in counts.values():
    if value == 3:
        answer += 1

print(answer)
