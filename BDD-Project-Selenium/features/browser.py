
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Browser:

    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver.get("https://the-internet.herokuapp.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def close(self):
        self.driver.quit()

    def get_current_url(self):
        return self.driver.current_url

    def get_abtesting(self):
        abtesting_elem_btn = (By.XPATH, '/html/body/div[2]/div/ul/li[1]/a')
        return self.driver.find_element(*abtesting_elem_btn)

    def get_infinite_scroll(self):
        infinite_scroll_btn = (By.XPATH, '/html/body/div[2]/div/ul/li[26]/a')
        return self.driver.find_element(*infinite_scroll_btn)

    def get_geolocation(self):
        geolocation_btn = (By.XPATH, '/html/body/div[2]/div/ul/li[23]/a')
        return self.driver.find_element(*geolocation_btn)

    def get_checkboxes_link(self):
        checkboxes_btn = (By.XPATH, '//*[@id="content"]/ul/li[6]/a')
        return self.driver.find_element(*checkboxes_btn)

    def get_form_authentication_link(self):
        form_authentication_selector = (By.XPATH, '//*[@href ="/login"]')
        return self.driver.find_element(*form_authentication_selector)

    def get_username_element(self):
        username_selector = (By.XPATH, '//*[@id="username"]')
        return self.driver.find_element(*username_selector)

    def get_password_element(self):
        password_selector = (By.XPATH, '//*[@id="password"]')
        return self.driver.find_element(*password_selector)

    def get_login_button(self):
        login_button = (By.XPATH, '//*[@id="login"]/button')
        return self.driver.find_element(*login_button)

    def get_alert_secure_area(self):
        alert_message = (By.XPATH, '//*[@id="flash"]')
        return self.driver.find_element(*alert_message)

    # def get_message_secure_area(self):
    #     secure_message = (By.XPATH, '//*[@class="subheader"]')
    #     return self.driver.find_element(*secure_message)

    def get_logout_bt(self):
        logout_bt = (By.XPATH, '//*[@id="content"]/div/a/i')
        return self.driver.find_element(*logout_bt)

    def get_logout_message(self):
        logout_message = (By.XPATH, '//*[@class="flash success"]')
        return self.driver.find_element(*logout_message)
