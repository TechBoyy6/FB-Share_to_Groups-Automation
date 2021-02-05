from selenium import webdriver
from plyer import notification
import time
from selenium.webdriver.common.action_chains import ActionChains

user_email = input("Enter your facebook Login ID --> ")
user_pass = input("Enter your facebook Password --> ")
post_link = input("Paste your post link--> ")
filename = input("Type the name of the file with the extension--> ")    #make sure the file is in same folder
user = int(input("If your post is video press 0 and if photo press 1--> "))

driver = webdriver.Firefox(executable_path="geckodriver")       #path for driver
driver.get(post_link)
opn = open(filename, 'r', encoding="utf-8").readlines()

xpaths_pic = {

    "share_btn": "//div[@class='ozuftl9m tvfksri0 olo4ujb6 jmbispl3']/div/div[3]/div",
    "groups": "//div[@class='pybr56ya f10w8fjw']/div[5]",
    "search": "//input[@aria-label='Search for groups']",
    "share": "//div[@aria-label='Post']"
}

xpaths_vid = {

    "share_btn": "//div[@class='s1tcr66n']/div[2]/div/div",
    "more_option": "//*[text()='More options']",
    "share_to_groups": "//span[text()='Share to a group']",
    "search": "//input[@aria-label='Search for groups']",
    "share": "//div[@aria-label='Post']"
}

if user == 0:
    time.sleep(4)
    log_email = driver.find_element_by_id('email').send_keys(user_email)
    log_pass = driver.find_element_by_id('pass').send_keys(user_pass)
    login = driver.find_element_by_id('loginbutton').click()
    notification.notify(
        title="Press Enter to confirm and start -->",
        message="If the login is successfully done, press enter in terminal to proceed",
        timeout=10
    )
    input("-->")
    time.sleep(2)

    try:
        enlarge = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[4]").click()
        time.sleep(3)
        element = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[2]/div/div[3]")
        hover = ActionChains(driver).move_to_element(element).perform()
        pause = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/span/span/span/div").click()

        for g in opn:

            for x in xpaths_vid.keys():

                if x == "search":
                    time.sleep(2)
                    search = driver.find_element_by_xpath(xpaths_vid[x]).send_keys(g.strip())
                    grp_click = driver.find_element_by_xpath("//*[@class='b20td4e0 muag1w35']/div[1]").click()

                else:
                    time.sleep(4)
                    press = driver.find_element_by_xpath(xpaths_vid[x]).click()
    except Exception as error:
        print(error)

elif user == 1:
    time.sleep(4)
    log_email = driver.find_element_by_name('email').send_keys(user_email)
    log_pass = driver.find_element_by_name('pass').send_keys(user_pass)
    login = driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[2]/div/form/div/div[3]/div').click()
    notification.notify(
        title="Press Enter to confirm and start -->",
        message="If the login is successfully done, press enter in terminal to proceed",
        timeout=10
    )
    input("-->")

    # This code below can be used to change profile if you have multiple accounts.

    # ch1 = driver.find_element_by_xpath("//button[@aria-label='Voice Selector']").click()
    # time.sleep(2)
    # ch2 = driver.find_element_by_xpath("//div[@role='menu']/div/div/div/div[3]/div").click()

    try:
        for i in opn:

            for x in xpaths_pic.keys():

                if x == "search":
                    time.sleep(2)
                    search = driver.find_element_by_xpath(xpaths_pic[x]).send_keys(i.strip())
                    grp_click = driver.find_element_by_xpath("//*[@class='b20td4e0 muag1w35']/div[1]").click()
                else:
                    time.sleep(4)
                    press = driver.find_element_by_xpath(xpaths_pic[x]).click()
    except Exception as error:
        notification.notify(
            title="I am Sry, ERROR occurred -->",
            message="There was an unexpected error so execution of program stopped.",
            timeout=10
        )
        print(error)

else:
    print("It seems like you don't follow instructions so 'BYE'")
    exit(0)
