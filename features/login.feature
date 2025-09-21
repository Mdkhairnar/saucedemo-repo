Feature: Login functionality

	Scenario: Successful login
	Given I open the SauceDemo login page
	When I enter valid credentials
	Then I should see the products page


	Scenario: Failed login with invalid credentials
	Given I open the SauceDemo login page
	When I enter invalid credentials
	Then I should see an error message
	
	
	Scenario: Add item to cart
	Given I am logged in with valid credentials
	When I add a product to the cart
	Then the cart should contain that product

