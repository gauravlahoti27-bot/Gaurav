filename = input("Enter file name: ")
length = int(input("Enter desired word length: "))

try:
    with open(filename, "r") as file:
        text = file.read()
        import string
        for p in string.punctuation:
            text = text.replace(p, "")

        words = text.split()

        print(f"\nWords with length {length}:\n")
        for word in words:
            if len(word) == length:
                print(word)

except FileNotFoundError:
    print("File not found. Please check file name.")
