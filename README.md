# tldr bot

## Overview
This is a program which takes in a block of text and attempts to summarize it. The bot works by first creating a dictionary of word frequencies based on the non-stopwords words in the text. Each sentence is then assigned a value based on its word frequencies. To compensate for the fact that longer sentences have an inherent advantage, sentence scores will be divided by their length. Finally, sentences with the highest scores are used to create the summarized version of the text. Sentences with the bottom 78% of scores will be excluded from the final summary.

## Installation

The only requirement is nltk. Install it using pip

```bash
pip install nltk
```

## Usage

Run tldr.py to create a new tldr from an existing text source. You will be prompted for two inputs. The first is the name of the text file that you want to use. If you leave this empty, the program use the sample text file isntead (the sample text file contains an article from the New York Times). The second input is what you want the output text file should be called. If this field is left empty, the program will name the output file "output.txt". The program is hardcoded to exclude the bottom 78% percent of sentences from the final summary. You can change this value by chaning the hardcoded variable "topPercent" to something else.

Run the wikipediaCrawl.py file to gather text from a wikipedia article. The file will prompt you for two inputs, a article link and an output name. The article link is the link of the wikipedia article that you want to crawl. The output name is the name of the final text file (must end in .txt). If one is not provided, the article title will be used instead.
