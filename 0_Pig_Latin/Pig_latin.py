# Pig latin is a silly made-up language that alters English words. 
# If a word begins with a vowel, the word yay is added to the end of it. 
# If a word begins with a consonant or consonant cluster (like ch or gr), 
# that consonant or consonant cluster is moved to the end of the word and followed by ay.

# Let’s write a pig latin program that will output something like this:

# Enter the English message to translate into pig latin:
# My name is AL SWEIGART and I am 4,000 years old.
# Ymay amenay isyay ALYAY EIGARTSWAY andyay Iyay amyay 4,000 yearsyay oldyay.

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

def pig_latin(message):
    """
    Precondition: message is a string of one or more words.
    Postcondition: returns the Pig Latin translation of message.
    """
    pig_latin = []
    
    for word in message.split():
        prefix_non_letters = ''
        # check first letter not a number
        while len(word) > 0 and not word[0].isalpha():  
            prefix_non_letters += word[0]
            word = word[1:]
        if len(word) == 0:
            pig_latin.append(prefix_non_letters)
            continue
    
        # remove non letters at the end
        suffix_non_letters = ''
        while not word[-1].isalpha():
            suffix_non_letters += word[-1]
            word = word[:-1]
        
        was_upper = word.isupper()
        was_title = word.istitle()

        word = word.lower()

        # check words begginning with constants
        prefix_constants = ''
        while len(word) > 0 and not word[0] in VOWELS:
            prefix_constants += word[0]
            word = word[1:]

        # add ay at the end
        if prefix_constants != '':
            word += prefix_constants + 'ay'
        else:
            word += 'yay'

        # restore UPPERCASE or Title
        if was_upper:
            word = word.upper()
        if was_title:
            word = word.title()
        
        # Add non-letters at prefix and suffix
        pig_latin.append(prefix_non_letters + word + suffix_non_letters)

    return ' '.join(pig_latin)

def main():
    """
    Precondition: message is a string of one or more words.
    Postcondition: returns the Pig Latin translation of message.
    """
    message = input("Enter the English message to translate into pig latin: ")
    print(pig_latin(message))

if __name__ == "__main__":
    main()






