from selenium.webdriver.common.by import By

class Flights_options_page_locators:
    #Locators
    WINDOW_BUTTON = (By.XPATH, "//div/button[@class = 'button buttonSecondry buttonBig fontSize12 relative']")
    AIRLINES_OPTIONS = (By.CSS_SELECTOR, "#listing-id .fli-list.simpleow")
    AIRLINES_NAME = (By.CSS_SELECTOR, ".boldFont.blackText.airlineName")
    FLIGHT_NAME = (By.CSS_SELECTOR, "p.fareNameHead")
    FLIGHT_PRICE = (By.CSS_SELECTOR, ".viewFareRowWrap .viewFareBtnCol .blackText")
    VIEW_PRICE_BUTTON = (By.CSS_SELECTOR, ".listingCard button")
    FLIGHT_LIST = (By.CSS_SELECTOR, "#listing-id #premEcon div div.fli-list .collapse.show .viewFareRowWrap")
    BOOK_NOW = (By.CSS_SELECTOR, ".button.corp-btn.latoBlack.buttonPrimary.fontSize13")
    def __init__(self, driver):
        self.driver = driver
    
    def click_on_window(self):
        """"
            Click on Pop up Window
        """
        # return self.driver.find_element(*Flights_options_page_locators.WINDOW_BUTTON).click() 
        check_window_status = self.driver.find_elements(*Flights_options_page_locators.WINDOW_BUTTON)
        print(len(check_window_status))
        return check_window_status
    
    def scroll_window(self):
        """"
            Scroll Window to desire place
        """
        self.driver.execute_script("window.scrollBy(0, 300)")

    # def get_flight_name(self):
    #     print("your flight name")
    #     flight = self.driver.find_element(*Flights_options_page_locators.FLIGHT_NAME)
    #     flight_name = flight.text
    #     print(flight_name)
    #     return flight_name
    
    # def click_on_view_price(self):
    #     return self.driver.find_element(*Flights_options_page_locators.VIEW_PRICE_BUTTON).click() 
    
    def get_airlines_name_click_on_viewprice(self, airline_index) -> list:
        """"
            Get all available Airlines name,
            click on View Price button of desired airline index
            :return: (list) - name of all airlines
        """
        print("airlines list")
        airlines = []
        i = 0
        airlines_list = self.driver.find_elements(*Flights_options_page_locators.AIRLINES_OPTIONS)
        print(len(airlines_list))
        for each_airlines in airlines_list:
            airlines_names = each_airlines.find_element(*Flights_options_page_locators.AIRLINES_NAME).text
            airlines.append(airlines_names)
            i = i + 1
            if i == airline_index:
                print(i)
                # aireach_airlines.find_element(*Flights_options_page_locators.VIEW_PRICE_BUTTON).text
                each_airlines.find_element(*Flights_options_page_locators.VIEW_PRICE_BUTTON).click()
        return airlines

    
    
    def get_flight_list_click_on_booknow(self, flight_index) -> list:
        """"
            Get all available Flight name and related price,
            click on Book now button of desired flight_index
            :return: (list, list) - (name of flights, price of flights)
        """
        print("flight list")
        name = []
        price = []
        flight_list = self.driver.find_elements(*Flights_options_page_locators.FLIGHT_LIST)
        print(len(flight_list))
        i=0
        for flight in flight_list:
            flight_name = flight.find_element(*Flights_options_page_locators.FLIGHT_NAME).text
            print(flight_name)
            name.append(flight_name)
            flight_price = flight.find_element(*Flights_options_page_locators.FLIGHT_PRICE).text
            price.append(flight_price)
            i = i + 1
            if i == flight_index:
                print("click on buy now")
                print(i)
                flight.find_element(*Flights_options_page_locators.BOOK_NOW).click()
        return name, price










    # def click_on_book_now(self):
    #     print("aaaa")
    #     return self.driver.find_element(*Flights_options_page_locators.BOOK_NOW).click()

    
    










# //div/button[@class = 'button buttonSecondry buttonBig fontSize12 relative']
#//button[@id = 'bookbutton-RKEY:337b569f-ac69-42fe-985b-d041d8bb0004:25_0']/span[@class = 'appendRight8']
# listing-id .fli-list.simpleow .listingCard button