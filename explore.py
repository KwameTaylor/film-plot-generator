import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import re
import unicodedata
import nltk

# default viz size settings
plt.rc('figure', figsize=(9, 7))
plt.rc('font', size=15)

from wordcloud import WordCloud

def word_cloud_1(wordlist):
    