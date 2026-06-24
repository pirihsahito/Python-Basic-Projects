import random
import string
str = input("Enter your message: ")
words = str.split(" ")
choice = input("1 for Coding or 0 for Decoding: ")
coding = True if(choice == "1") else False
print(choice)

if(coding):
    newWords = []
    for word in words:
        if(len(word) >= 3):
            r1 = "".join(random.choices(string.ascii_lowercase, k=3))
            r2 = "".join(random.choices(string.ascii_lowercase, k=3))
            strnew = r1 + word[1:] + word[0] + r2
            newWords.append(strnew)
        else:
            newWords.append(word[:: -1])

    print(f"Coded message: {" ".join(newWords)}")

else:
    newWords = []
    for word in words:
        if (len(word) >= 3):
            strnew = word[3:-3]
            strnew = strnew[-1] + strnew[:-1]
            newWords.append(strnew)
        else:
            newWords.append(word[::-1])
    print(f"Decoded message: {" ".join(newWords)}")