# Trending-Keywords
A Python script that collects RSS feeds and creates a word cloud, which is made of keywords of the day.

To use this script, download update.py and urls.txt from this repo. Then move to wherever the files are located, and type in the console this command:
'python update.py'

Note that it may take a while for the script to be processed.
Once it is finished, there will be a new image called 'cloud.png', which is the image of the word cloud.
Note that running the script multiple times with the image in the same directory will simply overwrite the image. This may or may not change the content 
of the image, depending on the RSS Feed.

# Technologies used for this script
Python 3.9.1
Python libraries: feedparser, rake-nltk, wordcloud

# How this script works
It works in three steps.

1) Data Collection
2) Natural Language Processing (NLP)
3) Visualizing the Result as a Word Cloud

- Data Collection
Data were collected using a Python library called 'feedparser,' which uses RSS feeds to collect data from various news outlets. 
Specifically, headlines of various news articles were gathered.

- Natural Language Processing
It is not enough to simply gather data, but to use them. Since the data took the form of text, it would be appropriate to use an NLP library 
to process these data. The library used here is called 'nltk-rake.' With this library, it only took a few lines of code to extract keywords 
from the headlines. 
Each keyword is given a numerical value depending on metrics set by the programmer (the metric used in this script is 'Degree to Frequency Ratio.'),
which is very useful if one wished to rank the keywords in some order.
Once having ranked the keywords, the top 30 were selected.

- Visualizing the Result as a Word Cloud
The top 30 keywords should give one a decent idea of what is going on at the moment. Visualization helps to put data into perspective.
The visualization method used in this script is a 'word cloud,' which is a common form of visualization of textual data. 
A Python library called 'wordcloud' was perfect for this step, even providing a method that saves the result as a file.

'sample.png' should give you an idea of how the end result of this script would look like.
