from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import re

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC



class ZalandoBot():
	def __init__(self):
		self.driver = webdriver.Chrome("C:\\Users\\jozee\\chromedriver\\chromedriver.exe")

	def login(self):
		self.driver.get("https://www.zalando-lounge.pl/#/login")
		self.driver.maximize_window() 

		# finding email entry
		email = self.driver.find_element_by_xpath('//*[@id="form-email"]')
		email.send_keys('youremail')

		pswd = self.driver.find_element_by_xpath('//*[@id="form-password"]')
		pswd.send_keys('password')

		login_btn = self.driver.find_element_by_xpath('//*[@id="react-root-form"]/div/div/div[4]/div/form/fieldset/button')
		login_btn.click()

		# shop
		sleep(0.6)
		# trzeba wylaczyc tren popup o cookies bo nei kliknie sie inaczej
		x = self.driver.find_element_by_xpath('//*[@id="inner-wrapper"]/div[1]/section/section/div')
		x.click()
		odkryj = self.driver.find_element_by_xpath('//*[@id="campaign-ZZO0YB0"]/div/div[1]/div/button')
		act = ActionChains(self.driver)
		act.move_to_element(odkryj).perform()
		odkryj.click()


		
		# wybeiramy rozmiar
		zaladuj = self.driver.find_element_by_xpath('//*[@id="load-my-filter"]/span/span').click()
		self.driver.refresh()
		items = self.driver.find_elements_by_css_selector('div.eFHNko')
		

		for i in range(0,len(items)):
			licznik = 0
			item = self.driver.find_elements_by_css_selector('div.eFHNko') # najlepiej css selectorem szukac jak chcesz multiple elements miec
			item[i].click()
			sleep(1)
			try:
				for i in range(1,5):
					rozmiar = self.driver.find_element_by_xpath(f'//*[@id="article-information"]/div[4]/div[2]/div[{i}]/div')
					if bool(re.search('L|XL', rozmiar.text)):
						rozmiar.click()
						dodaj = self.driver.find_element_by_xpath('//*[@id="addToCartButton"]/div[1]/div[1]')
						dodaj.click()
						sleep(1.5)
						licznik=licznik+1
						if licznik == 2:
							dwa_rozmiary_confirm = self.driver.find_element_by_xpath('//*[@id="article-information"]/div[7]/div/div/div/div/div[2]/div[1]/div[2]/label[3]').click()
							# sleep(1)
							potwierdz = self.driver.find_element_by_xpath('//*[@id="article-information"]/div[7]/div/div/div/div/div[2]/div[2]/button').click()
							sleep(1)					
			except:
				pass
				
			finally:
				self.driver.back()	

if __name__ == '__main__':
	bot = ZalandoBot()
	bot.login()
