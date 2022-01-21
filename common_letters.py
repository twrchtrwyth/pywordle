import json

f = open("words_dictionary.json")

words = json.load(f)
letters = {}
for word in words.keys():
    if len(word) == 5:
        if word.isalpha():
            for letter in word:
                if letter in letters.keys():
                    letters[letter] += 1
                else:
                    letters[letter] = 1
    else:
        pass
total_letters = 0
for value in letters.values():
    total_letters += value
letters = sorted(letters.items(), key=lambda item: item[1], reverse=True)
print("\nLetter Frequency in Five-Letter Words")
print("-------------------------------------")
print(f"{'Letter' : >20}{'Occurrences' : >15}{'Percentage' : >15}")
position = 1
for letter, total in letters:
    print(f"{f'{position}.' : >10}{letter.upper() : >10}{total : >15}{round(total/total_letters*100, 1) : >15}")
    position += 1
