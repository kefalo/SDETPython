from selenium import webdriver
from selenium.webdriver.common.by import By

class Creation():

    driver = webdriver.Chrome()
    webPage = "https://gallery-app.vivifyideas.com/"

    def __init__(self):
        print("Inicializing")

    def login(self):
        self.driver.maximize_window()
        self.driver.get(self.webPage)
        self.driver.find_element(By.XPATH, "//html//body//div[1]//div[1]//nav//div//ul[2]//li[1]//a").click()

    def login_form(self):
        email = "email"
        password = "password"
        submit_button = "//html//body//div[1]//div[2]//div//form//button"

        self.driver.find_element(By.ID, email).send_keys("stefan@test.com")
        self.driver.find_element(By.ID, password).send_keys("Testtest1")
        self.driver.find_element(By.XPATH, submit_button ).click()
        #self.driver.set_page_load_timeout(30)

    def createThe_gallery(self):
        createButton_className = "nav-link nav-buttons"
        url_input = "//html//body//div[1]//div[2]//div//div//form//div[3]//div//div//input"
        add_button = "//html//body//div[1]//div[2]//div//div//form//div[3]//button"
        submitCreation_button = "//html//body//div[1]//div[2]//div//div//form//button[1]"
        title = "title"
        description = "description"


        self.driver.find_element(By.PARTIAL_LINK_TEXT, "//create").click()
        self.driver.find_element(By.ID,title ).send_keys("Test01")
        self.driver.find_element(By.ID,description ).send_keys("Random Description01")
        self.driver.find_element(By.XPATH, url_input ).send_keys("https://autoblog.rs/gallery/108/196865-bmw%20m5%2022.jpg")
        self.driver.find_element(By.XPATH, add_button).click()
        self.driver.find_element(By.XPATH, submitCreation_button ).click()

creation = Creation()
creation.login()
print("Login Page loaded successfully")
creation.login_form()
print("User successfully loaded into app")
creation.createThe_gallery()
print("Gallery Successfully Created")