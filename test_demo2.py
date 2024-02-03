#Any pytest file should start with test_ or end with _test
#pytest method names should start with test
#any code must be in method
#to run in cmd pytest -v -s // pytest test.py -v -s // pytest -k name -v -s // pytest -m markname -v -s
#-k for method names execution, -s log in output, -v stands for more info
#-m is for mark test item @pytest.mark.markname
#You can skip test with @pytest.mark.skip
#You can prevent output from showing error by using @pytest.mark.xfail
#fixtures are used as setup and teardown methods for test cases - conftest ffile are to generalize fixture and make it available to all test cases


import pytest

@pytest.mark.smoke
def test_thirdProgram():
    print("Good Morning")
    
