# tldr bot

## Overview
This is a program which takes in a block of text and attempts to summarize it. The bot works by first creating a dictionary of word frequencies based on the non-stopwords words in the text. Stopwords are words such as "the" and "is" that do not add any meaning to a sentence. Each sentence is then assigned a value based on its word frequencies. To compensate for the fact that longer sentences have an inherent advantage, sentence scores will be divided by their length. Finally, sentences with the highest scores are used to create the summarized version of the text. Sentences with the bottom 78% of scores will be excluded from the final summary.

## Installation

The only requirement is nltk. Install it using pip

```bash
pip install nltk
```

## Usage

Run tldr.py to create a new tldr from an existing text source. The program will prompt you for the name of a textfile to read from. The output will also be a textfile containing the shortened text.

Run the wikipediaCrawl.py file to gather text from a wikipedia article. You will need to provide the program with an article link and an output name. The output name is the name of the final text file (must end in .txt). If one is not provided, the article title will be used as the name.
