import time
import traceback

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from ExecReq import *

#def driverForPlayDay(day, month):
def main():
    chrome_options = Options()
    notFin = True
    while notFin:
        try:
            driver = webdriver.Chrome("/home/az/ProjectsData/Drivers/chromedriver",chrome_options=chrome_options)
            driver.set_page_load_timeout(10)

            driver.get('https://alexbetting.com/auth/')
            notFin = False
        except:
            print('TIMEOUT:\n', traceback.format_exc())
            print('timeout')
            #driver = webdriver.Chrome("/usr/bin/chromedriver",chrome_options=chrome_options)
            #driver.set_page_load_timeout(80)
            time.sleep(1)
    login(driver)
    while len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    # while clickGetElem(driver, "//input[@value='103']") == False:
    #     while len(driver.window_handles) > 1:
    #         driver.switch_to.window(driver.window_handles[1])
    #         driver.close()
    #         driver.switch_to.window(driver.window_handles[0])
    #time.sleep(5)
    driver.get('https://alexbetting.com/matches/statp/')

    clickGetElemSpace(driver, "//input[@type='checkbox' and ()]")
    clickGetElemSimple(driver, "//select[@name='day']/option[contains(text(), '1')]")
    clickGetElemSimple(driver, "//select[@name='month']/option[contains(text(), 'января')]")
    clickGetElemSimple(driver, "//select[@name='year']/option[contains(text(), '2018')]")
    clickGetElemSimple(driver, "//select[@name='dodata']/option[@value='4']")
    clickGetElemEnter(driver, "//input[@value='Показать']")
    print(getElemByXPath("//pre", driver).text)


def login(driver, name = 'fczspb', password = '1luLndck'):
    time.sleep(1)
    while (True):
        #time.sleep(5)
        clickGetElemEnter(driver, "//a[contains(text(), 'Авторизация')]")
        #time.sleep(1)
        isContinue = False
        while len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            isContinue = True
        if isContinue:
            continue
        getElemByXPath("//input[@name='login']", driver).send_keys(name)
        getElemByXPath("//input[@name='pass']", driver).send_keys(password)
        while (True):
            time.sleep(3)
            clickGetElemEnter(driver, "//input[@class='but']")
            #time.sleep(5)
            isContinue = False
            while len(driver.window_handles) > 1:
                driver.switch_to.window(driver.window_handles[1])
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                isContinue = True
            if isContinue:
                continue
            #time.sleep(3)
            #time.sleep(1)
            break
        break
    driver.refresh()





if __name__ == '__main__':
    main()