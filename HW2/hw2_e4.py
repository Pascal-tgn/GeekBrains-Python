sentence = input("Please enter a sentence >>> ")
words = (sentence.split())
for i, word in enumerate(words, 1):
    print(i, word[:10])
