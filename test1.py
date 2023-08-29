from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Python"))
     )
except:
    driver.quit()

x = driver.find_element(By.LINK_TEXT, "Python")
driver.execute_script("arguments[0].click();", x)
time.sleep(10)
# Find an element by its ID and interact with it

# Close the browser
driver.quit()