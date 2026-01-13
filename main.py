def read_word_file(filename):
    word_list = []
    try:
        with open(filename) as filename:
            for line in filename:
                line = line.strip()
                word_list.append(line)
    except FileNotFoundError:
        print("File not found")
    print(word_list)
    return word_list


if __name__ == '__main__':
    read_word_file('words.txt')
