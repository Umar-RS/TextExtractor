import pythonTask
import pathlib

def test_check_prefix():
    test = pythonTask.TextExtractor("www.google.com")
    url = test.check_prefix()
    assert "https://" in url

def test_get_content():
    test = pythonTask.TextExtractor("https://www.google.com")
    content = test.get_content()
    assert content != ''

def test_output_file():
    test = pythonTask.TextExtractor("https://www.google.com")
    test.get_content()
    test.output_file()
    path = pathlib.Path('file.txt')
    assert path.exists() == True