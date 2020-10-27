from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer

text = """
If there’s one word admirers and critics alike can agree on when it comes to The New York Times’s award-winning 1619 Project, it’s ambition. Ambition to reframe America’s conversation about race. Ambition to reframe our understanding of history. Ambition to move from news pages to classrooms. Ambition to move from scholarly debate to national consciousness.

In some ways, this ambition succeeded. The 1619 Project introduced a date, previously obscure to most Americans, that ought always to have been thought of as seminal — and probably now will. It offered fresh reminders of the extent to which Black freedom was a victory gained by courageous Black Americans, and not just a gift obtained from benevolent whites.

It showed, in a stunning photo essay, the places where human beings were once bought and sold as slaves — neglected scenes of American infamy. It illuminated the extent to which so much of what makes America great, including some of our uniquely American understandings of liberty and equality, is unthinkable without the struggle of Black Americans, as well as the extent to which so much of what continues to bedevil us is the result of centuries of racism.

And, in a point missed by many of the 1619 Project’s critics, it does not reject American values. As Nikole Hannah-Jones, its creator and leading voice, concluded in her essay for the project, “I wish, now, that I could go back to the younger me and tell her that her people’s ancestry started here, on these lands, and to boldly, proudly, draw the stars and those stripes of the American flag.” It’s an unabashedly patriotic thought.

But ambition can be double-edged. Journalists are, most often, in the business of writing the first rough draft of history, not trying to have the last word on it. We are best when we try to tell truths with a lowercase t, following evidence in directions unseen, not the capital-T truth of a pre-established narrative in which inconvenient facts get discarded. And we’re supposed to report and comment on the political and cultural issues of the day, not become the issue itself.

As fresh concerns make clear, on these points — and for all of its virtues, buzz, spinoffs and a Pulitzer Prize — the 1619 Project has failed.

Those concerns came to light last month when a longstanding critic of the project, Phillip W. Magness, noted in the online magazine Quillette that references to 1619 as the country’s “true founding” or “moment [America] began” had disappeared from the digital display copy without explanation.

These were not minor points. The deleted assertions went to the core of the project’s most controversial goal, “to reframe American history by considering what it would mean to regard 1619 as our nation’s birth year.”

That doesn’t mean that the project seeks to erase the Declaration of Independence from history. But it does mean that it seeks to dethrone the Fourth of July by treating American history as a story of Black struggle against white supremacy — of which the Declaration is, for all of its high-flown rhetoric, supposed to be merely a part.

In a tweet, Hannah-Jones responded to Magness and other critics by insisting that “the text of the project” remained “unchanged,” while maintaining that the case for making 1619 the country’s “true” birth year was “always a metaphoric argument.” I emailed her to ask if she could point to any instances before this controversy in which she had acknowledged that her claims about 1619 as “our true founding” had been merely metaphorical. Her answer was that the idea of treating the 1619 date metaphorically should have been so obvious that it went without saying.

She then challenged me to find any instance in which the project stated that “using 1776 as our country’s birth date is wrong,” that it “should not be taught to schoolchildren,” and that the only one “that should be taught” was 1619. “Good luck unearthing any of us arguing that,” she added.

Here is an excerpt from the introductory essay to the project by The New York Times Magazine’s editor, Jake Silverstein, as it appeared in print in August 2019 (italics added):

“1619. It is not a year that most Americans know as a notable date in our country’s history. Those who do are at most a tiny fraction of those who can tell you that 1776 is the year of our nation’s birth. What if, however, we were to tell you that this fact, which is taught in our schools and unanimously celebrated every Fourth of July, is wrong, and that the country’s true birth date, the moment that its defining contradictions first came into the world, was in late August of 1619?”

Now compare it to the version of the same text as it now appears online:

“1619 is not a year that most Americans know as a notable date in our country’s history. Those who do are at most a tiny fraction of those who can tell you that 1776 is the year of our nation’s birth. What if, however, we were to tell you that the moment that the country’s defining contradictions first came into the world was in late August of 1619?”

In an email, Silverstein told me that the changes to the text were immaterial, in part because it still cited 1776 as our nation’s official birth date, and because the project’s stated aim remained to put 1619 and its consequences as the true starting point of the American story.

Readers can judge for themselves whether these unacknowledged changes violate the standard obligations of transparency for New York Times journalism. The question of journalistic practices, however, raises deeper doubts about the 1619 Project’s core premises.

In his introduction, Silverstein argues that America’s “defining contradictions” were born in August 1619, when a ship carrying 20 to 30 enslaved Africans from what is present-day Angola arrived in Point Comfort, in the English colony of Virginia. And the title page of Hannah-Jones’s essay for the project insists that “our founding ideals of liberty and equality were false when they were written.”

Both points are illogical. A “defining contradiction” requires a powerful point of opposition or inconsistency, and in the year 1619 the points of opposition were few and far between. Slavery and the slave trade had been global phenomena for centuries by the early 17th century, involving Europeans and non-Europeans as slave traders and the enslaved. The Africans who arrived in Virginia that August got there only because they had been seized by English privateers from a Portuguese ship headed for the port of Veracruz in Mexico, then a part of the Spanish Empire.

In this sense, and for all of its horror, there was nothing particularly surprising in the fact that slavery made its way to the English colonies on the Eastern Seaboard, as it already had in the rest of the Western Hemisphere.

What was surprising was that in 1776 a politically formidable “defining contradiction” — “that all men are created equal” — came into existence through the Declaration of Independence. As Abraham Lincoln wrote in 1859, that foundational document would forever serve as a “rebuke and stumbling block to the very harbingers of reappearing tyranny and oppression.” It’s why, at the dedication of the Gettysburg cemetery, Lincoln would date the country’s founding to “four score and seven years ago.”

As for the notion that the Declaration’s principles were “false” in 1776, ideals aren’t false merely because they are unrealized, much less because many of the men who championed them, and the nation they created, hypocritically failed to live up to them. Most of us, at any given point in time, are falling short of some ideal we nonetheless hold to be true or good.

These two flaws led to a third, conceptual, error. “Out of slavery — and the anti-Black racism it required — grew nearly everything that has truly made America exceptional,” writes Silverstein.

Nearly everything? What about, say, the ideas contained by the First Amendment? Or the spirit of openness that brought millions of immigrants through places like Ellis Island? Or the enlightened worldview of the Marshall Plan and the Berlin airlift? Or the spirit of scientific genius and discovery exemplified by the polio vaccine and the moon landing? On the opposite side of the moral ledger, to what extent does anti-Black racism figure in American disgraces such as the brutalization of Native Americans, the Chinese Exclusion Act or the internment of Japanese-Americans in World War II?

Monocausality — whether it’s the clash of economic classes, the hidden hand of the market, or white supremacy and its consequences — has always been a seductive way of looking at the world. It has always been a simplistic one, too. The world is complex. So are people and their motives. The job of journalism is to take account of that complexity, not simplify it out of existence through the adoption of some ideological orthodoxy.

This mistake goes far to explain the 1619 Project’s subsequent scholarly and journalistic entanglements. It should have been enough to make strong yet nuanced claims about the role of slavery and racism in American history. Instead, it issued categorical and totalizing assertions that are difficult to defend on close examination.

It should have been enough for the project to serve as curator for a range of erudite and interesting voices, with ample room for contrary takes. Instead, virtually every writer in the project seems to sing from the same song sheet, alienating other potential supporters of the project and polarizing national debate.

An early sign that the project was in trouble came in an interview last November with James McPherson, the Pulitzer Prize-winning author of “Battle Cry of Freedom” and a past president of the American Historical Association. He was withering: “Almost from the outset,” McPherson told the World Socialist Web Site, “I was disturbed by what seemed like a very unbalanced, one-sided account, which lacked context and perspective.”

In particular, McPherson objected to Hannah-Jones’s suggestion that the struggle against slavery and racism and for civil rights and democracy was, if not exclusively then mostly, a Black one. As she wrote in her essay: “The truth is that as much democracy as this nation has today, it has been borne on the backs of Black resistance.”

McPherson demurs: “From the Quakers in the 18th century, on through the abolitionists in the antebellum, to the Radical Republicans in the Civil War and Reconstruction, to the N.A.A.C.P., which was an interracial organization founded in 1909, down through the civil rights movements of the 1950s and 1960s, there have been a lot of whites who have fought against slavery and racial discrimination, and against racism,” he said. “And that’s what’s missing from this perspective.”

In a lengthier dissection, published in January in The Atlantic, the Princeton historian Sean Wilentz accused Hannah-Jones of making arguments “built on partial truths and misstatements of the facts.” The goal of educating Americans on slavery and its consequences, he added, was so important that it “cannot be forwarded through falsehoods, distortions and significant omissions.”

Wilentz’s catalog of the project’s mistakes is extensive. Hannah-Jones’s essay claimed that by 1776 Britain was “deeply conflicted” over its role in slavery. But despite the landmark Somerset v. Stewart court ruling in 1772, which held that slavery was not supported by English common law, it remained deeply embedded in the practices of the British Empire. The essay claimed that, among Londoners, “there were growing calls to abolish the slave trade” by 1776. But the movement to abolish the British slave trade only began about a decade later — inspired, in part, Wilentz notes, by American antislavery agitation that had started in the 1760s and 1770s. The list goes on.

Then there was an essay in Politico in March by the Northwestern historian Leslie M. Harris, an expert on pre-Civil War African-American life and slavery. “On Aug. 19 of last year,” Harris wrote, “I listened in stunned silence as Nikole Hannah-Jones … repeated an idea that I had vigorously argued against with her fact checker: that the patriots fought the American Revolution in large part to preserve slavery in North America.”

None of this should have come as a surprise: The 1619 Project is a thesis in search of evidence, not the other way around. Nor was this fire from the right: Both Wilentz and Harris were at pains to emphasize their sympathy with the project’s moral aims.

Yet, aside from a one-word “clarification” issued in March — after months of public pressure, The Times conceded that only “some” colonists fought for independence primarily to defend slavery — the response of the magazine has been, in effect, “nothing to see here.” In a pair of lengthy editor’s notes, Silverstein has defended much of the scholarship in the project by citing another slate of historians to back him up. That’s one way of justifying the final product.

The larger problem is that The Times’s editors, however much background reading they might have done, are not in a position to adjudicate historical disputes. That should have been an additional reason for the 1619 Project to seek input from, and include contributions by, an intellectually diverse range of scholarly voices. Yet not only does the project choose a side, it also brooks no doubt.

“It is finally time to tell our story truthfully,” the magazine declares on its 1619 cover page. Finally? Truthfully? Is The Times suggesting that distinguished historians, like the ones who have seriously disputed aspects of the project, had previously been telling half-truths or falsehoods?



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


