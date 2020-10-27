from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer

text = """
"""

def readFromFile(fileName):
    with open(fileName, 'r', encoding="utf8") as file:
        data = file.read().replace('\n', '')
    global text
    text = data

def createTLDR(data, sentenceTable, scoreFloor):
    current_line_length = 0
    f = open("output.txt", 'w')
    for s in sent_tokenize(data):
        if s in sentenceTable and sentenceTable[s] >= scoreFloor:
            sent = s + " "

            current_line_length += len(sent)
            if current_line_length >= 90:
                current_line_length = 0
                f.write('\n')
            f.write(sent)

def countStopwordInSent(sentence):
    stopWords = set(stopwords.words('english'))
    count = 0
    words = word_tokenize(sentence)
    for w in words:
        if w.lower() in stopWords:
            count += 1

    return count

def sentenceValues(freqT, data):
    sentences = sent_tokenize(data)
    sentenceTable = {}

    for s in sentences:
        wordCount = len(word_tokenize(s))

        for w in freqT:
            if w in s.lower():
                if s in sentenceTable:
                    sentenceTable[s] += freqT[w]
                else:
                    sentenceTable[s] = freqT[w]

        stopwordCount = countStopwordInSent(s)
        if s in sentenceTable:
            sentenceTable[s] = sentenceTable[s] / (wordCount - stopwordCount)

    return sentenceTable

def createTable(data):
    porterstemmer = PorterStemmer()
    stopWords = set(stopwords.words('english'))
    tokenized_by_words = word_tokenize(data)
    freqT = {}

    for word in tokenized_by_words:
        w = porterstemmer.stem(word)
        if w not in stopWords:
            if word not in freqT:
                freqT[w] = 1
            else:
                freqT[w] += 1
    return freqT

if __name__ == '__main__':

    fileName = input("Enter the text file that you want to read from (should end in .txt): ")

    if len(fileName) > 0:
        readFromFile(fileName)
    else:
        readFromFile('sample_text.txt')

    freqT = createTable(text)
    sentenceTable = sentenceValues(freqT, text)

    average = 0
    scoresList = []
    for s in sentenceTable:
        average += sentenceTable[s]
        scoresList.append(sentenceTable[s])
    average /= len(sentenceTable)

    scoresList.sort()

    scoreFloor = scoresList[int(len(scoresList)*0.78)]

    outputName = input('Save the output as? (filename should end in .txt) Default is output.txt: ')

    if len(outputName) == 0:
        outputName = 'output.txt'

    createTLDR(text, sentenceTable, scoreFloor)


