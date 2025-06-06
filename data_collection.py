import pandas as pd
import os

def fetch_articles():
    dataset = pd.read_csv("merged_data.csv")
    print(dataset.columns)
    articles = dataset.to_dict('records')
    for article in articles:
            article['url'] = article.get('url', '')
    return articles
