# tldr bot

## Overview
This is a program which takes in a block of text and attempts to summarize it. The bot works by first creating a dict of word frequencies based on the non-stopwords words in the text. Each sentence is then assigned a value based on its word frequencies. To compensate for the fact that longer sentences have an inherent advantage, sentence scores will be divided by their length. Finally, sentences with the highest scores are used to create the summarized version of the text.

## Installation

The only requirement is nltk

```bash
pip install nltk
```

## Usage

Run tldr.py to create a new tldr from an existing text source. You will be prompted for three inputs. The first is the name of the text file that you want to use. If you leave this empty, the program resort to the hard coded text instead. The next input is the multiplier. The multiplier determines the length of the summary. A larger multiplier will result in a smaller summary as sentences with values greater than average * multiplier will be included. The file input is the output file name. The output name is what the output text file should be called. 

Run the wikipediaCrawl.py file to gather text from a wikipedia article. The file will prompt you for two inputs, a article link and an output name. The article link is the link of the wikipedia article that you want to crawl. The output name is the name of the final text file (must end in .txt). If one is not provided, the article title will be used instead.
