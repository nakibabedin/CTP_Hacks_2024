from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://www1.cuny.edu/mu/cunyverse/2023/01/12/relieving-stress-through-yoga-at-cuny/")

# Wait for the page to fully load
driver.implicitly_wait(7)  

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
body_text = soup.body.get_text(separator='\n', strip=True)

print(body_text)

driver.quit()
