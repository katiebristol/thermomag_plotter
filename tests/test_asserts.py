import pytest
import sys, os

sys.path.append(os.path.join(
    os.path.dirname(__file__),
    "../"))

from src import plotting

plotting.plot()

def hello():
    return "Hello World"

def test_hello():
    assert(hello() == "Hello World")