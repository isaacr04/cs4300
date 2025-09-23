from homework1.src.task5 import favorite_books, slice_list, make_students

def test_slice_list(capsys):
    slice_list(favorite_books)
    capture = capsys.readouterr()
    assert capture.out == ("[('Mother of Learning', 'Domagoj Kurmaić'), "
                           "('The Light of All That Falls', 'James Islington'), "
                           "('Golden Son', 'Pierce Brown')]\n")
    with capsys.disabled():
        print('| Output: ' + capture.out, end='')


def test_make_students():
    assert make_students() == {0: 'John C.', 1: 'Emily T.', 2: 'Laura K.', 3: 'Megan S.'}