from emoji import UNICODE_EMOJI


MAX_FONT_SIZE = 200


class EmojiCloud(object):

    def __init__(self, text):

        self.text = text


    def buildCloud(self):
        """ Gets weights of unique emoji characters in a string """
        # Get a count of each unique emoji.
        unique_characters = list(set(self.text))
        emojis = [] 
        for character in unique_characters:
            if self.is_emoji(character):
                emoji = {'text': character, 'count': self.text.count(character)}
                emojis.append(emoji)

        # Get the most frequent emoji.
        # We need this to set relative weights.
        top_emoji = max(emojis, key=lambda x:x['count'])

        # Set weights.
        for emoji in emojis:
            emoji['weight'] = self.get_emoji_weight(emoji['count'], top_emoji['count'])

        return emojis


    def is_emoji(self, s):
        """ Check if a character is an emoji. """
        count = 0
        for emoji in UNICODE_EMOJI:
            count += s.count(emoji)
            if count > 1:
                return False
        return bool(count)


    def get_emoji_weight(self, count, highest_count):
        """ Assign a font sized proportional to total occurances. """
        font_size = (count * MAX_FONT_SIZE) / highest_count
        return int(font_size)
