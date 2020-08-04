from selenium import webdriver
import csv

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['position', 'first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

# Open the site url
driver.get("http://portal.nysed.gov/pls/sedrefpublic/SED.sed_inst_qry_vw$.startup")
# Finding the address input
address_input = driver.find_element_by_id("P_ADDR_LINE1")
# Typing the School Address
address_input.send_keys("23 HUSKY LANE")
# Clicking the submition button
driver.find_element_by_css_selector('input[type=submit]').click()
# Checking if the list contains the desired school
driver.find_element_by_link_text("FRANKLIN-ESSEX-HAMILTON BOCES").click()
# Finding the contacts associated with the school
school_contacts = driver.find_elements_by_xpath("/html/body/p[13]/table/tbody/tr")

for contact in school_contacts:
    contact_fields = contact.find_elements_by_tag_name('td')
    # Itterating through the listed fields ex. "First Name" ect.    
    contact_info = []

    for field in contact_fields:
        print(field.text)
        contact_info.append(field.text)

    print('This is after the finished contact')
    print(contact_info)

    print(len(contact_info))

    if len(contact_info) > 0:
        writer.writerow({'position': contact_info[0], 'first_name': contact_info[1], 'last_name': contact_info[2]})
    else:
        print("Sorry there is no data here")
# driver.close()













