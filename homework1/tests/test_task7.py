from homework1.src.task7 import request_example

def test_request_example(capsys):
    request_example()
    capture = capsys.readouterr()
    assert capture.out == '''This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.\n'''
    with capsys.disabled():
        print('| Output: ' + capture.out, end='')