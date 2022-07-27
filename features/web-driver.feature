@fixture.browser.chrome
Feature: begin to use the web-driver
  Scenario: I want to use the chrome to browser bing
    Given I was on the Bing Index
    When I search for a "keyword" keyword
    Then I will find out the "keyword" in the search result page's input box
