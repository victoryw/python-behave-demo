Feature: show case the step implementation
  Scenario: look up a book
  Given I search for a valid book
   Then the result page will include "success"

  Scenario: look up an invalid book
    Given I search for a invalid book
     Then the result page will include "failure"