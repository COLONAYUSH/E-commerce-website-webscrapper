from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
n = input()
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome("C:/Users/Ayush kumar/Downloads/chromedriver_win32_2/chromedriver.exe", options= options)
driver.get("https://www.walmart.com")
driver.maximize_window()
driver.find_element_by_id("global-search-input").send_keys(n)
sleep(2)
driver.find_element_by_id("global-search-input").send_keys(Keys.ENTER)
# driver.find_element_by_css_selector("#searchProductResult > ul > li.Grid-col.u-size-6-12.u-size-1-4-m.u-size-1-5-xl.search-gridview-first-col-item.search-gridview-first-grid-row-item > div > div.search-result-gridview-item.clearfix.arrange-fill > div:nth-child(5) > div > a").click()
i = 1
while(True):
	f = open("Product.txt", 'a')
	try:
		xpath = f'//*[@id="searchProductResult"]/ul/li[{i}]/div/div[2]/div[5]/div/a/span'
		print(driver.find_element_by_xpath(xpath).text)
		f.write(driver.find_element_by_xpath(xpath).text)
		f.write("\n")
		i += 1
	except:
		print("End of Products")
		f.write("End of Products")
		break
# print(driver.find_element_by_xpath('//*[@id="searchProductResult"]/ul/li[18]/div/div[2]/div[5]/div/a/span').text)

# print(driver.find_element_by_xpath('//*[@id="searchProductResult"]/ul/li[19]/div/div[2]/div[5]/div/a/span').text)

# print(driver.find_element_by_xpath('//*[@id="searchProductResult"]/ul/li[20]/div/div[2]/div[5]/div/a/span').text)

# print(driver.find_element_by_xpath('//*[@id="searchProductResult"]/ul/li[21]/div/div[2]/div[5]/div/a/span').text)

#searchProductResult > ul > li:nth-child(17) > div > div.search-result-gridview-item.clearfix.arrange-fill > div:nth-child(5) > div > a > span
//*[@id="container"]/div/div[3]/div[1]/div[2]/div[6]/div/div[1]/div/a[2]
//*[@id="container"]/div/div[3]/div[1]/div[2]/div[6]/div/div[2]/div/a[2]
//*[@id="container"]/div/div[3]/div[1]/div[2]/div[7]/div/div[1]/div/a[2]
//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a[2]