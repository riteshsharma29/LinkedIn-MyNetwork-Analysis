import streamlit as st
import plotly.express as px
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="WordCloud of MyConnections")

st.sidebar.success("Finally displaying  WordCloud of MyConnections.")

connections_df = pd.read_csv(os.path.join(os.getcwd(),"Connections.csv"))

positions = ' '.join(connections_df[~connections_df.Position.str.lower().isnull()].Position.unique())

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt


def make_wordcloud(new_text):
    ''''function to make wordcloud'''

    wordcloud = WordCloud(width=800, height=800,
                          min_font_size=10,
                          background_color='black',
                          colormap='Set2',
                          collocations=False).generate(new_text)

    fig7 = plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=0)
    return fig7


st.pyplot(make_wordcloud(positions))


