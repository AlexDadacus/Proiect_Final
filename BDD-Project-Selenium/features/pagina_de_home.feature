Feature: Pagina de Home
  @A/B_page
  Scenario: Verify A/B Testing page
    Given I am on the home page
    When I click A/B Testing
    Then I am on A/B Test Control page
  @Checkboxes_page
  Scenario: Verify A/B Testing page
    Given I am on the home page
    When I click Checkboxes
    Then I am on Checkboxes page
  @Scroll_page
  Scenario: Verify Infinite Scroll page
    Given I am on the home page
    When I click Infinite Scroll
    Then I am on Infinite Scroll page
  @Geolocation_page
  Scenario: Verify Geolocation page
    Given I am on the home page
    When I click Geolocation
    Then I am on Geolocation page
  @Form_authentication_page
  Scenario: Verify Form authentication page
    Given I am on the home page
    When I click Form authentication
    Then I am on Form authentication page