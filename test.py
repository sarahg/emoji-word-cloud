from emoji_word_cloud.emoji_word_cloud import EmojiCloud
from sys import argv
import json

script, input_file = argv

text = open(input_file).read()

emojis = EmojiCloud(text)
weighted = EmojiCloud.buildCloud(emojis)
   
print (json.dumps({'status':'OK','weighted_emojis':weighted}))
