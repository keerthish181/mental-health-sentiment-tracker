from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    polarity = None
    if request.method == 'POST':
        text = request.form['journal_entry']
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            sentiment = 'Positive'
        elif polarity < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
    return render_template('form.html', sentiment=sentiment, polarity=polarity)

if __name__ == '__main__':
    app.run(debug=True)
