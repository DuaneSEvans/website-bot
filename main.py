import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from decouple import config

EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")
PATH = "./chromedriver"
driver = webdriver.Chrome(
    "/Users/duaneevans/programming/website-bot/chromedriver")
driver.implicitly_wait(6)

# Wodify IDs


class WebSiteIDs:
    EMAIL = "Input_UserName"
    PASSWORD = "Input_Password"
    CALENDAR_TAB = (
        "AthleteTheme_wtLayoutNormal_block_wtMenu_AthleteTheme_wt67_block_wt38"
    )
    DATE_PICKER = "AthleteTheme_wt6_block_wtMainContent_wt9_W_Utils_UI_wt216_block_wtDateInputFrom"
    TABLE = "AthleteTheme_wt6_block_wtMainContent_wt9_wtClassTable"
    BLANK_SPACE = "AthleteTheme_wt6_block_wtTitle"
    REGISTER_7AM = "AthleteTheme_wt6_block_wtMainContent_wt9_wtClassTable_ctl06_AthleteTheme_wt221_block_wtIconSvg_Svg"
    FILTER_DROPDOWN = "AthleteTheme_wt6_block_wtMainContent_wt9_wt157"


# Start Script
# Open webpage
driver.get("https://app.wodify.com/")
print(driver.title)

# Login
userNameField = driver.find_element(By.ID, WebSiteIDs.EMAIL)
userNameField.send_keys(EMAIL)
passwordField = driver.find_element(By.ID, WebSiteIDs.PASSWORD)
passwordField.send_keys(PASSWORD)
passwordField.send_keys(Keys.RETURN)

# Go to Calendar
calendarTab = driver.find_element(By.ID, WebSiteIDs.CALENDAR_TAB)
ActionChains(driver).move_to_element(calendarTab).click(calendarTab).perform()

# Select Day
datePicker = driver.find_element(By.ID, WebSiteIDs.DATE_PICKER)
ActionChains(driver).move_to_element(datePicker).click(datePicker).send_keys(
    Keys.ARROW_RIGHT
).send_keys(Keys.ARROW_RIGHT).click(datePicker).perform()

# Click blankspace otherwise the datepicker annoyingly pops up again
blankSpace = driver.find_element(By.ID, WebSiteIDs.BLANK_SPACE)
ActionChains(driver).move_to_element(blankSpace).click(blankSpace).perform()

# Register for 3rd event down from the top (hope it is always 7am)
registerButton = driver.find_element(By.ID, WebSiteIDs.REGISTER_7AM)
ActionChains(driver).move_to_element(
    registerButton).click(registerButton).perform()
time.sleep(3)

driver.quit()
