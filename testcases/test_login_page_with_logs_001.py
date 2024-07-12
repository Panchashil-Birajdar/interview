from pageObjects.loginPage import LoginClass
from utilities.Logger import LoggingClass


class Test_Credkart_Login:
    Email = 'anuu@gmail.com'
    Password = '9421377331@Ppb'
    log = LoggingClass.log_generator()

    def test_user_login_001(self,setup):
        self.driver=setup
        self.lg=LoginClass(self.driver)

        self.log.info('Enter Email ='+self.Email)
        self.lg.Enter_Email(self.Email)
        self.log.info('Enter Password ='+self.Password)
        self.lg.Enter_Password(self.Password)
        self.log.info('Click on login button')
        self.lg.Click_Login_Button()

        if self.lg.Verify_Login()=='pass':
            self.log.info('Login testcase test_user_login_001 is pass')
            self.log.info('Taking Screenshot')
            self.driver.save_screenshot("D:\\Credence\\Assignments\\My Assignments\\Final Revision\\Interview1\\Screenshots\\test_user_login_001_pass.PNG")
            assert True
        else:
            self.log.info('Login testcase test_user_login_001 is fail')
            self.log.info('Taking Screenshot')
            self.driver.save_screenshot("D:\\Credence\\Assignments\\My Assignments\\Final Revision\\Interview1\\Screenshots\\test_user_login_001_fail.PNG")
            assert False














































