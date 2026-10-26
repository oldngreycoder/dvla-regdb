Feature: Vehicle Registrations
  As a User
  I want to query the register
  So that I can find vehicle_id

  Background:
    Given The Register contains Registrations

  Scenario: Count the registrations
    When I count the registrations
    Then there are 4 registrations

  Scenario: accumulate the cost
    When I accumulate the registration cost
    Then the total cost is 1000100


  Scenario Outline: Find the vehicle_id of a registration
    When I look up the vehicle_id of "<registration_id>"
    Then the vehicle_id is "<vehicle_id>"

    Examples:
      | registration_id | vehicle_id |
      | AB01 CDE        | 12345      |
      | FG02 HJK        | 67890      |
      | L33T H4X0R      | Unassigned |
      | AG1L3           | 999999     |
