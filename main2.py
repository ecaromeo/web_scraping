from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.youtube.com/watch?v=lUzSsX4T4WQ")

# assert "Psychotic" in driver.title

# continue_link = driver.find_element_by_tag_name('a')
# elems = driver.find_element("tag", "a")
elems = driver.find_elements(By.TAG_NAME, "a")
for elem in elems:
    href = driver.get(elem.get_attribute('href'))
    if href is not None:
        print(href)