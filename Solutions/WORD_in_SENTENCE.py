sentence = input()
words = sentence.split()
required_word = input()
presence = 0
notpresence = -1
for word in words:
    if word == required_word:
        presence = presence + 1
if presence == 0:
    print(notpresence)
else:
    print(presence)
