from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.RegistrationPage import Registration_Class

class Test_User_Profile:

    def test_UserRegistration_001(self):
        # 1 Browser Open
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.ur = Registration_Class(self.driver)
        # 2 Go to registration url
        self.driver.get("https://automation.credence.in/register")

        # 3 Enter Name
        #driver.find_element(By.ID, 'name').send_keys("Rohit")
        self.ur.Enter_Name("Rohit")

        # 4 Enter EMail Id
        #self.driver.find_element(By.ID, 'email').send_keys("Rohit3442@credence.in")
        self.ur.Enter_Email("Rohits1@credence.in")


        # 5 Enter Password
        #self.driver.find_element(By.ID, 'password').send_keys("rohit@123")
        self.ur.Enter_Password("Rohit1234")

        # 6 Enter Confirm Password
        #self.driver.find_element(By.ID, "password-confirm").send_keys("rohit@123")
        self.ur.Enter_ConfirmPassword("Rohit1234")


        # 7 Click on Register button
        #self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        self.ur.Click_RegisterButton()

        # 7 Validate Registration
        # try:
        #     self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
        #     print("Registration Pass")
        #     assert True
        # except:
        #     print("Registration Fail")
        #     assert False

        if self.ur.Validate_Registration() == "Registration Pass":
            assert True
        else:
            assert False



    # def test_UserLogin_002(self):
    #
    #     # 1 Browser Open
    #
    #     driver = webdriver.Chrome()
    #     # 2 Go to Url https://automation.credence.in/login
    #     driver.get("https://automation.credence.in/login")
    #
    #     # 3 Enter email
    #     driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Rohit344@credence.in")
    #     # 4 Enter Password
    #     driver.find_element(By.XPATH, "//input[@id='password']").send_keys("rohit@123")
    #     # 5 Click on Login button
    #     driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    #     # 6 Validate Login
    #     try:
    #         driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
    #         print("Login Pass")
    #         assert True
    #     except:
    #         print("Login Fail")
    #         assert False
