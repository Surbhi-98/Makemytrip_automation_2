from genericpath import isfile
import inspect
import logging
import os
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("driver_setup")
class BasePage:

    def wait_clickable(self, path):
        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(expected_conditions.element_to_be_clickable((path)))
        except Exception as e:
            self.message_logging(e)
    
    def wait_presence(self, path):
        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(expected_conditions.presence_of_element_located((path)))
        except Exception as e:
            self.message_logging(e)
        
    def taking_screen_short(self, file_name):
        path = "/home/cbnits/Documents/Makemytrip_Assignment/Screen_short/"+file_name
        if os.path.isfile(path):
            # print("true")
            os.remove(path)
        return self.driver.get_screenshot_as_file("/home/cbnits/Documents/Makemytrip_Assignment/Screen_short/"+file_name)
    
    def message_logging(self, message):
        """"
        Create Log File
        """
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler("/home/cbnits/Documents/Makemytrip_Assignment/Log/logfile.log", mode='a')
        logger.addHandler(filehandler)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        logger.info(message)
    
    def delete_log_file(self):
        file_path = "/home/cbnits/Documents/Makemytrip_Assignment/Log/logfile.log"
        if os.path.isfile(file_path):
            os.remove("/home/cbnits/Documents/Makemytrip_Assignment/Log/logfile.log")








            

# class Logger:
#     def message_logging(self, message):
#         """"
#         Create Log File
#         """
#         loggerName = inspect.stack()[1][3]
#         logger = logging.getLogger(loggerName)
#         filehandler = logging.FileHandler("/home/cbnits/Documents/Makemytrip_Assignment/Log/logfile.log", mode='a')
#         logger.addHandler(filehandler)
#         formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
#         filehandler.setFormatter(formatter)
#         logger.setLevel(logging.INFO)
#         logger.setLevel(logging.WARNING)
#         return logger
        