import os;
import decimal;     # We need decimal.Decimal
import math;        # We need math.exp()
import bagOfWords as bagOfWords;


# ===================================================================================================
# Creating a bag of words from the ham and spam datasets


# Path to the directory containing the ham messages
pathHam = "../datasets/data01/ham"
# Initializing dictionary
dictHam = {}

# Pass each file to bow.py
temp = bagOfWords.createBOW(pathHam, dictHam)
dictHam = bagOfWords.getDict(dictHam)
dSizeHam = bagOfWords.getDictSize(dictHam)

totalWordsHam = temp[0]
messagesHam = temp[1]


# Path to the directory containing the spam messages
pathSpam = "../datasets/data01/spam"
# Initializing dictionary
dictSpam = {}

# Pass each file to bow.py
temp = bagOfWords.createBOW(pathSpam, dictSpam)
dictSpam = bagOfWords.getDict(dictSpam)
dSizeSpam = bagOfWords.getDictSize(dictSpam)

totalWordsSpam = temp[0]
messagesSpam = temp[1]


# Merging the spam and ham dictionary
combinedDict = []
for key in dictHam.keys():
    combinedDict.append(key)
for key in dictSpam.keys():
    if key in combinedDict:
        continue
    else:
        combinedDict.append(key)


# ===================================================================================================
# Classifying the actual messages to either spam or ham

# Asking the user for the value of k
k = int(input("Enter value for k: "))

probSpam = decimal.Decimal((messagesSpam + k) / ((messagesSpam + messagesHam) + (2*k)))
probHam = decimal.Decimal(1 - probSpam)


def classifyMessage(path, m):
    dict = {}
    newWords = 0

    with open(path, encoding="latin-1") as file:
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
            
            if token in combinedDict:   # Checking if token exists as a key in combinedDict
                continue
            else:
                newWords += 1           # Increments the number of new words by 1


    # Computing for probability of message given Spam
    prob = []
    i=0
    for key in dict.keys():
        j = dictSpam.get(key, 0)
        prob.append(((j + k) / (totalWordsSpam + (k * (len(combinedDict) + newWords)))))

    probMesSpam = 1
    for element in prob:
        probMesSpam = decimal.Decimal(element) * decimal.Decimal(probMesSpam)

    probMesSpam = decimal.Decimal(probMesSpam) * probSpam

    # Gets the ln of the probability of message given Spam
    probMesSpam = probMesSpam.ln()


    # Computing for probability of message given Ham
    prob = []
    i=0
    for key in dict.keys():
        j = dictHam.get(key, 0)
        prob.append(((j + k) / (totalWordsHam + (k * (len(combinedDict) + newWords)))))

    probMesHam = 1
    for element in prob:
        probMesHam = decimal.Decimal(element) * decimal.Decimal(probMesHam)

    probMesHam = decimal.Decimal(probMesHam) * probHam
    
    # Gets the ln of the probability of message given Spam
    probMesHam = probMesHam.ln()

 
    # The code below does exp(probMesHam)
    probMesHam = decimal.Decimal(math.exp(1))**probMesHam
    probMesSpam = decimal.Decimal(math.exp(1))**probMesSpam


    try:
        # Computing for probability of Spam given message
        answer = (probMesSpam) / (probMesSpam + probMesHam)
            
    except Exception as exception:
        print (exception)


    # Writing to output file
    if m == 1:
        fp = open("../output/classify.out", "w")  # If we are in the first iteration, write file
    else:
        fp = open("../output/classify.out", "a")  # If we are not in the first iteration, apppend to file

    
    threshold = 0.50
    if answer < threshold:
        # Message is a Ham
        fp.write(str(m).zfill(3) +  " HAM  " + str(answer) + "\n")      # str(m).zfill(3) converts m integer into a string with leading zeroes
        
    else:
        # Message is a spam
        fp.write(str(m).zfill(3) + " SPAM " + str(answer) + "\n")


    # Closing the files
    fp.close()
    file.close()


# ===================================================================================================

# Path to the directory containing the messages to be classified
pathClassify = "../datasets/data01/classify"
m = 1
for filename in sorted(os.listdir(pathClassify)):               # os.listdir(directory) gets all the folders listed in the given directory
    classifyMessage(os.path.join(pathClassify, filename), m)    # os.path.join(a, b*) concatenates at least two strings into a pathname
    m += 1