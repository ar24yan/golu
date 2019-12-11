from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass

user_id = input("Enter the user id: ")
password = getpass.getpass("Enter the password: ")
Search_keyword = input("Enter the searching keyword: ")
npage = int(input("Enter the number of pages:"))
nprofile = int(input("Enter the number of profiles:"))


driver = webdriver.Firefox(executable_path='/home/spanidea/Downloads/geckodriver-v0.26.0-linux64/geckodriver')
driver.maximize_window()
time.sleep(2)

driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
time.sleep(3)

user_ele = driver.find_element_by_name("session_key")
#print(user_ele.is_displayed())
#print(user_ele.is_enabled())

pwd_ele = driver.find_element_by_name("session_password")
#print(pwd_ele.is_displayed())
#print(pwd_ele.is_enabled())

user_ele.send_keys(user_id)
time.sleep(1)
pwd_ele.send_keys(password)
time.sleep(2)

driver.find_element_by_xpath('//button[text()="Sign in"]').click()
print("Successfully logged-in")


inpt_ele = driver.find_element_by_xpath("/html/body/header/div/form/div/div/div/div/div[1]/div/input")
driver.find_element_by_xpath("/html/body/header/div/form/div/div/div/div/div[1]/div/input").clear()
inpt_ele.send_keys(Search_keyword)
time.sleep(2)

srch_ele = driver.find_element_by_css_selector(".search-global-typeahead__icon > svg:nth-child(1)").click()
time.sleep(2)
print("Profile searched has been done")

srch_ppl = driver.find_element_by_xpath("/html/body/div[6]/div[4]/div[3]/div/div[1]/header/div/div/div[1]/ul/li[1]/button/span").click()
time.sleep(2)
#driver.refresh()
#time.sleep(10)
print("Searching for people")

i = 1
j = 1


'''while j<=npage:
	rqst = "/html/body/div[6]/div[4]/div[3]/div/div[2]/div/div[2]/div/div/div/div/ul/li[1]/div/div/div[3]/div/button"
	while i <= nprofile:
		driver.refresh()
		print("Refreshing...")
		z1 = i
		z2 = str(z1)
		rqst_sent = rqst.replace("1", z2)
		rqst_sent = driver.find_element_by_xpath("/html/body/div[6]/div[4]/div[3]/div/div[2]/div/div[2]/div/div/div/div/ul/li[1]/div/div/div[3]/div/button").click()
		print(i,"Searched")
		time.sleep(2)

		send_now = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]/span").click()
		print(i, "sent")
		time.sleep(5)
		i += 1

	#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)"
	#driver.execute_script("window.scrollTo(0,1000);")
	next_page =  driver.find_element_by_css_selector("#ember1130 > span:nth-child(2)")
	driver.execute_script("arguments[0].scrollIntoview", next_page)
	time.sleep(5)
	print("Going to the next page...")
	j += 1
print("Request has been sent")
'''
'''
chck_prfl = driver.find_element_by_xpath("/html/body/div[6]/div[5]/div[3]/div/div[2]/div/div[2]/div/div/div/div/ul/li[2]/div/div/div[2]/a/h3/span/span/span[1]").click()
print("Checking profile...")
time.sleep(3)


driver.find_element_by_css_selector("#ember26").click()
time.sleep(1)
driver.find_element_by_id("ember1070").click()
time.sleep(5)
print("Successfully logged-out")
'''


driver.close()

print("Successfully executed.")

