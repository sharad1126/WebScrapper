from selenium import webdriver

geckodriver = '/Users/SharadAggrawal/Downloads/geckodriver'

options = webdriver.FirefoxOptions()
options.add_argument('-headless')

browser = webdriver.Firefox(executable_path=geckodriver, firefox_options=options)

browser.get('https://www.duckduckgo.com')

browser.save_screenshot('/Users/SharadAggrawal/Desktop/headless_firefox_test.png')

browser.quit()
