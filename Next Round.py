N,K = map(int,input().split())
l = list(map(int,input().split()))
temp = l[K-1]
count=0
for i in l:
  if i >= temp and i>0:
      count+=1

print(count)
