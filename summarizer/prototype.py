import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

# nltk.download('punkt')

# url = "https://edition.cnn.com/2024/06/27/politics/presidential-debate-trump-biden/index.html"

# article = Article(url)

# article.download()
# article.parse()
# article.nlp()

# print(f'Title: {article.title}')
# print(f'Authors: {article.authors}')
# print(f'Publication Date: {article.publish_date}')
# print(f'Summary: {article.summary}')

# analysis = TextBlob(article.text)
# print(analysis.polarity)
# print(f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')


root = tk.Tk()
root.title("Article Summarizer")
root.geometry('1200x600')

tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg="#dddddd")
title.pack()

auth_label = tk.Label(root, text="Author")
auth_label.pack()

author = tk.Text(root, height=1, width=140)
author.config(state="disabled", bg="#dddddd")
author.pack()

p_label = tk.Label(root, text="Publication Date")
p_label.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state="disabled", bg="#dddddd")
publication.pack()

sum_label = tk.Label(root, text="Summary")
sum_label.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state="disabled", bg="#dddddd")
summary.pack()

senti_label = tk.Label(root, text="Sentiment Analysis")
senti_label.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state="disabled", bg="#dddddd")
sentiment.pack()

url_label = tk.Label(root, text="URL")
url_label.pack()

url_text = tk.Text(root, height=1, width=140)
url_text.pack()


btn = tk.Button(root, text="Summarize")
btn.pack()
root.mainloop()
