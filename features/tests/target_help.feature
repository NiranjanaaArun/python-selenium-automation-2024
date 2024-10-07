# Created by Admin at 10/7/2024
Feature: Target Help page feature
  # Enter feature description here

  Scenario: Verify that Select works and opens the correct page
    Given Open TargetHelp
    When Click on search
    And Choose dropdown
    Then Verify correct page is opened

