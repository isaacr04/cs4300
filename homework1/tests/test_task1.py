from homework1.src.task1 import helloworld

def test_helloworld(capsys):
    helloworld()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
    with capsys.disabled():
        print('| Output: ' + captured.out, end='')
