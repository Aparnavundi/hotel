import pytest
from selenium import webdriver
from Library.configuration import Configuration


# elif request.param == "Edge":
#      driver = webdriver.Edge(executable_path=Configuration.MSEDGE_PATH)

@pytest.fixture(params=["Chrome"])
def init_driver(request):
    global driver
    # browser = request.param

    if request.param == "Chrome":
        driver = webdriver.Chrome(executable_path=Configuration.CHROME_PATH)




    driver.get(Configuration.URL)
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    driver.quit()
