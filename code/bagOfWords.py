import os;

# Creates a bag of words for each file
# Returns the total number of words
def createBOW(path, dict):
    totalWords = 0
    numOfMessages = 0

    for filename in os.listdir(path):
        with open(os.path.join(path, filename), encoding="latin-1") as file:
            numOfMessages +=1

            # Iterates through each line in the file
            for line in file:
                # Punctuations to look out for
                punctuations = "~`!@#$%^&*()-_+=[{]}|\;:'\",<>./?"

                # Checks if each character in the punctuations variable is present in the line
                for punc in punctuations:
                    line = line.replace(punc, "")   # Replaces the punctuation with an empty string
                    line = line.lower()             # Converts the line to lower-case characters

                # Splits the words in each line with the whitespace as a delimiter
                token_list = line.split()

                # Inserts each word in the token_list into the dictionary
                for token in token_list:
                    dict[token] = dict.get(token,0) + 1     # get() function returns the value held by the specified key, which, in this case, is "token"
                                                            # Second parameter in get() function is optional. Returns 0 if key does not exist in dictionary
                                                            # Also adds 1 to the value returned by get()
                    totalWords += 1         # Increments the total number of words by 1

        # Closing the file
        file.close()

    temp = [totalWords, numOfMessages]
    return temp


# Returns dictionary size
def getDictSize(dict):
    dictSize = len(dict)
    return dictSize


# Sorts dictionary alphabetically by key and returns it
def getDict(dict):
    # Sorts the dictionary by key
    from collections import OrderedDict
    sortedDict = OrderedDict(sorted(dict.items()))

    return sortedDict