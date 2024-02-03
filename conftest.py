import pytest

@pytest.fixture(scope="class")
def setup():
    print("I will be execute first")
    yield
    print("I will be execute last")
    
@pytest.fixture()
def dataLoad():
    print("user profile data is being created!")
    return["Alejandra","Evander","alejandra.evander@gmail.com"]

@pytest.fixture(params=[("chrome","Rahul"),"firefox","IE"]) #incase multiple data to pass use tuple
def crossBrowser(request):
    return request.param