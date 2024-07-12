from selenium.webdriver.common.by import By


class   LoginClass:
    text_email_xpath = (By.XPATH,"//input[@id='email']")
    text_password_xpath = (By.XPATH,"//input[@id='password']")
    click_login_button = (By.XPATH,"//button[@type='submit']")
    verify_login_xpath = (By.XPATH,"//h2[normalize-space()='CredKart']")

    def __init__(self,driver):
        self.driver = driver

    def Enter_Email(self,email):
        self.driver.find_element(*LoginClass.text_email_xpath).send_keys(email)

    def Enter_Password(self,password):
        self.driver.find_element(*LoginClass.text_password_xpath).send_keys(password)

    def Click_Login_Button(self):
        self.driver.find_element(*LoginClass.click_login_button).click()

    def Verify_Login(self):
        try:
            self.driver.find_element(*LoginClass.verify_login_xpath)
            return "pass"
        except:
            return "fail"









































