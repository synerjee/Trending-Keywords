import feedparser
import io

from rake_nltk import Metric, Rake
from nltk.corpus import stopwords

from wordcloud import WordCloud

headlines = []

# Uses feedparser to collect titles (headlines) from various news outlets.
def collectHeadlines(rss_url):
    feed = feedparser.parse(rss_url)

    # Add every headline to the global array.
    for entry in feed.entries:
        headlines.append(entry.title)

# urls.txt contains the list of all URLs of news outlet used for this
# code.
urls_file = open("urls.txt", "r")

urls = urls_file.readlines()

for url in urls:
    collectHeadlines(url)

urls_file.close()

# Then an NLP tool called Rake (or rake_nltk) is used to analyze each
# headline.
r = Rake(ranking_metric=Metric.DEGREE_TO_FREQUENCY_RATIO, min_length=1, max_length=3)

# Since the analysis takes the form of a list of pairs, each of which consists
# of a phrase and its score (which denotes its importance), a dictionary
# would be nice when it comes to storing these pairs.
freq_dict = {}

for title in headlines:
    # Here is where Rake does its work.
    extract = r.extract_keywords_from_text(title)
    pair_array = r.get_ranked_phrases_with_scores()

    # Each pair will be stored in the dictionary.
    if (len(pair_array) > 0):
        for pair in pair_array:
            if (pair[1] not in freq_dict):
                freq_dict[pair[1]] = pair[0]
            else:
                freq_dict[pair[1]] += pair[0]

# Time to sort the dictionary. Top 30 phrases will be used for the word cloud.
#sort_phrases = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
#phrase_list = sort_phrases[:30]

word_cloud = WordCloud(background_color="white", width = 1000, height = 500).generate_from_frequencies(freq_dict)
word_cloud_svg = word_cloud.to_file('cloud.png')