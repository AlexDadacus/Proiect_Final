from behave import *


@given("I am on the home page")
def step_impl(context):
    context.browser.driver.get("https://the-internet.herokuapp.com/")


@when("I click A/B Testing")
def step_impl(context):
    abtesting = context.browser.get_abtesting()
    abtesting.click()


@then("I am on A/B Test Control page")
def step_impl(context):
    redirect_link = context.browser.get_current_url()
    expected_url = "https://the-internet.herokuapp.com/abtest"
    assert redirect_link == expected_url


@when("I click Checkboxes")
def step_impl(context):
    checkbox_link = context.browser.get_checkboxes_link()
    checkbox_link.click()


@then("I am on Checkboxes page")
def step_impl(context):
    redirect_link = context.browser.get_current_url()
    expected_url = "https://the-internet.herokuapp.com/checkboxes"
    assert redirect_link == expected_url


@when("I click Infinite Scroll")
def step_impl(context):
    infinite_scroll = context.browser.get_infinite_scroll()
    infinite_scroll.click()


@then("I am on Infinite Scroll page")
def step_impl(context):
    redirect_link = context.browser.get_current_url()
    expected_url = "https://the-internet.herokuapp.com/infinite_scroll"
    assert redirect_link == expected_url


@when("I click Geolocation")
def step_impl(context):
    geolocation = context.browser.get_geolocation()
    geolocation.click()


@then("I am on Geolocation page")
def step_impl(context):
    redirect_link = context.browser.get_current_url()
    expected_url = "https://the-internet.herokuapp.com/geolocation"
    assert redirect_link == expected_url


@when("I click Form authentication")
def step_impl(context):
    form_link = context.browser.get_form_authentication_link()
    form_link.click()


@then("I am on Form authentication page")
def step_impl(context):
    redirect_link = context.browser.get_current_url()
    expected_url = "https://the-internet.herokuapp.com/login"
    assert redirect_link == expected_url
