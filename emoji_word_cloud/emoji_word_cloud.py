from sys import argv
from emoji import UNICODE_EMOJI
import json

script, input_file = argv

# How many different sizes should be shown in the word cloud?
cloud_levels = 5

""" Check if a character is an emoji. """
def is_emoji(s):
    count = 0
    for emoji in UNICODE_EMOJI:
        count += s.count(emoji)
        if count > 1:
            return False
    return bool(count)

""" Set emoji weights for the word cloud. """
#def set_emoji_weights(emojis):
    # Get the total emoji count.
    # Separate items equal groups, based on size.
    # Algoritm is based on http://stackoverflow.com/a/1478314.

    # var words = [
    #   {text: ":beers:", weight: 13},
    #   {text: ":see-no-evil-monkey:", weight: 10.5},
    # ]
    
    #return cloud

# Read the given text file.
text = open(input_file).read()

# Create a list of the unique characters.
unique_characters = list(set(text))

# Count how many occurances of each emoji are in the file.
emoji_counts = {}
for character in unique_characters:
    if is_emoji(character): 
        emoji_counts[character] = text.count(character)

print (emoji_counts)

# Set weights.
#weighted_cloud = set_emoji_weights(emoji_counts)
#print (weighted_cloud)
        

# Prints a JSON object of JavaScript-escaped emojis with their counts
# print (json.dumps(emoji_counts))

