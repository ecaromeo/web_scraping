from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver = webdriver.Firefox()
driver.get("https://www.youtube.com/watch?v=lUzSsX4T4WQ")

# assert "Psychotic" in driver.title

# continue_link = driver.find_element_by_tag_name('a')
# elems = driver.find_elements(By.XPATH, "//a[@href]")
# elems = driver.find_elements(By.XPATH, "//ytd-text-inline-expander")
elem = driver.find_element(By.ID, "description")
elem.click()
elems = driver.find_element(By.CLASS_NAME, "yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap")
# for elem in elems:
print('ok')
print(elems)