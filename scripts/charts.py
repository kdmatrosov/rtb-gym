from random import randint
import matplotlib.pylab as plt

acc = []
plt.figure(figsize=(8,4))
for number in range(60 * 24):
    max = 27
    rate = 100
    if number < 500:
        max = 7
        if number > 100 and number < 300:
            max = 5
    else:
        if number < 800:
            max = 10
        max = 15 + randint(-1, 2)
        if number > 1000:
            max = 22
        if number > 1100:
            max = 27
        if number > 1150:
            max = 24
        if number > 1200:
            max = 22
        if number > 1250:
            max = 17
        if number > 1300:
            max = 12
        if number > 1350:
            max = 9

    num = randint(-1 + int(max / 5), max + randint(-4, 5)) if randint(-1 + int(max / 5), rate) != 0 else 0
    acc.append(num)

plt.plot(acc)
plt.ylabel('Клики')
plt.xlabel('Минуты')
plt.show()

plt.figure(figsize=(8,4))
acc2 = []
i = 0
for number in range(0, 24):
    sum = 0
    for j in range(0, 60):
        sum = sum + acc[i]
        i = i + 1
    acc2.append(sum)

plt.plot(acc2)
plt.ylabel('Клики')
plt.xlabel('Часы')
plt.show()