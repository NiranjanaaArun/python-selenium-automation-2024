Feature: Test Scenarios for Search functionality

  Scenario Outline: User can search for a product
    Given Open Google page
    When Input <search_word> into search field
    And Click on search icon
    Then Product results for <search_word> are shown
    Examples:
    |search_word  |
    |Car          |
    |Bike         |
    |MotorCycle   |

  Scenario:  User can click on different colors
    Given Open target product A-91511634 page
    Then verify user can click through colors

  Scenario: Verify that every product on Target search
    Given Open Target page
    When Input Tea into search field1
    Then Verify Tea is on the search results header
    #Then Verify product name and product image
