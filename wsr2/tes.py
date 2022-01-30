from aws_synthetics.selenium import synthetics_webdriver as webdriver
from aws_synthetics.common import synthetics_logger as logger

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from aws_synthetics.common import synthetics_configuration

synthetics_configuration.set_config(
    {
        "screenshot_on_step_start": False,
        "screenshot_on_step_success": True,
        "screenshot_on_step_failure": True,
    }
)

waitTime = 2


async def joinJourney50():
    base_url = "https://www.virginmedia.com/my-virgin-media/home"
    # declare and initialize driver variable
    driver = webdriver.Chrome()
    # browser should be loaded in maximized window
    driver.maximize_window()
    # driver should wait implicitly for a given duration, for the element under consideration to load.
    # to enforce this setting we will use builtin implicitly_wait() function of our 'driver' object.
    driver.implicitly_wait(10)  # 10 is in seconds
    # to load a given URL in browser window

    def click_element(driver, locator, selector):
        WebDriverWait(driver, waitTime).until(
            EC.element_to_be_clickable((locator, selector))
        ).click()

    def page_has_loaded(driver):
        page_state = driver.execute_script("return document.readyState;")
        return page_state == "complete"

    def home_page():
        driver.get(base_url)

    await webdriver.execute_step("Click_virginmediaBroadbandLoadingTime_1", home_page)

    def accept_prompt():
        try:
            driver.find_element_by_id("consent_prompt_submit").click()
        except:
            pass
        page_has_loaded(driver)

    await webdriver.execute_step("Click_Cookie_Prompt", accept_prompt)


 


  
    driver.quit()       


async def handler(event, context):
    return await joinJourney50()