from selenium import webdriver
import csv

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

with open('names.csv', 'w', newline='') as csvfile:
    
    thewriter = csv.writer(csvfile)
    thewriter.writerow(['Occupation', 'First Name', 'Last Name'])
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

    school_leaders_list = []

    for index, contact in enumerate(school_contacts):     
        fields = contact.find_elements_by_tag_name('td')
        if index == 0:
            continue
        for field_index, field in enumerate(fields):
            if field_index == 0:
                school_leaders_list.append(field.find_element_by_tag_name('a').get_attribute("href"))
                print(field.find_element_by_tag_name('a').get_attribute("href"))
                thewriter.writerow([field.find_element_by_tag_name('a').get_attribute("href")])
            continue

    print(school_leaders_list)
    print(len(school_leaders_list))

            # print(driver.current_url)