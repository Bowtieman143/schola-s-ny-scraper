from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://portal.nysed.gov/pls/sedrefpublic/SED.sed_inst_qry_vw$.startup")

element = driver.find_element_by_id("P_ADDR_LINE1")
element.send_keys("126 COUNTY RT 2")
driver.find_element_by_css_selector('input[type=submit]').click()
driver.find_element_by_link_text("PUTNAM CENTRAL SCHOOL").click()