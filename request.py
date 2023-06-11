# import requests

# response = requests.get('https://www.getapp.com/hr-employee-management-software/a/samesystem/features/')
# print(response.text)

from  selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep
import os



# BASE_DIR = os.getcwd()
# driver = webdriver.Chrome()
# driver.get('https://www.getapp.com/hr-employee-management-software/a/samesystem/features/')

# driver = webdriver.Chrome()

def get_app_feature(driver, app_url):
    driver.get(app_url)

    result = dict()
    driver.implicitly_wait(10)
    
    expand_btn = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[1]/div/div[4]/div[2]/button')

    expand_btn.click()
    sleep(5)

    # //*[@id="__next"]/div[2]/div/div[2]/div[1]/div[1]/div/div[4]/div[1]
    # //*[@id="__next"]/div[2]/div/div[2]/div[1]/div[1]/div/div[4]/div[1]/div[1]
    # //*[@id="__next"]/div[2]/div/div[2]/div[1]/div[1]/div/div[4]/div[1]/div[49]/div
    # //*[@id="__next"]/div[2]/div/div[2]/div[1]/div[1]/div/div[4]/div[1]/div[2]/div/span
    # //*[@id="__next"]/div[2]/div/div[2]/div[1]/div[1]/div/div[4]/div[1]/div[2]/i

    content = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[1]/div/div[4]/div[1]')
    content_child = content.find_elements(By.XPATH, ".//*/div/span")
    content_type = content.find_elements(By.XPATH, ".//*/i")

    for c, t in zip(content_child,content_type):
        text = c.get_attribute("innerHTML")
        att_type = True if t.get_attribute("data-icon") == "fas-check" else False
        
        result[text] = att_type

    return result

def get_app_info(driver, root_url):
    driver.get(root_url)
    result = dict()
    names = driver.find_elements(By.XPATH, '//a[@data-testid="listing-item_text-link_product-name"]/h2/span')
    url_element = driver.find_elements(By.XPATH, '//a[@data-testid="listing-item_text-link_read-more-about-product"]')
    
    for c, u in zip(names, url_element):
        text = c.get_attribute("innerHTML")
        url = u.get_attribute("href") + "features/"
        u.click()
        feature = get_app_feature(driver, url)

        result[text] = [url, feature]
        sleep(3)
        driver.get(root_url)
        sleep(3)
    
    return result

# def get_app_features_from_list(driver, urls):
#     result = dict()
#     for app in urls.keys():
#         print(urls[app])
#         feature = get_app_feature(driver, urls[app])
#         result[app] = [urls[app], feature]

#     return result

if __name__ == '__main__':
    driver = webdriver.Chrome()

    app_features = get_app_info(driver, 'https://www.getapp.com/hr-employee-management-software/human-resources/')
    # app_features = get_app_features_from_list(driver, app_urls)
    print(app_features)