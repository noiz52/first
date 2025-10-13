import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_addition():
    """Проверка, что сумма чисел корректно отображается"""
    options = Options()
    options.add_argument("--headless")           
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("http://89.169.2.19:8080")        


    input1 = driver.find_element(By.CSS_SELECTOR, "[data-testid='input1']")
    input2 = driver.find_element(By.CSS_SELECTOR, "[data-testid='input2']")
    button = driver.find_element(By.CSS_SELECTOR, "[data-testid='button']")
    result = driver.find_element(By.CSS_SELECTOR, "[data-testid='result']")


    input1.clear()
    input1.send_keys("5")
    input2.clear()
    input2.send_keys("3")
    button.click()

    time.sleep(1)  

    assert result.text.strip() == "8", f"Ожидали 8, получили {result.text}"
    driver.quit()
