from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
"""driver = webdriver.Chrome(ChromeDriverManager().install()"""


class GreenKartSeleniumProject:
    """Test case is:

    1. Open the website and verify the URL
    2. Search for "Broccoli"
    3. Perform actions on the search results, add to cart, and check the basket

    """
    actual_site_url = "https://rahulshettyacademy.com/seleniumPractise/#/"

    # Step 1: Open the website and verify the URL
    driver = webdriver.Chrome(executable_path="/Users/ceyhunalyesil/Desktop/dersicerik/chromedriver")
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    site_url = driver.current_url
    print("Site URL is " + site_url)
    if actual_site_url == site_url:
        print("Site URL is correct")

    # Step 2: Search for "Brocolli"
    search_box = driver.find_element(by=By.CLASS_NAME, value="search-keyword")
    search_box.send_keys("Brocolli")
    search_button = driver.find_element(by=By.CLASS_NAME, value="search-button")
    search_button.click()
    print("Search for Broccoli successfully")

    # Step 3: Perform actions on the search results, add to cart, and check the basket
    increment_button = driver.find_element(by=By.CLASS_NAME, value="increment")
    increment_button.click()
    driver.implicitly_wait(10)

    decrement_button = driver.find_element(by=By.CLASS_NAME, value="decrement")
    decrement_button.click()
    driver.implicitly_wait(5)

    # Note: Assuming add_to_cart_button is a list
    add_to_cart_button = driver.find_element(By.XPATH, "//button[text()='ADD TO CART']")
    add_to_cart_button.click()

    basket_icon = driver.find_element(by=By.CLASS_NAME, value="cart-icon")
    basket_icon.click()

    driver.implicitly_wait(100)

    basket_items = driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")
    basket_items.click()  # Assuming used to select the element in the list
    driver.implicitly_wait(100)

    product_name_element = driver.find_element(By.CLASS_NAME, "product-name")
    product_name_text = product_name_element.text
    expected_text = "Brocolli - 1 Kg"
    if expected_text in product_name_text:
        print(
            f"Product name verification successful. Expected text: '{expected_text}', Actual text: '{product_name_text}'")
    else:
        print(f"Product name verification failed. Expected text: '{expected_text}', Actual text: '{product_name_text}'")

    product_amount = driver.find_element(By.CLASS_NAME, "amount")
    product_amount_text = product_amount.text
    expected_amount_text = "120"
    if expected_amount_text in product_amount_text:
        print(
            f"Product name verification successful. Expected text: '{expected_amount_text}', Actual text: '{expected_amount_text}'")
    else:
        print(f"Product name verification failed. Expected text: '{expected_amount_text}', Actual text: '{expected_amount_text}'")

    # Close the browser
    driver.quit()
