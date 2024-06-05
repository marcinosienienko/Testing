Feature: Register

  Scenario Outline: Register new account
    Given Register page
    When User is created with email:<email> password:<password>
    Then Registered account returns correct response
    And The response contains the fields id and token
    And User id is 4 and token is a string

  Examples:
  | email              | password |
  | eve.holt@reqres.in | pistol   |