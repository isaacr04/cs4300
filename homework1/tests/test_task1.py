from ..src.task1 import helloworld

def test_helloworld(capsys):
    helloworld()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
