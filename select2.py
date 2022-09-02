import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep


class TestTestselect():

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_testselect(self):
        self.driver.get("https://select2.org/selections")
        self.driver.set_window_size(1280, 680)

        assert "built-in-escaping" in self.driver.page_source # вариант через assert
        #title_text = self.driver.find_element(By.ID, "built-in-escaping")
        #if title_text == self.driver.find_element(By.ID, "built-in-escaping"):
            #print("Мы попали на страницу с текстом - Built-in escaping")
        #else:
            #print("Ошибка элемента")


        # первый селект
        self.driver.find_element(By.ID, "body-inner").click()
        self.driver.find_element(By.CSS_SELECTOR, ".select2-selection--single").click()
        self.driver.find_element(By.CSS_SELECTOR, ".select2-search--dropdown > .select2-search__field").click()
        self.driver.find_element(By.CSS_SELECTOR, ".select2-search--dropdown > .select2-search__field").send_keys(
            "California")
        self.driver.find_element(By.CSS_SELECTOR, ".select2-search--dropdown > .select2-search__field").send_keys(
            Keys.ENTER)
        self.driver.save_screenshot('screen1.png')

        # второй селект
        self.driver.find_element(By.CSS_SELECTOR, ".padding:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".select2-selection--multiple").click()
        self.driver.find_element(By.CSS_SELECTOR, ".select2-search__field").send_keys("Hawaii")
        self.driver.find_element(By.CSS_SELECTOR, ".select2-search__field").send_keys(Keys.ENTER)
        self.driver.save_screenshot('screen2.png')
        self.driver.find_element(By.LINK_TEXT, "internal representation of the selected option").click()
        self.driver.save_screenshot('screen3.png')
