word = input()

word_list = []

for i in range(len(word) - 2):
    for j in range(i + 1, len(word) - 1):
        first = word[:i+1]
        middle = word[i+1:j+1]
        last = word[j+1:]
        
        reversed_word = first[::-1] + middle[::-1] + last[::-1]
        word_list.append(reversed_word)
        
        
word_list.sort()
print(word_list[0])