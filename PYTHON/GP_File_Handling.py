file = open("my_file.txt", 'r')
content = file.read()
words = content.split()
length_word = int(input("Enter word length: "))
matching_words = []

for word in words:
    #We strip the punctuation here to get the true length
    clean_word = word.strip('[]{}.,()')

    if len(clean_word) == length_word:
        #Appending clean_word ensure the period isn't there when printing
        matching_words.append(clean_word)

if len(matching_words) == 0:
    print("No word found")
else:
    for i in matching_words:
        print(i)    
