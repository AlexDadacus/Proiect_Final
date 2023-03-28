from behave import *


@given('I am on the login page')
def step_impl(context):
    context.browser.driver.get("https://the-internet.herokuapp.com/login")


@when('I enter a "{username}"')
def step_impl(context, username):
    user_name = context.browser.get_username_element()
    user_name.send_keys(username)


@then('I enter a "{password}"')
def step_impl(context, password):
    pasw = context.browser.get_password_element()
    pasw.send_keys(password)


@then('I click the login button')
def step_impl(context):
    login_button = context.browser.get_login_button()
    login_button.click()


@then('I am on Secure Area page')
def step_impl(context):
    redirect_link = context.browser.get_current_url()
    expected_url = "https://the-internet.herokuapp.com/secure"
    assert redirect_link == expected_url


@then('I am on Login page again')
def step_impl(context):
    redir_link = context.browser.get_current_url()
    expt_url = "https://the-internet.herokuapp.com/login"
    assert redir_link == expt_url


@when('I enter a ""')
def step_impl(context):

    @then('I enter a ""')
    def step_impl(context):
        login_button = context.browser.get_login_button()
        login_button.click()
