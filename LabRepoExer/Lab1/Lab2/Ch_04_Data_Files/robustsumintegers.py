import os.path
fileName = "integers.txt"
if os.path.exists(fileName):  # Check for missing file
    f = open(fileName, 'r')
    theSum = 0
    invalidInteger = False
    for line in f:
        wordlist = line.split()
        for word in wordlist:
            if word.isdigit():  # Check for valid integer
                number = int(word)
                theSum += number
            else:
                invalidInteger = True
                print("Invalid integer in file: ", word)
                break
    if not invalidInteger:
         print("The sum is", theSum)
else:
    print("The file", fileName, "does not exist")

