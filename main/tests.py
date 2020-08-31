from django.test import LiveServerTestCase, override_settings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@override_settings(DEBUG=True)
class FormTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)  # seconds
        super(FormTest, self).setUp()

    def tearDown(self):
        self.browser.quit()
        super(FormTest, self).tearDown()

    def testForm(self):
        browser = self.browser
        browser.get('%s%s' % (self.live_server_url, '/'))

        original_url_input = browser.find_element_by_id('original_url')
        generated_hash_input = browser.find_element_by_id('generated_hash')
        submit_button = browser.find_element_by_css_selector('#form button')

        original_url_input.send_keys('https://www.djangoproject.com/')
        generated_hash_input.send_keys('XXX')
        submit_button.send_keys(Keys.RETURN)

        generated_url_element = browser.find_element_by_css_selector('#generated_urls>.card a')

        assert generated_url_element.text == '%s%s' % (self.live_server_url, '/XXX')

