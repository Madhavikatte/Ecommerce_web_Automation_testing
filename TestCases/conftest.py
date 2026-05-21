from selenium import webdriver
# import pytest
#
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os



@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        options = ChromeOptions()
        if os.environ.get("CI"):          # Only headless on GitHub Actions
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

    elif browser == 'firefox':
        options = FirefoxOptions()
        if os.environ.get("CI"):          # Only headless on GitHub Actions
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    else:
        driver = webdriver.Chrome()       # Default fallback
    driver.implicitly_wait(10)
    yield driver  # hands driver to the test
    driver.quit()  # runs after every test automatically


# #### Generate HTML Report ####
# 
# it is a hook for adding environment info to HTML report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome=yield
    report=outcome.get_result()

    if report.when == call and report.failed:
        print("test failed")

        driver=item.funcargs['driver']
        driver.save_screenshot('Screenshot/failure.png')



import logging

# log generation configuration
@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    logger = logging.getLogger("TestLogger")
    logger.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    fh = logging.FileHandler("test.log")
    fh.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger


@pytest.fixture(scope="function")
def logger(configure_logging):
    return configure_logging

@pytest.fixture(scope="function")
def logger(configure_logging):
    return configure_logging

@pytest.fixture(scope="function")
def login():
    driver=webdriver.Chrome()
    driver.get("https://admin-demo.nopcommerce.com/")

#enter username
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(By.XPATH, '//*[@id="Email"]'))
    element.send_keys("admin@yourstore.com")
#enter password
    driver.find_element(By.ID,"Password").send_keys("admin")
#click on login
    driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div/div[2]/div[1]/div/form/div[3]/button').click()

    yield(driver)
    driver.close()


