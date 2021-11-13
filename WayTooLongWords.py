n = int(input())

words = []

for word in range(n):
    words.append(input())

for i in range(n):
    if len(words[i]) > 10:
        temp = words[i]

        words[i] = temp[0] + str(len(temp) - 2) + temp[-1]
    print(words[i])
