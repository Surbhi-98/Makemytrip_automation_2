import time
from selenium.webdriver.common.by import By

class Flight_description_page_locators:
    #Locators
    # (//span[@class='box'])[1]
    ARROW_BUTTON = (By.XPATH, "//button[@class='sliderNextBtn']")
    RADIO_BUTTON = (By.XPATH, "//b[normalize-space()='Yes, Secure my trip.']")
    # ADULT_BUTTON = (By.XPATH, "//button[@class='addTravellerBtn']")
    ADULT_BUTTON = (By.XPATH, "//div[@class='otherList']//button[normalize-space()='+ ADD NEW ADULT']")
    ADULT_BOX = (By.XPATH, "//label[@for='text']//span[@class='box']")
    # ADULT_BUTTON = (By.XPATH, "//label[@for='text']//span[@class='customCheckbox']//span[@class='box']//span[@class='check']")
    MOBILE_NUMBER = (By.XPATH, "//input[@placeholder = 'Mobile No']")
    EMAIL = (By.XPATH, "//input[@placeholder = 'Email']")
    SELECT_EMAIL = (By.CSS_SELECTOR, ".emailId")
    FIRST_NAME = (By.XPATH, "//input[@placeholder='First & Middle Name']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='Last Name']")
    GENDER = (By.XPATH, "//label[2]")
    GST_CHECK = (By.XPATH, "//div[@id='gstDetails']//span[contains(@class,'customCheckbox')]//span[contains(@class,'box')]")
    COMPANY_NAME = (By.XPATH, "//input[@placeholder='Company Name']")
    GST_NUMBER = (By.XPATH, "//input[@placeholder='Registration No']")
    CONFIRM_BUTTON = (By.XPATH, "//button[normalize-space()='CONFIRM']")
    CONTINUE_BUTTON = (By.XPATH, "//button[normalize-space()='Continue']")
    POPUP = (By.XPATH, "//button[normalize-space()='Yes, Please']")
    # SELECT_MEAL = (By.XPATH, "//span[normalize-space()='Meals']")
    SELECT_MEAL = (By.XPATH, "//li//span[normalize-space()='Meals']")
    SEAT_CONTINUE_BUTTON = (By.XPATH, "//div//button[normalize-space()='Continue']")
    # CONTINUE_ANYWAY = (By.XPATH, "//button[normalize-space()='CONTINUE ANYWAY']")
    # CONTINUE_ANYWAY = (By.XPATH, "//button[normalize-space()='CONTINUE']")
    CONTINUE_ANYWAY = (By.XPATH, "//button[@class = 'reviewAddonsBtn']")
    PROCEED_TO_PAY = (By.XPATH, "//button[normalize-space()='Proceed to pay']")

    def __init__(self, driver):
        self.driver = driver
    
    def switch_to_new_tab(self):
        """"
        Switch to a new tab
        """
        windows_open = self.driver.window_handles
        return self.driver.switch_to.window(windows_open[1])
    
    def scroll_to_location(self):
        """"
            Scroll to desired location
        """
        # self.driver.execute_script("window.scrollBy(0, 1650)")
        self.driver.execute_script("window.scrollBy(0, 1700)")

    def click_on_radio_button(self):
        """"
            Click on radio button
        """
        return self.driver.find_element(*Flight_description_page_locators.RADIO_BUTTON).click()
    
    def check_new_adult(self):
        """"
            Check box for adult button
        """
        check_adult_status = self.driver.find_elements(*Flight_description_page_locators.ADULT_BOX)
        print("check new adult" + str(len(check_adult_status)))
        return check_adult_status
    
    def add_new_adult(self):
        """"
            Click on add new adult button
        """
        # time.sleep(1)
        return self.driver.find_element(*Flight_description_page_locators.ADULT_BUTTON).click()
    
    def enter_first_name(self):
        """"
            Enter first name
        """
        return self.driver.find_element(*Flight_description_page_locators.FIRST_NAME).send_keys("Avantika")
    
    def enter_last_name(self):
        """"
            Enter last name
        """
        return self.driver.find_element(*Flight_description_page_locators.LAST_NAME).send_keys("sharma")
    
    def select_gender(self):
        """"
            Select gender
        """
        return self.driver.find_element(*Flight_description_page_locators.GENDER).click()
    
    def enter_mobile_number(self):
        """"
            Enter Mobile number
        """
        return self.driver.find_element(*Flight_description_page_locators.MOBILE_NUMBER).send_keys("9876543210")
    
    def enter_email(self):
        """"
            Enter Email id
        """
        self.driver.find_element(*Flight_description_page_locators.EMAIL).send_keys("nice@gmail.com")
        return self.driver.find_element(*Flight_description_page_locators.SELECT_EMAIL).click()
    
    def check_gst(self):
        """"
            click on check box of gst
        """
        return self.driver.find_element(*Flight_description_page_locators.GST_CHECK).click()
    
    def enter_company_name(self):
        """"
            Enter company name
        """
        return self.driver.find_element(*Flight_description_page_locators.COMPANY_NAME).send_keys("CBNITS")
    
    def enter_gst_number(self):
        """"
            Enter GST number
        """
        return self.driver.find_element(*Flight_description_page_locators.GST_NUMBER).send_keys("07AAGFF2194N1Z1")
    
    def click_on_confirm_button(self):
        """"
            Click on Confirm button
        """
        return self.driver.find_element(*Flight_description_page_locators.CONFIRM_BUTTON).click()
    
    def click_on_continue_button(self):
        """"
            Click on Continue button
        """
        return self.driver.find_element(*Flight_description_page_locators.CONTINUE_BUTTON).click()

    def click_on_popup(self):
        """"
            Click on Button of popup window
        """
        return self.driver.find_element(*Flight_description_page_locators.POPUP).click()
    
    def click_on_meal(self):
        """"
            Click on meal option
        """
        # return self.driver.find_element(*Flight_description_page_locators.SELECT_MEAL).click()
        check_meal_status = self.driver.find_elements(*Flight_description_page_locators.SELECT_MEAL)
        print(len(check_meal_status))
        return check_meal_status

    def click_on_meal_arrow_button(self):
        """"
            Click on meal arrow_button
        """
        # return self.driver.find_element(*Flight_description_page_locators.SELECT_MEAL).click()
        arrow_meal_button_status = self.driver.find_elements(*Flight_description_page_locators.ARROW_BUTTON)
        print(len(arrow_meal_button_status))
        return arrow_meal_button_status

    def click_on_seat_continue_button(self):
        """"
            Click on Continue button after selecting seat
        """
        return self.driver.find_element(*Flight_description_page_locators.SEAT_CONTINUE_BUTTON).click()
    
    def click_on_continue_anyway_button(self):
        """"
            Click on Continue anyway button of popup window
        """
        # return self.driver.find_element(*Flight_description_page_locators.CONTINUE_ANYWAY).click()
        check_continue_anyway = self.driver.find_elements(*Flight_description_page_locators.CONTINUE_ANYWAY)
        print(len(check_continue_anyway))
        return check_continue_anyway

    def scroll_to_bottom(self):
        """"
            Scroll to Bottom of the page
        """
        return self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

    def click_on_proceed_to_pay_button(self):
        """"
            Click on proceed to pay button
        """
        return self.driver.find_element(*Flight_description_page_locators.PROCEED_TO_PAY).click()

    def close_new_tab(self):
        """"
        Close new tab
        """
        self.driver.close()
        windows_open = self.driver.window_handles
        return self.driver.switch_to.window(windows_open[0])

    
    
