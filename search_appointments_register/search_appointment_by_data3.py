from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import json

try:
    @pytest.fixture(scope='session')
    def config():
        with open('search_config.json') as config_file:
            data = json.load(config_file)
        return data
    
    @pytest.fixture(scope='session')
    def browser(config):
        if config['browser'] == 'chrome':
            driver = Chrome()
        else:
            raise Exception(f'"{config["browser"]}" is not a supported browser')
            
        driver.implicity_wait(config['wait_time'])
        yield driver

finally:
    driver.quit()