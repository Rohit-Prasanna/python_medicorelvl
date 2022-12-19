fin = open('about.txt')
content = fin.read()
words = content.split(" ")

atleast6 = []
for i in words:
    if len(i) > 5:
        atleast6.append(i)

d = {}
for i in words:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] = d[i] + 1

maximum = 0
for i in d.keys():
    if d[i] > maximum:
        maximum = d[i]
        most_frequent = i
print(atleast6)
print("Most frequent word:", most_frequent)
