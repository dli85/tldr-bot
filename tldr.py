from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer

text = """
Times Insider explains who we are and what we do, and delivers behind-the-scenes insights into how our journalism comes together.

In March, when the coronavirus pandemic began to spread and increase in severity, the Times newsroom was already devoting enormous resources to covering it. But as the deputy editor for Special Sections, I also started thinking about what we could offer our readers — as they were quarantined, stressed and perhaps even ill — that was positive, distracting and, most important, helpful.

And so our (more or less) weekly Resilience series was born. It’s admittedly a broad topic: Resilience can take so many forms, and means different things to different people. In a way, though, that made it a particularly interesting series to assign and edit. I knew I wanted a variety of voices, some offering specific advice, others affording writers with particular and unusual perspectives a place to share their stories.

Before the series began, I happened to be in the middle of reading Eva Holland’s new book, “Nerve: Adventures in the Science of Fear,” in which she discussed both overcoming her own traumas and researching groundbreaking techniques intended to combat phobias. So I asked her if she would write about trauma therapies and what lessons we could learn from them.

Like Ms. Holland’s article, most pieces in the series combined some form of personal narrative and information that the reader could use. In her article on what makes some people more resilient than others, Eilene Zimmerman wrote about losing her ex-husband to a drug overdose, but also how stress can actually be a character-building experience. “You can think of resilience as a set of skills that can be, and often is, learned,” she wrote. “Part of the skill-building comes from exposure to very difficult — but manageable — experiences.” That resonated with me, and, I’m guessing, many of our readers.

These sorts of series generally consist of a combination of ideas I have and pitches I get from writers. Either way, some perspectives inevitably feel entirely counterintuitive to those who haven’t lived through them. Take the article by Phil Klay, the veteran and National Book Award winner, whom we asked to write about what we could learn from PTSD and war trauma. Some soldiers, he said, “found in their suffering a strange and terrible blessing.”

Or the one by Bonnie Tsui, who also has a new book, “Why We Swim,” that touches on elements of resilience. Bonnie suggested that she write about the older swimmers she had come across over the years, and how the activity had kept them not just physically fit, but mentally and emotionally stable.

It’s a fascinating article, but I was also touched by many of the comments it got from readers. They wrote about swimming as liberating and healing, in a way I’m not sure I’ve experienced. “If you’re a good enough swimmer to keep going for 30, 45, 60 minutes or more, no matter how slowly, what you will experience is a moving meditation, a floating tranquillity and mindfulness,” one reader wrote. “That’s what I sorely miss, as well as the physical exercise, and am waiting impatiently for the pool to reopen.”

We’ve tried to include helpful tips and techniques in each of these articles, but some are simply inspirational stories — a balm, we hope, for the pervasive anxiety we’re all facing.

I’ve sometimes joked to my colleagues in the newsroom that during this pandemic, we should just rename The Times “Pivoting!” Nearly everyone is having to adapt to new circumstances and challenges — personal, professional and otherwise. But the hardest part for me are the unknowns: Will my daughter go to school in the fall? Will there be an uptick in cases as colder weather comes to New York? The open questions can feel overwhelming. What these resilience pieces have in common is a focus on how to combat that spiral — both through guidance and others’ experiences in overcoming hardships.

And there is more to come. We just published an entertaining and thought-provoking piece by the novelist Jami Attenberg on whether resilience might be overrated. “I am not suggesting we stop encouraging others to succeed, or surpass goals,” she wrote. “But are we seeing the concept of resilience in its current incarnation for what it really is?”

I hope this series provides at least the start of an answer to Ms. Attenberg’s question: Resilience is about perspective, about what we can — and can’t — do when times are tough, about knowing our limits and, sometimes, when we can, going beyond them.

"""

def createTLDR(data, sentenceTable, average, multiplier):
    current_line_length = 0
    f = open("output.txt", 'w')
    for s in sent_tokenize(data):
        if s in sentenceTable and sentenceTable[s] >= average * multiplier:
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

    freqT = createTable(text)
    sentenceTable = sentenceValues(freqT, text)

    average = 0
    for s in sentenceTable:
        average += sentenceTable[s]
    average /= len(sentenceTable)

    multiplier = input('What multiplier (default is 1.3): ')

    try:
        multiplier = int(multiplier)
    except:
        multiplier = 1.3
    else:
        multiplier = int(multiplier)

    outputName = input('Save the output as? (filename should end in .txt) Default is output.txt: ')

    if len(outputName) == 0:
        outputName = 'output.txt'

    createTLDR(text, sentenceTable, average, multiplier)


