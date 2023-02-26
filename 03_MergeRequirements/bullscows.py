import random
import sys
from urllib import request

def bullscows(guess, secret):
    bulls, cows = 0, 0
    for g, s in zip(guess, secret):
        if g == s:
            bulls += 1
        elif g in secret:
            cows += 1
    return bulls, cows

def gameplay(ask, inform, words):
    secret = random.choice(words)
    k = 0
    while True:
        guess = ask("Введите слово: ", words)
        k += 1
        inform("Быки: {}, Коровы: {}", *bullscows(guess, secret))
        if guess == secret:
            return k

if __name__ == '__main__':
    def ask(prompt, valid = None):
        if valid is None:
            return input(prompt)
        else:
            while True:
                guess = input(prompt)
                if guess in valid:
                    return guess

    def inform(format_string, bulls, cows):
        print(format_string.format(bulls, cows))

    dict_path = sys.argv[1]
    secret_len = int(sys.argv[2]) if len(sys.argv) == 3 else 5

    try:
        words = open(dict_path).readlines()
        words = [w.strip() for w in words if w.strip()]
    except:
        words = request.urlopen(dict_path).readlines()
        words = [w.decode('utf8').strip() for w in words if w.decode('utf8').strip()]

    words = [w for w in words if len(w) == secret_len]

    print(gameplay(ask, inform, words))