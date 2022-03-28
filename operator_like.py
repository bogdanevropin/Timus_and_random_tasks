

try:
    with open('like_text.txt', 'r') as text_file:
        number_of_templates = int(text_file.readline())
        print(number_of_templates)
        for line in text_file:
            list_line = [word for word in line.split()]
            print(list_line)
            for item_word in list_line:
                item_word = item_word[1: -1]
                print(item_word)

            like_chars = []
            for char_like in list_line[0]:
                like_chars.append(char_like)
            like_chars = like_chars[1: -1]
            print(like_chars)

            templates_chars = []
            for char_template in list_line[2]:
                templates_chars.append(char_template)
            templates_chars = templates_chars[1: -1]
            print(templates_chars)

except IOError:
    print("No input file")

