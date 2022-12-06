import streamlit as st
import os, sys
import subprocess

# @st.experimental_singleton
# def install_chrome():
#   os.system('sbase install chromedriver')
# #   os.system('ln -s /home/appuser/venv/lib/python3.9/site-packages/seleniumbase/drivers/chromedriver /home/appuser/venv/bin/chromedriver')

# _ = install_chrome()
subprocess.run(["which", "chromium"])
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('http://example.com')
st.write(driver.page_source)
