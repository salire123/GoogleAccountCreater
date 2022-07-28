from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class inputtogoogle:

#input to web p1
    def runweb(youdrive, username, passwd, lastname, fristName, phonenum, year, day, month, gender ) -> None:

        
        driver = webdriver.Firefox(executable_path=youdrive)
        driver.get("https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dgoogle%26oq%3Dgoogle%2B%26aqs%3Dchrome..69i57j69i60l3j69i65l3j69i60.3469j0j1%26sourceid%3Dchrome%26ie%3DUTF-8&hl=zh-TW&dsh=S1711349062%3A1657553309834069&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp")

        set1 = {
            "lastName"      : lastname,
            "firstName"     : fristName,
            "Username"      : username,
            "Passwd"        : passwd,
            "ConfirmPasswd" : passwd
        }

        #put info in to from #########
        for i in set1:
            element = driver.find_element(By.NAME, i)
            element.send_keys(set1[i])

        #next p 
        element.click()
        element.send_keys(Keys.ENTER)
        
        #input p4
        #put phone num   
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID,"phoneNumberId")))
        element = driver.find_element(By.ID, "phoneNumberId")
        element.send_keys(phonenum)
        #next p
        element.send_keys(Keys.ENTER)



        
        #input p3
        element = wait.until(EC.element_to_be_clickable((By.ID,"code")))
        element = driver.find_element(By.ID, "code")
        verifycode = input("phone verify: ")
        element.send_keys(verifycode)
        #next p
        element.send_keys(Keys.ENTER)

        #input p4
        element = wait.until(EC.element_to_be_clickable((By.ID,"year")))

        set2 = {
            "year"     : year,
            "day"     : day,
        }

        for i in set2:
            element = driver.find_element(By.NAME, i)
            element.send_keys(set2[i])
##########################################3
        set3 = {
            "month"     : month,
            "gender"     : gender,
        }

        for i in set3:
            select_element = driver.find_element(By.ID,i)
            select_object = Select(select_element)
            select_object.select_by_value(set3[i])

        element.click()
        element.send_keys(Keys.ENTER)

        '''
        element = wait.until(EC.element_to_be_clickable((By.ID,"year")))
        element = driver.find_element(By.ID, "year")
        element.send_keys(2002)

        select_element = driver.find_element(By.ID,"month")
        select_object = Select(select_element)
        select_object.select_by_value("4")

        element = driver.find_element(By.ID, "day")
        element.send_keys(2002)
        
        select_element = driver.find_element(By.ID,"gender")
        select_object = Select(select_element)
        select_object.select_by_value("3")
        element.send_keys(Keys.ENTER)
        '''


        #input p5
        element = driver.find_elements(By.XPATH,"//span[text(),'略過']")
        element.click()

        #input p6
        element = driver.find_elements(By.XPATH,"//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']")
        element.click()
