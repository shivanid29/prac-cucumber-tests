Feature: Verify whether the book is added and deleted

  Scenario: Verify Add Book functionality
    Given the book details which needs to be added
    When we execute the API
    Then the book is successfully added




    