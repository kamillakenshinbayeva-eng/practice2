n=int(input())

k=list(map(int, input().split()))

count=0

for x in k:

    if x>0:

        count+=1

print(count)
 