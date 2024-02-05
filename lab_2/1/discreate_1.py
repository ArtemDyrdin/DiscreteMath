word = "КОМБИНАТОРИКА"
letters_number = len(word)

words_number = 0

wordSet = set()

for i in range(letters_number):
    for j in range(letters_number):
        if i != j:
            for k in range(letters_number):
                if k != i and k != j:
                    for l in range(letters_number):
                        if l != i and l != j and l != k:
                            current_word = word[i] + word[j] + word[k] + word[l]
                            if current_word not in wordSet:
                                wordSet.add(current_word)
                                print(current_word, i, j, k, l)
                                words_number += 1

print(f'Количество различных слов из 4-х букв - {words_number}')
