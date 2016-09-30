from sys import argv
from emoji import UNICODE_EMOJI
import json

script, input_file = argv


max_font_size = 200


def is_emoji(s):
    """ Check if a character is an emoji. """
    count = 0
    for emoji in UNICODE_EMOJI:
        count += s.count(emoji)
        if count > 1:
            return False
    return bool(count)


def get_emoji_weight(count, highest_count):
    """ Assign a font sized proportional to total occurances. """
    font_size = (count * max_font_size) / highest_count
    return int(font_size)


# Read the given text file.
text = open(input_file).read()


# Get a count of each unique emoji.
unique_characters = list(set(text))
emojis = []
 
for character in unique_characters:
    if is_emoji(character):
        emoji = {'character': character, 'count': text.count(character)}
        emojis.append(emoji)


# Get the most frequent emoji.
top_emoji = max(emojis, key=lambda x:x['count'])


# Set weights.
for emoji in emojis:
    emoji['weight'] = get_emoji_weight(emoji['count'], top_emoji['count'])
    


# Print a JSON object containing emojis, weights and counts.
print (json.dumps(emojis))
