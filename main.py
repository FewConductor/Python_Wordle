char = 'abcdefghijklmnopqrstuvwxyz'

import module_wordle
import random
ans = module_wordle.words[random.randint(0,len(module_wordle.words)-1)]

# print(ans)

g = 1
guess = ''
while guess != ans:
    g1 = ''
    guess = input('Enter your guess: ')
    if guess not in module_wordle.allowed_words:
        print('Word not recognised. Please try again.')
    elif len(guess) != 5:
        print('Word not 5 letters. Please try again.')
    else:
        i = 0
        while i < 5:
            let = guess[i]
            if let in ans:
                if let == ans[i]:
                    g1 = g1 + let.upper()
                else:
                    g1 = g1 + let.lower()
                char = char.replace(let,let.upper())
            else:
                g1 = g1 + '_'
                char = char.replace(let,'_')
            i += 1
        print(f'Guess {g}: {g1}')
        print(f'Remaining letters: {char}')
        g += 1