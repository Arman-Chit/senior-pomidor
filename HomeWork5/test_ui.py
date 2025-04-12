from HomeWork5.Pages.login_page import LoginPage
from HomeWork5.Pages.inventory_page import InventoryPage
from HomeWork5.Pages.checkout_page import CheckoutPage
from conftest import browser



def test_checkout_order(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_first_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout("Arman", "Arman", "123")
    checkout_page.contain_checkout()
    checkout_page.finish_checkout()

    assert page.locator(".complete-header").inner_text() == "Thank you for your order!"

    checkout_page.burger_button()
    checkout_page.logout_button()


