import os
from selenium import webdriver
from selenium.webdriver.common.by import By

LINKEDIN_URL = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
PYTHON_JOB_SEARCH_QUERY = "https://www.linkedin.com/jobs/search/?currentJobId=3550859748&f_AL=true&f_WT=2&geoId=103644278&keywords=python%20developer&location=United%20States&refresh=true&sortBy=DD"
LINKEDIN_USERNAME = os.environ.get("LINKEDIN_USERNAME")
LINKEDIN_PASSWORD = os.environ.get("LINKEDIN_PASSWORD")

driver = webdriver.Chrome()
driver.get(LINKEDIN_URL)

username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.CSS_SELECTOR, "button")

username_field.send_keys(LINKEDIN_USERNAME)
password_field.send_keys(LINKEDIN_PASSWORD)
login_button.click()

# the following line keeps the browser open after the script runs
keyword = input("enter a character or press enter to continue")

driver.quit()
