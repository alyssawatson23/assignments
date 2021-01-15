# 2.8

def unscramble(letters):
    with open('wordlist.txt', 'r') as file:
        dictionary = [line.strip() for line in file]
        matches = []
        for word in dictionary:
            if len(word) == len(letters):
                if sorted(word) == sorted(letters):
                    matches.append(word)
        print(matches)


unscramble("eilnst")
