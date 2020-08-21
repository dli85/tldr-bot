# tldr bot

This is a program which takes in a block of text and attempts to summarize it. The bot works by first creating a dict of word frequencies based on the non-stopwords words in the text. Each sentence is then assigned a value based on its word frequencies. To compensate for the fact that longer sentences have an inherent advantage, sentence scores will be divided by their length. Finally, sentences with the highest scores are used to create the summarized version of the text.

# Installation

The only requirement is nltk

```bash
pip install nltk
```

# Usage

To change what text is summarized, edit the global text variable. The program will prompt you for two inputs, a multiplier and an output name. The output name is what the output text file should be called. The multiplier determines the length of the summary. A larger multiplier will result in a smaller summary as sentences with values greater than average * multiplier will be included.


