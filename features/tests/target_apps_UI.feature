# Created by Admin at 9/28/2024
Feature: Tests for Target App page

  Scenario: User is able to open Privacy policy
    Given Open Target App Page2
    And Store original window
    When Click Privacy Policy Link
    And Switch to a new window
    Then Verify privacy policy page opened
    And Close the current page
    And Return to the original window
