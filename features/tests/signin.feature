# Created by Admin at 9/15/2024
Feature: Target signin page

  Scenario: verify that a logged out user can navigate to Sign In
    Given Open Target
    When Click Sign In
    Then Verify Sign In form opened

  Scenario:  Verify benefit cells on Target Circle Page
    Given Target Circle Page
    Then Verify there are 10 benefit cells

  Scenario: User can signin successfully
    Given Open target
    When Click Sign In
    When Input email and password on SignIn page
    Then Verify user is logged in

  Scenario: User cannot signin
    Given Open target
    When Click Sign In
    When Input incorrect email and password combination
    Then Verify message is shown

  Scenario: User can open and close Terms and Condition
    Given Open Target
    When Click Sign In
    And Store original window
    And Click Term and Condition
    And Switch to a terms and conditions window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original

