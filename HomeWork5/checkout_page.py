from base_page import BasePage

class CheckoutPage(BasePage):
    CHECKOUT_BUTTON_SELECTOR = '[data-test="checkout"]'
    FIRST_NAME_SELECTOR = '[data-test="firstName"]'
    LAST_NAME_SELECTOR = '#last-name'
    POSTAL_CODE_SELECTOR = 'input[name="postalCode"]'
    CHECKOUT_CONTAIN_SELECTOR = '#continue'
    CHECKOUT_FINISH_SELECTOR = '#finish'
    BURGER_BUTTON_SELECTOR = '#react-burger-menu-btn'
    LOGOUT_BUTTON_SELECTOR = '[data-test="logout-sidebar-link"]'

    def __init__(self,page):
        super().__init__(page)
        self._endpoint = 'checkout-step-one.html'

    def start_checkout(self):
        self.wait_for_selector_and_click(self.CHECKOUT_BUTTON_SELECTOR)
        self.assert_element_is_visible(self.FIRST_NAME_SELECTOR)
        self.assert_element_is_visible(self.LAST_NAME_SELECTOR)
        self.assert_element_is_visible(self.POSTAL_CODE_SELECTOR)

    def fill_checkout(self, first_name, last_name, postal_code):
        self.wait_for_selector_and_type(self.FIRST_NAME_SELECTOR, first_name, 100)
        self.wait_for_selector_and_type(self.LAST_NAME_SELECTOR, last_name, 100)
        self.wait_for_selector_and_type(self.POSTAL_CODE_SELECTOR, postal_code, 100)
        self.assert_input_value(self.POSTAL_CODE_SELECTOR, postal_code)
        self.assert_input_value(self.FIRST_NAME_SELECTOR,first_name)
        self.assert_input_value(self.LAST_NAME_SELECTOR,last_name)
        self.assert_element_is_visible(self.CHECKOUT_CONTAIN_SELECTOR)

    def contain_checkout(self):
        self.wait_for_selector_and_click(self.CHECKOUT_CONTAIN_SELECTOR)
        self.assert_text_present_on_page('Payment Information:')
        self.assert_element_is_visible(self.CHECKOUT_FINISH_SELECTOR)


    def finish_checkout(self):
        self.wait_for_selector_and_click(self.CHECKOUT_FINISH_SELECTOR)
        self.assert_text_present_on_page('Thank you for your order!')

    def burger_button(self):
        self.wait_for_selector_and_click(self.BURGER_BUTTON_SELECTOR)
        self.assert_text_present_on_page('Logout')

    def logout_button(self):
        self.wait_for_selector_and_click(self.LOGOUT_BUTTON_SELECTOR)
        self.assert_text_present_on_page('Swag Labs')