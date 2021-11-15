n = int(input())
cou = 0
for i in range(n):
    a, b, c = map(int, input().split())
    if a + b + c >= 2:
      cou += 1
print(cou)
