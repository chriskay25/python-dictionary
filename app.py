import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        confirm = input('Did you mean %s? Enter "y" for yes or "n" for no.' % get_close_matches(word, data.keys())[0])
        confirm = confirm.lower()
        if confirm == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif confirm == 'n':
            return 'Sorry, could not find that word. Please try again.'
        else:
            'Sorry, invalid confirmation.'
    else:
        return 'Sorry, could not find that word. Please try again.'

word = input('Enter word: ')

print(translate(word)) 