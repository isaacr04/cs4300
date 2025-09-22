from homework1.src.task6 import read_word_count

filepath = 'src/task6_readme.txt'

# task6_readme.txt has 104 words
def test_read_word_count():
    assert read_word_count(filepath) == 104