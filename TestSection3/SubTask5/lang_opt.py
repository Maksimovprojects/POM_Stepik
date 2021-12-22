from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'language': user_language})
browser = webdriver.Chrome(options=options)