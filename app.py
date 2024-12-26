from flask import Flask, request, render_template, jsonify
import nltk
from textblob import TextBlob
from collections import Counter
import os
import json

nltk.download('punkt')

app = Flask(__name__)


def read_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text


def analyze_text(text):
    words = nltk.word_tokenize(text)
    sentences = nltk.sent_tokenize(text)

    word_count = len(words)
    sentence_count = len(sentences)
    character_count = len(text)
    character_count_no_spaces = len(text.replace(' ', ''))

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "character_count": character_count,
        "character_count_no_spaces": character_count_no_spaces
    }


def readability_scores(text):
    import textstat
    flesch_kincaid = textstat.flesch_reading_ease(text)
    gunning_fog = textstat.gunning_fog(text)

    return {
        "flesch_kincaid": flesch_kincaid,
        "gunning_fog": gunning_fog
    }


def keyword_frequency(text, keywords):
    words = nltk.word_tokenize(text.lower())
    frequency = Counter(words)
    keyword_freq = {keyword: frequency[keyword] for keyword in keywords}

    return keyword_freq


def most_common_words(text, n=10):
    words = nltk.word_tokenize(text.lower())
    frequency = Counter(words)
    common_words = frequency.most_common(n)

    return common_words


def sentiment_analysis(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment

    return {
        "polarity": sentiment.polarity,
        "subjectivity": sentiment.subjectivity
    }


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file']
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    text = read_file(file_path)

    keywords = request.form.get('keywords')
    if keywords:
        keywords = json.loads(keywords)
    else:
        keywords = []

    basic_analysis = analyze_text(text)
    readability = readability_scores(text)
    keyword_freq = keyword_frequency(text, keywords)
    common_words = most_common_words(text)
    sentiment = sentiment_analysis(text)

    result = {
        "basic_analysis": basic_analysis,
        "readability_scores": readability,
        "keyword_frequency": keyword_freq,
        "most_common_words": common_words,
        "sentiment_analysis": sentiment
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
