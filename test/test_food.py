from selenium import webdriver
from selenium.webdriver.common.by import By
def test_start_page():
  driver = webdriver.Chrome()
  driver.get("https://nanavions.github.io/food.html")
  assert driver.title == "Рецепт бутерброда"
  assert driver.find_element(By.TAG_NAME, "h1").text == "Простой бутерброд с сыром 🍞🧀"
  assert driver.find_element(By.TAG_NAME, "h2").text == "Что нужно:"
  assert driver.find_element(By.ID, "p").text == "Хлеб, сливочное масло, сыр, зелень (по желанию)"
  assert driver.find_element(By.TAG_NAME, "h2").text == "Как приготовить:"
  assert driver.find_element(By.ID, "p1").text == "1. Намажьте хлеб маслом. 🍞🧈"
  assert driver.find_element(By.ID, "p2").text == "2. Положите сверху ломтик сыра. 🧀 "
  assert driver.find_element(By.ID, "p3").text == " 3. Добавьте зелень, если хотите. 🥬"
  assert driver.find_element(By.ID, "p4").text == " 4. Бутерброд готов! 🥳"
  driver.quit()
