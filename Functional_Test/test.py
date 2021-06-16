from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 2
class PageTest(LiveServerTestCase):



	def wait_for_table(self, row_text):        
           start_time = time.time()
           while True:  
               try:                
                   table = self.browser.find_element_by_id('id_table')                  
                   rows = table.find_elements_by_tag_name('tr')                
                   self.assertIn(row_text, [row.text for row in rows])
                   return
               except (AssertionError, WebDriverException) as e:  
                   if time.time() - start_time > MAX_WAIT:  
      	               raise e                  
                   time.sleep(0.5)  
                 
	def setUp(self):
	 self.browser = webdriver.Firefox()

	def test_browser_title(self):
	 self.browser.get('http://localhost:8000/')
	 #self.browser.get(self.live_server_url)
	 self.assertIn('Community Pantry System',self.browser.title)
	 header_text = self.browser.find_element_by_tag_name('h2').text
	 self.assertIn('Community Pantry System', header_text)
	 
	 
	 
	
	 inputfname = self.browser.find_element_by_id('fname')
	 self.assertEqual(inputfname.get_attribute('placeholder'),'Enter your fullname')
	 inputfname.click()
	 time.sleep(1)
	 inputfname.send_keys('Kenneth Denaga')
	 
	 time.sleep(1)

	 inputeadd = self.browser.find_element_by_id('contactnumber')
	 self.assertEqual(inputeadd.get_attribute('placeholder'),'Enter your contactnumber')
	 inputeadd.click()
	 time.sleep(1)
	 inputeadd.send_keys('09054990958')
	 time.sleep(1)
	 
	 
	 inputeadd = self.browser.find_element_by_id('eadd')
	 self.assertEqual(inputeadd.get_attribute('placeholder'),'Enter your Email Address')
	 inputeadd.click()
	 time.sleep(1)
	 inputeadd.send_keys('kennethdenaga1212@gmail.com')
	 time.sleep(1)
	 
	 
	 '''boxConfirm = self.browser.find_element_by_id('boxConfirm')
	 boxConfirm.click()
	 time.sleep(2)'''
	 
