from config import keys
from selenium import webdriver
import time

def order(k):
    driver.get(k['product_url'])
    driver.find_element_by_xpath('//*[@id="add-to-cart"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="cart-items"]/div/a').click()
    driver.find_element_by_xpath('//*[@id="checkout"]').click()
    driver.find_element_by_xpath('//*[@id="checkout_email"]').send_keys(k["email"])
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').send_keys(k["first_name"])
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_last_name"]').send_keys(k["last_name"])
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]').send_keys(k["address"])
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address2"]').send_keys(k["apartment"])
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]').send_keys(k["city"])
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]').send_keys(k["zip_code"])
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]').send_keys(k["phone_num"])
    driver.find_element_by_xpath('//*[@id="continue_button"]').click()
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="continue_button"]').click()
    driver.find_element_by_name("").send_keys(k["card_num"])
    driver.find_element_by_xpath('//*[@id="name"]').send_keys(k["card_name"])
    driver.find_element_by_xpath('//*[@id="expiry"]').send_keys(k["card_expiry"])
    driver.find_element_by_xpath('//*[@id="verification_value"]').send_keys(k["cvv"])
    driver.find_element_by_xpath('//*[@id="continue_button"]').click()




if __name__ == '__main__':
    driver = webdriver.Chrome('chromedriver')
    order(keys)