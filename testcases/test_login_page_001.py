from pageObjects.loginPage import LoginClass


class Test_Credkart_Login:
    Email = 'anuu@gmail.com'
    Password = '9421377331@Ppb'

    def test_user_login_001(self,setup):
        self.driver=setup
        self.lg=LoginClass(self.driver)

        self.lg.Enter_Email(self.Email)
        self.lg.Enter_Password(self.Password)
        self.lg.Click_Login_Button()

        if self.lg.Verify_Login()=='pass':
            assert True
        else:
            assert False














































