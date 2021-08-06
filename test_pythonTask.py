import pythonTask
import pytest
import argparse

def test_create_parser():# create parser and add the argument "url" which is parsed through to the script
    args = pythonTask.create_parser()
    assert len(vars(args)) == 1

@pytest.fixture
def create_parser():
    parser = argparse.ArgumentParser()  
    parser.add_argument("url")
    args = parser.parse_args()
    return args


def test_check_prefix(create_parser):
    create_parser.url = pythonTask.check_prefix()
    assert "https://" in create_parser.url == True