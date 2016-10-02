from emoji_word_cloud import EmojiCloud
from sys import argv

script, input_file = argv

text = open(input_file).read()

cloud = EmojiCloud(text)
print (cloud)

# TODO
# Something's amiss with how the classes/modules are set up.
# $ python test.py emoji_word_cloud/emoji.txt
# Traceback (most recent call last):
#   File "test.py", line 1, in <module>
#     from emoji_word_cloud import EmojiCloud
# ImportError: cannot import name 'EmojiCloud'
