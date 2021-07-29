from selenium import webdriver
import time


driver = webdriver.Firefox(executable_path="geckodriver")       #path for driver


xpaths_pic = {

    "share_btn": "//div[@aria-label='Send this to friends or post it on your Timeline.']",
    "groups": "//div[@class='pybr56ya f10w8fjw']/div[5]",
    "search": "//input[@aria-label='Search for groups']",
    "share": "//div[@aria-label='Post']",
}

xpaths_vid = {

    "share_btn": "//div[@aria-label='Send this to friends or post it on your Timeline.']",
    "more_option": "//*[text()='More options']",
    "share_to_groups": "//span[text()='Share to a group']",
    "search": "//input[@aria-label='Search for groups']",
    "share": "//div[@aria-label='Post']"
}



def SignIn(id, password, type):
    driver.find_element_by_name('email').send_keys(id)
    driver.find_element_by_name('pass').send_keys(password)
    if (type == 0):
        driver.find_element_by_id('loginbutton').click()
    else:
        driver.find_element_by_xpath("//div[@aria-label='Accessible login button']").click()


def ChangeAcc(profile):
    driver.find_element_by_xpath("//button[@aria-label='Voice Selector']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@role='menuitemradio']/div[2]/div/div/span[text()='{}']".format(profile)).click()


def Video(file):

    file_content = open(file, 'r', encoding="utf-8").readlines()

    time.sleep(2)

    try:
        
        for grp in file_content:

            for x in xpaths_vid.keys():

                if x == "search":
                    time.sleep(5)
                    driver.find_element_by_xpath(xpaths_vid[x]).send_keys(grp.strip())
                    time.sleep(3)
                    driver.find_element_by_xpath("//*[@class='b20td4e0 muag1w35']/div[1]").click()

                else:
                    time.sleep(8)
                    driver.find_element_by_xpath(xpaths_vid[x]).click()

    except Exception as error:
        print(error)



def Photo(file):

    file_content = open(file, 'r', encoding="utf-8").readlines()
    time.sleep(4)
    
    try:
        for grp in file_content:

            for x in xpaths_pic.keys():

                if x == "search":
                    time.sleep(3)
                    driver.find_element_by_xpath(xpaths_pic[x]).send_keys(grp.strip())
                    time.sleep(3)
                    driver.find_element_by_xpath("//*[@class='b20td4e0 muag1w35']/div[1]").click()
                else:
                    time.sleep(6)
                    driver.find_element_by_xpath(xpaths_pic[x]).click()

    except Exception as error:
        print(error)



def main(username, password, post_link, file, acc_switch,post_type):

    driver.get(post_link)
    time.sleep(5)
    SignIn(username, password, post_type)
    time.sleep(10)

    if (post_type == 0):

        Video(file)

    else:

        if(acc_switch != ""):
            ChangeAcc(acc_switch)
        
        Photo(file)

    

# main('Your Username', 'Your Password', 'Post Link', 'Filename.txt', 'Profile Name', 0 or 1)
