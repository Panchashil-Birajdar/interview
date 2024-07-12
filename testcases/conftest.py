import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    driver=webdriver.Firefox()
    driver.get('https://automation.credence.in/login')
    yield driver
    driver.quit()


@pytest.fixture(params=[
    ("anuu@gmail.com","9421377331@Ppb","Login_Pass"),
    ("anuu@gmail1.com","9421377331@Ppb","Login_Fail"),
    ("anuu@gmail.com","9421377331@Ppb1","Login_Fail"),
    ("anuu@gmail.com1","9421377331@Ppb1","Login_Fail"),
])
def getDataForLogin(request):
    return request.param




# pytest -v -s --html=HtmlReports/Report.html
























