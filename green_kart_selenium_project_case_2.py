from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

"""driver = webdriver.Chrome(ChromeDriverManager().install()"""


class GreenKartSeleniumProjectCase2:
    """Test case is:

    1. Open the website and verify the URL
    2. Scroll down to the specified element and check the Nuts Mixture
    3. Click the "Go to Cart" button, go to Basket and enter the promo code

    """
    actual_site_url = "https://rahulshettyacademy.com/seleniumPractise/#/"

    # Step 1: Open the website and verify the URL
    driver = webdriver.Chrome(executable_path="/Users/ceyhunalyesil/Desktop/dersicerik/chromedriver")
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    site_url = driver.current_url

    # Step 2: Scroll down to the specified element and check the Nuts Mixture
    nuts_mixture_element = driver.find_element(By.XPATH, "//h4[@class='product-name' and contains(text(), 'Nuts Mixture - 1 Kg')]")
    ActionChains(driver).move_to_element(nuts_mixture_element).perform()

    # Wait for some time to see the changes (you might need to add a proper wait here)
    driver.implicitly_wait(3)

    quantity_elements = driver.find_elements(By.CLASS_NAME, "quantity")
    index_to_change = 27  # Python indeksleri 0'dan başladığı için 27. indeksi seçiyoruz
    quantity_elements[index_to_change].clear()
    quantity_elements[index_to_change].send_keys("5")
    print(f"Set the value '5' for the 28th quantity element.")

    # Locate the price element
    price_element = driver.find_elements(By.CLASS_NAME, "product-price")

    # Get the text content of the price element
    actual_price_text = price_element[27].text

    # Expected price
    expected_price_text = "950"

    # Check if the expected price matches the actual price
    if expected_price_text == actual_price_text:
        print(
            f"Price verification successful. Expected price: '{expected_price_text}', Actual price: '{actual_price_text}'")
    else:
        print(
            f"Price verification failed. Expected price: '{expected_price_text}', Actual price: '{actual_price_text}'")

    driver.implicitly_wait(100)
    # Locate and click the "Add to Cart" button
    add_to_cart_button = driver.find_elements(By.XPATH, "//button[text()='ADD TO CART']")
    add_to_cart_button[27].click()
    driver.implicitly_wait(100)

    # Step 3: Click the "Go to Cart" button, go to Basket and enter the promo code
    basket_icon = driver.find_element(by=By.CLASS_NAME, value="cart-icon")
    basket_icon.click()
    driver.implicitly_wait(100)
    go_to_cart_button = driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")
    go_to_cart_button.click()

    # Locate the input element with the class "promoCode" and send keys
    promo_code_input = driver.find_element(By.CLASS_NAME, "promoCode")
    promo_code_input.clear()
    promo_code_input.send_keys("X657YY")

    # Locate the button with the class "promoBtn" and click
    apply_button = driver.find_element(By.CLASS_NAME, "promoBtn")
    apply_button.click()

    # Wait for some time to see the changes (you might need to add a proper wait here)
    driver.implicitly_wait(100)

    # Locate the span element with the class "promoInfo" and check the text content
    promo_info_element = driver.find_element(By.CLASS_NAME, "promoInfo")
    actual_promo_info_text = promo_info_element.text
    expected_promo_info_text = "Invalid code ..!"

    # Check if the expected promo info text matches the actual promo info text
    if expected_promo_info_text == actual_promo_info_text:
        print(
            f"Promo info verification successful. Expected text: '{expected_promo_info_text}', Actual text: '{actual_promo_info_text}'")
    else:
        print(
            f"Promo info verification failed. Expected text: '{expected_promo_info_text}', Actual text: '{actual_promo_info_text}'")

    # Finally, close the browser
    driver.quit()
