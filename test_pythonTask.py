import pythonTask
import pathlib

def test_create_parser():
    args = pythonTask.create_parser()
    assert len(vars(args)) == 1

def test_check_prefix():
    url = pythonTask.check_prefix(url="")
    assert "https://" in url

def test_create_and_output_file():
    pythonTask.create_and_output_file(url="https://www.google.com")
    path = pathlib.Path('file.txt')
    assert path.exists() == True