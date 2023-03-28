from behave import *


@given("I am on login page")
def step_impl(context):
    context.browser.driver.get("https://the-internet.herokuapp.com/login")


@when("I login with valid credentials")
def step_impl(context):
    user_name = context.browser.get_username_element()
    user_name.send_keys("tomsmith")
    password = context.browser.get_password_element()
    password.send_keys("SuperSecretPassword!")
    login_button = context.browser.get_login_button()
    login_button.click()


@then("I see 'You logged into a secure area!' message")
def step_impl(context):
    secure_area_message = context.browser.get_alert_secure_area().text
    expected_message = "You logged into a secure area!"
    assert expected_message in secure_area_message


@given("I am on Secure area page after a valid login")
def step_impl(context):
    context.browser.driver.get("https://the-internet.herokuapp.com/login")
    user_name = context.browser.get_username_element()
    user_name.send_keys("tomsmith")
    password = context.browser.get_password_element()
    password.send_keys("SuperSecretPassword!")
    login_button = context.browser.get_login_button()
    login_button.click()


@when("I click the logout button")
def step_impl(context):
    logout_button = context.browser.get_logout_bt()
    logout_button.click()


@then("I see the logout message")
def step_impl(context):
    logout_msg = context.browser.get_logout_message().text
    expected_msg = "You logged out of the secure area!"
    assert expected_msg in logout_msg
