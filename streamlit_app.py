import streamlit as st
import os, sys

@st.experimental_singleton
def install_chrome():
  os.system('sbase install chromedriver')
  os.system('ln -s /home/appuser/venv/lib/python3.9/site-packages/seleniumbase/drivers/chromedriver /home/appuser/venv/bin/chromedriver')

_ = install_chrome()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.add_argument("--headless")
browser = webdriver.Chrome(options=opts)

browser.get('http://example.com')
st.write(browser.page_source)
