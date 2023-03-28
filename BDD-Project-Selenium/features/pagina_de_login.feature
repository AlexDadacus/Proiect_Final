Feature: Pagina de login
  @Valid_login
  Scenario Outline: Login with valid credentials
    Given I am on login page
    When I enter a "<username>"
    Then I enter a "<password>"
    Then I click the login button
    Then I am on Secure Area page

    Examples:
        | username    | password             |
        | tomsmith    | SuperSecretPassword! |

  @Invalid_login
  Scenario Outline: Login with invalid credentials
    Given I am on the login page
    When I enter a "<username>"
    Then I enter a "<password>"
    Then I click the login button
    Then I am on Login page again

      Examples:
        | username    | password             |
        | tomsmith    | Parolagresita!       |
        | alexdadacus | SuperSecretPassword! |
        | alexdadacus | Parolagresita!       |
        |             |                      |