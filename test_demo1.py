#Any pytest file should start with test_ or end with _test
#pytest method names should start with test
#any code must be in method
import pytest

#@pytest.mark.skip 
def test_firstProgram(setup):
    print("Hello")
 
@pytest.mark.smoke  
@pytest.mark.xfail 
def test_secondProgram():
    msg = "Hello"
    assert msg == "Hi"
    
#@pytest.mark.usefixtures
def test_crossBrowser(crossBrowser):
    print(crossBrowser)