Feature: Users

  Scenario Outline: Create new user
    Given Im in super App
    When User is created with name:<name> job:<job>
    Then Created user exist in the system
    And User has correct data for "name" is "<name>"
    And User has correct data for "job" is "<job>"

  Examples:
    | name      | job      |
    | morpheus  | leader   |
