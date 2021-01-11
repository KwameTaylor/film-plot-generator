import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from numpy.random import choice

import re
import unicodedata
import nltk

# default viz size settings
plt.rc('figure', figsize=(9, 7))
plt.rc('font', size=15)

from wordcloud import WordCloud

def word_cloud_1(all_words, javascript_words, python_words):
    all_cloud = WordCloud(background_color='white', colormap='cividis', height=1000, width=400, margin=2).generate(all_words)
    javascript_cloud = WordCloud(background_color='white', colormap='winter', height=600, width=800, margin=2).generate(javascript_words)
    python_cloud = WordCloud(background_color='white', colormap='cool', height=600, width=800, margin=2).generate(python_words)

    plt.figure(figsize=(10, 8))
    axs = [plt.axes([0, 0, .6, 1]), plt.axes([.5, .5, .45, .45]), plt.axes([.5, 0, .45, .45])]

    axs[0].imshow(all_cloud)
    axs[1].imshow(javascript_cloud)
    axs[2].imshow(python_cloud)

    axs[0].set_title('All Words')
    axs[1].set_title('Javascript')
    axs[2].set_title('Python')

    for ax in axs: ax.axis('off')

    plt.show