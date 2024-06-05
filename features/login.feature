Feature: Login

  Scenario Outline: Login existing account
    Given Login page
    When User logs in with email:<email> password:<password>
    Then Login is successful
    And The response contains the field token
    And Token is a string

  Examples:
  | email              | password |
  | eve.holt@reqres.in | pistol   |
