from colorama import Fore, Back, Style
from random import choice

def check_duplicates(word):
    word_no_duplicates = list(set(word))
    if len(word) != len(word_no_duplicates):
        return True
    else:
        return False

def analyze_guess(guess_letters, duplicates):
    results = []
    for index, letter in enumerate(guess_letters):
        if word_letters[index] == letter: 
            results.append(1)
        elif letter in word_letters:
            results.append(0.5)
        else:
            results.append(0)
    print(results)

    # guess_data = {}
    # for index, letter in enumerate(guess_letters):
    #     occurences = 0
    #     occurences_index = []
    #     for index2, letter2 in enumerate(guess_letters):
    #         if letter == letter2:
    #             occurences += 1
    #             if occurences > 0:
    #                 occurences_index.append(index2)
    #     print(letter, index, occurences, occurences_index)
    #     guess_data[letter] = (index, occurences, occurences_index)

    # word_data = {}
    # for index, letter in enumerate(word_letters):
    #     occurences = 0
    #     occurences_index = []
    #     for index2, letter2 in enumerate(word_letters):
    #         if letter == letter2:
    #             occurences += 1
    #             if occurences > 0:
    #                 occurences_index.append(index2)
    #     print(letter, index, occurences, occurences_index)
    #     word_data[letter] = (index, occurences, occurences_index)

    # print(guess_data)
    # print(word_data)
  
    # for index, letter in enumerate(guess_letters):
    #     if letter in word_data.keys():
    #         if guess_data[letter][1] != word_data[letter][1]:
    #              print(True, letter, guess_data[letter][1])
    #              print(word_data[letter][1])
    #              for index2, letter2 in enumerate(guess_letters):
    #                 if word_letters[index2] == letter2: 
    #                     results[index2] = 1
    #                 elif letter2 in word_letters:
    #                     results[index2] = 0



    return results

def display_results(guess_letters, results):
    for index, letter in enumerate(guess_letters):
        if results[index] == 0:
            print(letter, end="")
        elif results[index] == 0.5:
            print(Fore.YELLOW + letter, end="")
            print(Style.RESET_ALL, end="")
        elif results[index] == 1:
            print(Fore.GREEN + letter, end="")
            print(Style.RESET_ALL, end="")
    print("\n")

with open("Wordle/words.txt", "r") as file:
    all_words = file.read().splitlines()

word = choice(all_words)
word = "clone"
word_letters = list(word)
duplicates = check_duplicates(word)

print(duplicates)

for attempt_number in range(5):
    guess = input(f"Attempt Number {attempt_number+1} Guess: ").lower()
    guess_letters = list(guess)
    results = analyze_guess(guess_letters, duplicates)
    display_results(guess_letters, results)
    if results == [1, 1, 1, 1, 1]:
        break
print(word)