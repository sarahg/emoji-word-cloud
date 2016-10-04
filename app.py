from flask import Flask, request, render_template
from emoji_word_cloud.emoji_word_cloud import EmojiCloud
import json

app = Flask(__name__)

@app.route('/')
def wordIn():
    return render_template('wordCloud.html')

# TODO 
#  File "app.py", line 12, in wordUp
#    text = request.form['emoji']
#   NameError: name 'request' is not defined
#   127.0.0.1 - - [03/Oct/2016 19:10:53] "POST /wordUp HTTP/1.1" 500 -

@app.route('/wordUp', methods=['POST'])
def wordUp():
    text = request.form['emoji']
   
    emojis = EmojiCloud(text)
    weighted = EmojiCloud.buildCloud(emojis)

    return json.dumps({'status':'OK','weighted_emojis':weighted})

if __name__ == "__main__":

    app.run()
