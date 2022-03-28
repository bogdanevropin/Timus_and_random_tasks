

unique_words = set()
dictionary = {}

try:
    with open('text.txt', 'r') as text_file:
        for line in text_file:
            split_line = line.replace('.', '')
            split_line = split_line.replace("(", '')
            split_line = split_line.replace(")", '')
            split_line = split_line.replace("?", '')
            split_line = split_line.replace("!", '')
            split_line = split_line.split()
            for words in split_line:
                unique_words.add(words)
except IOError:
    print("No input file")

for u_word in unique_words:
    dictionary[u_word] = 0

try:
    with open('text.txt', 'r') as text_file:
        for line in text_file:
            split_line = line.replace('.', '')
            split_line = split_line.replace("(", '')
            split_line = split_line.replace(")", '')
            split_line = split_line.replace("?", '')
            split_line = split_line.replace("!", '')
            split_line = split_line.split()
            for word in split_line:
                dictionary[word] += 1

except IOError:
    print("No input file")

print(dictionary)