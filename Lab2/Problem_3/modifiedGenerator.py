"""
Program: generator.py
Author: Ken
Generates and displays sentences using a simple grammar
and vocabulary. Words are chosen at random.

Modified to read vocabulary from external files.
"""

import random

def getWords(filename):
    """
    Reads words from a specified file, converts them to uppercase,
    and returns them as a tuple. Handles potential file errors.
    """
    words = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                
                for word in line.split():
                    words.append(word.upper())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        
        return ()
    
    return tuple(words)


articles = getWords("articles.txt")
nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
prepositions = getWords("prepositions.txt")


def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    
    if not articles or not nouns:
        return ""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    
    if not verbs or not articles or not nouns or not prepositions:
        return ""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    
    if not prepositions or not articles or not nouns:
        return ""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    
    if not articles or not nouns or not verbs or not prepositions:
        print("Could not generate sentences. Please ensure all vocabulary files exist and are not empty.")
        return

    try:
        number = int(input("Enter the number of sentences: "))
        for _ in range(number):
            print(sentence())
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")

# The entry point for program execution
if __name__ == "__main__":
    main()

