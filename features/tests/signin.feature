# Created by Admin at 9/15/2024
Feature: Target signin page

  Scenario: verify that a logged out user can navigate to Sign In
    Given Open target.com
    When Click Sign In
    Then Verify Sign In form opened
