from pageObjects.loginPage import LoginClass
from utilities.Logger import LoggingClass


class Test_Credkart_Login:
    log = LoggingClass.log_generator()

    def test_user_login_params_002(self,setup,getDataForLogin):
        self.driver=setup
        self.lg=LoginClass(self.driver)

        self.log.info('Testcase test_user_login_params_002 is Started')
        self.log.info('Enter Email ='+getDataForLogin[0])
        self.lg.Enter_Email(getDataForLogin[0])
        self.log.info('Enter Password ='+getDataForLogin[1])
        self.lg.Enter_Password(getDataForLogin[1])
        self.log.info('Click on login button')
        self.lg.Click_Login_Button()

        if getDataForLogin[2]=="Login_Pass" and self.lg.Verify_Login()=='pass':
           assert True
        elif getDataForLogin[2]=="Login_Fail" and self.lg.Verify_Login()=='pass':
            assert False
        elif getDataForLogin[2]=="Login_Pass" and self.lg.Verify_Login()=='fail':
            assert False
        elif getDataForLogin[2]=="Login_Fail" and self.lg.Verify_Login()=='fail':
            assert True

        self.log.info('Testcase test_user_login_params_002 is completed\n')















































