from django.test import LiveServerTestCase, override_settings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

ORIGINAL_URL_TEST = "https://www.djangoproject.com/"
GENERATED_HASH_TEST = "XXX"


@override_settings(DEBUG=True)
class FormTest(LiveServerTestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        self.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        self.browser.implicitly_wait(10)  # seconds
        super(FormTest, self).setUp()

    def tearDown(self):
        self.browser.quit()
        super(FormTest, self).tearDown()

    def testForm(self):
        browser = self.browser
        browser.get("%s%s" % (self.live_server_url, "/"))

        original_url_input = browser.find_element_by_id("original_url")
        generated_hash_input = browser.find_element_by_id("generated_hash")
        submit_button = browser.find_element_by_css_selector("#form button")

        original_url_input.send_keys(ORIGINAL_URL_TEST)
        generated_hash_input.send_keys(GENERATED_HASH_TEST)
        submit_button.send_keys(Keys.RETURN)

        generated_url_element = browser.find_element_by_css_selector("#generated_urls>.card a")

        assert generated_url_element.text == "%s%s" % (self.live_server_url, "/" + GENERATED_HASH_TEST)
