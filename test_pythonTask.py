import pythonTask
import pytest
import argparse

def test_create_parser():
    args = pythonTask.create_parser()
    assert len(vars(args)) == 1

def test_check_prefix():
    url = pythonTask.check_prefix(url="")
    assert "https://" in url

