from emoji import UNICODE_EMOJI


MAX_FONT_SIZE = 200


class EmojiCloud(text):

    def __init__(text):

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

        return emojis


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
        font_size = (count * MAX_FONT_SIZE) / highest_count
        return int(font_size)
