from selenium import webdriver
from selenium.webdriver.edge.service import Service

s= Service("msedgedriver.exe")
driver = webdriver.Edge(service=s)
driver.get("https:www.youtube.com")