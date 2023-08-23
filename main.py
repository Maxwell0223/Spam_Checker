# Maxwell Wippich
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import Flask, request
import json


def spamCheck(IP):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")


    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://multirbl.valli.org/lookup/'+ IP + '.html')
    wait = WebDriverWait(driver, 100) #wait for page to load

    css_selector = "#lo-main > table:nth-child(4) > tbody > tr:nth-child(2) > td.clrBrownlisted > span"

    # Wait for the element to be present
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
    element_text = element.text
    if(element_text != "0"):
        print("Brown Listed")

    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#lo-main > table:nth-child(4) > tbody > tr:nth-child(5) > td.clrBrownlisted > span")))
    element_text = element.text
    if(element_text != "0"):
        print("Brown Listed")

    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        "#lo-main > table:nth-child(4) > tbody > tr:nth-child(8) > td.clrBrownlisted > span")))
    element_text = element.text
    if (element_text != "0"):
        print("Brown Listed")

    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#lo-main > table:nth-child(4) > tbody > tr:nth-child(11) > td.clrBrownlisted > span")))
    element_text = element.text
    if (element_text != "0"):
        print("Brown Listed")

    css_selector = "#lo-main > table:nth-child(4) > tbody > tr:nth-child(2) > td.clrYellowlisted > span"

    # Wait for the element to be present
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
    element_text = element.text
    if(element_text != "0"):
        print("Yellow Listed")

    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#lo-main > table:nth-child(4) > tbody > tr:nth-child(5) > td.clrYellowlisted > span")))
    element_text = element.text
    if(element_text != "0"):
        print("Yellow Listed")

    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        "#lo-main > table:nth-child(4) > tbody > tr:nth-child(8) > td.clrYellowlisted > span")))
    element_text = element.text
    if (element_text != "0"):
        print("Yellow Listed")

    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#lo-main > table:nth-child(4) > tbody > tr:nth-child(11) > td.clrYellowlisted > span")))
    element_text = element.text
    if (element_text != "0"):
        print("Yellow Listed")

    css_selector = "#lo-main > table:nth-child(4) > tbody > tr:nth-child(2) > td.clrBlacklisted > span"

    # Wait for the element to be present
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
    element_text = element.text
    if(element_text != "0"):
        print("blacklisted")

    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#lo-main > table:nth-child(4) > tbody > tr:nth-child(5) > td.clrBlacklisted > span")))
    element_text = element.text
    if(element_text != "0"):
        print("blacklisted")

    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        "#lo-main > table:nth-child(4) > tbody > tr:nth-child(8) > td.clrBlacklisted > span")))
    element_text = element.text
    if (element_text != "0"):
        print("blacklisted")

    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#lo-main > table:nth-child(4) > tbody > tr:nth-child(11) > td.clrBlacklisted > span")))
    element_text = element.text
    if (element_text != "0"):
        print("blacklisted")

    driver.close()
    driver.quit()



# Press the green button in the gutter to run the script.
path_name = ''
service_name = 'default'
app = Flask(__name__)
@app.route("/")
def runner():
    IP = request.args.get("IP")
    if IP:
        IP_address = IP
    spamCheck(IP_address)

    # Specify the file path where you want to save the .json file
    return 'finished'



if __name__ == '__main__':
    app.run(port=8000, debug=True)
