def read_word_count(filename):
    file = open(filename, 'r')

    word_count = 0
    for line in file:
        line.strip()
        words = line.split(' ')
        word_count += len(words)

    return word_count