import pytest
@pytest.fixture()
def setup_fixtures ():
    print ("run set up fixtures")
    yield
    print ("run tear down fixture")

def setup_function(function):
    print ("this is set up function")


def test_01(setup_fixtures):
    print ("print test_01 function")

def test_02():
    print ("print test 02 function")

def test_03():
    print ("print test 03 function")

