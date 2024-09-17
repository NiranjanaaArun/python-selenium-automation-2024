# Created by Admin at 9/9/2024
Feature: Product checkout functionality

  Scenario: User can view the cart page
    Given Open Target page
    When Click cart icon
    Then “Your cart is empty” message is shown

  Scenario: User can verify the products in cart
    Given Open Target page
    When Search for an tea
    And Add items into cart
    Then Verify the products

