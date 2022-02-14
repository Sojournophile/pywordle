import json
import random

dic = list(json.load(open("words_dictionary.json")).keys())


def play_game():
    current_word = ""
    while len(current_word) != 5:
        current_word = random.choice(dic)
    # print(current_word)
    won = False
    tries = 6
    while not won and tries > 0:
        attempt = ""
        while len(attempt) != 5 and not attempt.isalpha():
            attempt = input("Guess: ").lower()
            if attempt not in dic:
                print("Not a valid word")
                attempt = ""
            elif len(attempt) != 5:
                print("Guess must be 5 letters")
            elif not attempt.isalpha():
                print("Letters only.")
        print(attempt.upper())
        if attempt == current_word:
            print("You win!")
            won = True
        else:
            result = ""
            letter_count = 0
            for letter in attempt:
                if letter == current_word[letter_count]:
                    result += "2"
                    # result += "🟩"
                elif letter in current_word:
                    result += "1"
                    # result += "🟨"
                else:
                    result += "0"
                    # result += "⬛"
                letter_count += 1
            print(result)
            tries -= 1
            print(str(tries), "tries remaining")
    if not won:
        print("You lose! The word was", current_word.upper(), "!")