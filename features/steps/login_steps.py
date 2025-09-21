from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I open the SauceDemo login page')
def step_open_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")

@when('I enter valid credentials')
def step_valid_login(context):
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    context.driver.find_element(By.ID, "login-button").click()

@when('I enter invalid credentials')
def step_invalid_login(context):
    context.driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    context.driver.find_element(By.ID, "password").send_keys("wrong_password")
    context.driver.find_element(By.ID, "login-button").click()

@then('I should see the products page')
def step_verify_products_page(context):
    assert "inventory.html" in context.driver.current_url
    context.driver.quit()

@then('I should see an error message')
def step_verify_error_message(context):
    error = context.driver.find_element(By.CLASS_NAME, "error-message-container")
    assert error.is_displayed()
    context.driver.quit()

@given('I am logged in with valid credentials')
def step_logged_in(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    context.driver.find_element(By.ID, "login-button").click()

@when('I add a product to the cart')
def step_add_to_cart(context):
    
    WebDriverWait(context.driver,5).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
       
    products = context.driver.find_elements(By.CLASS_NAME, "inventory_item")
    for product in products:
        name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
        if name == "Sauce Labs Backpack":
            product.find_element(By.CLASS_NAME, "btn_inventory").click()
        break
          
@then('the cart should contain that product')
def step_verify_cart(context):
    # Click the cart icon
    context.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    WebDriverWait(context.driver,5).until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))
    
    # Verify the cart has at least one item
    items = context.driver.find_elements(By.CLASS_NAME, "cart_item")
       
    assert len(items) > 0
    context.driver.quit()