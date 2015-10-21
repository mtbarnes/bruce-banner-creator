import utils
from functools import wraps
from nose.tools import assert_equals
from bruce import Bruce


def test_init():
    testfile = "test.jpg"
    testBruce = Bruce(testfile)
    assert testBruce.filenames == [testfile]
    testfiles = [testfile, testfile]
    testBruce = Bruce(testfiles)
    assert testBruce.filenames == testfiles
