
atleast_six_Letter_Words = []

with open('about.txt') as fin:

    for line in fin.readlines():

        for word in line.split(" "):

            if len(word) >= 6:

                atleast_six_Letter_Words.append(word)
file = open("about.txt", "r")
frequent_word = ""
frequency = 0
words = []

for line in file:

    line_word = line.lower().replace(',', '').replace('.', '').split(" ")

    for w in line_word:
        words.append(w)

for i in range(0, len(words)):


    count = 1

    for j in range(i + 1, len(words)):
        if words[i] == words[j]:
            count = count + 1

    if count > frequency:
        frequency = count
        frequent_word = words[i]

print(atleast_six_Letter_Words)
print("Most repeated word: " + frequent_word)
print("Frequency: " + str(frequency))
file.close()
