from flask import Flask, render_template
import emoji_word_cloud

app = Flask(__name__)

@app.route('/')
def wordIn():
    return render_template('wordCloud.html')

@app.route('/wordUp', methods=['POST'])
def wordUp():
    text = request.form['emoji']
    emojis = emoji_word_cloud.EmojiCloud(text)
    
    return json.dumps({'status':'OK','weighted_emojis':emojis})

if __name__ == "__main__":
    app.run()
