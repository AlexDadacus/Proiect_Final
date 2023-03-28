Feature: Pagina dupa logare
  @Succes_login_msg
  Scenario: Verify succes login message
    Given I am on login page
    When I login with valid credentials
    Then I see 'You logged into a secure area!' message
  @Logout_button
  Scenario: Verify logout button
    Given I am on Secure area page after a valid login
    When I click the logout button
    Then I see the logout message
