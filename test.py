ARGUMENT = {'start': {
    'text': "You start the argument by noting that Star Wars is fantasy, not science-fiction. John replies that, no, it isn't",

    'choices': [('Yes it is.', 'yes-is'), ('Point out that Star Wars is just swords and sorcery.', 'yes-is')]},
            'yes-is': {'text': "John replies that, no, it isn't.",
                       'choices': [('Yes it is.', 'yes-is'), ("Point out that's not actually arguing.", 'not-argue')]},
            'not-argue': {
                'text': "You point out that an argument is not the needless gainsaying of whatever is said to you. John replies that, yes, it is.",
                'choices': [("No it isn't", 'no-is'), ("Point out that he's doing it again.", 'again')]},
            'no-is': {'text': "John replies that, yes, it is.",
                      'choices': [("No it isn't", 'no-is'), ("Point out that he's doing it again.", 'again')]},
            'again': {
                'text': "You point out that John is just needlessly gainsaying again. He replies that no, he isn't",
                'choices': [('Yes you are!', 'yes-are'), ("Point out that he's doing it again.", 'the-end')]},
            'yes-are': {'text': "John replies that, no, he isn't.",
                        'choices': [('Yes you are!', 'yes-are'), ("Point out that he's doing it again.", 'the-end')]},
            'the-end': {'text': "Ding! I'm sorry, time's up."}}


def choose(choices):
    print('\nChoose one:')
    for choice_index, choice in enumerate(choices, start=1):
        print('{}: {}'.format(choice_index, choice[0]))
    while True:
        choice = input('\nWhat is your choice? ')
        try:
            return choices[int(choice) - 1][1]
        except (IndexError, ValueError):
            print('That is not a valid choice.')


def play(adventure):
    page_name = 'start'
    while not page_name.endswith('-end'):
        page = adventure[page_name]
        print('')
        print(page['text'])
        page_name = choose(page['choices'])
    print('')
    print(adventure[page_name]['text'])
    print('\nThanks for playing!')


if __name__ == '__main__':
    play(ARGUMENT)