def word_count(text):
    words = text.split()
    total_words = len(words)
    print("The number of words are: ", total_words)

def file_count(filename):
        try:
            with open(filename, 'r') as file_object:

                content = file_object.read()
                word_count(content)
        
        except FileNotFoundError:
            print("Write the correct name of file.")

while True:
    user = input("Press 1 to enter text manually, Press 2 to read a text file, or Press 'q' to exit: ")
    if user == '1':
        text = input("Paste your text here: ")
        word_count(text)
    elif user == '2':
        filename = input("Write the name of file here: ")
        file_count(filename)
    elif user == 'q':
        print("Bye! Have a good day!")
        break
    else:
        print("Invalid input! Choose from given options")