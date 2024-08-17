from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

base_dir = os.path.dirname(os.path.abspath(__file__))
screenshot_dir = os.path.join(base_dir, "../screenshots")
report_dir = os.path.join(base_dir, "../reports")

if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

if not os.path.exists(report_dir):
    os.makedirs(report_dir)

def take_screenshot(driver, filename):
    filepath = os.path.join(screenshot_dir, filename)
    driver.save_screenshot(filepath)

def log_to_report(message):
    with open(os.path.join(report_dir, "test_report.txt"), "a") as report_file:
        report_file.write(message + "\n")

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

try:
    # Step 1: Login
    try:
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        take_screenshot(driver, "log_in.png")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        log_to_report("Step 1: Logged in successfully.")
    except Exception as e:
        log_to_report(f"Step 1: Login failed. Error: {str(e)}")

    # Step 2: Agregar productos al carrito
    try:
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        take_screenshot(driver, "products_added.png")
        time.sleep(2)
        log_to_report("Step 2: Products added to the cart successfully.")
    except Exception as e:
        log_to_report(f"Step 2: Products added to the cart failed. Error: {str(e)}")
    
    # Step 3: Acceder al carrito
    try:
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)
        take_screenshot(driver, "cart_accessed.png")
        log_to_report("Step 3: Accessed the shopping cart successfully.")
    except Exception as e:
        log_to_report(f"Step 3: Access to the shopping cart failed. Error: {str(e)}")
    
    # Step 4: Verificar productos en el carrito
    try:
        cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        assert any("Sauce Labs Backpack" in item.text for item in cart_items)
        assert any("Sauce Labs Bike Light" in item.text for item in cart_items)
        log_to_report("Step 4: Products verified in the cart successfully.")
    except AssertionError:
        log_to_report("Step 4: Product verification in the cart failed.")
    except Exception as e:
        log_to_report(f"Step 4: Error during product verification in the cart. Error: {str(e)}")

    # Step 5: Completar el formulario de compra
    try:
        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.ID, "first-name").send_keys("Daniel")
        driver.find_element(By.ID, "last-name").send_keys("Bejarano")
        driver.find_element(By.ID, "postal-code").send_keys("Guayaquil")
        driver.find_element(By.ID, "continue").click()
        time.sleep(2)
        take_screenshot(driver, "checkout_form_completed.png")
        log_to_report("Step 5: Checkout form completed successfully.")
    except Exception as e:
        log_to_report(f"Step 5: Checkout form completion failed. Error: {str(e)}")
    
    # Step 6: Verificar precios
    try:
        item_total = driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
        tax = driver.find_element(By.CLASS_NAME, "summary_tax_label").text
        total = driver.find_element(By.CLASS_NAME, "summary_total_label").text
        
        assert "$39.98" in item_total
        assert "$3.20" in tax
        assert "$43.18" in total
        log_to_report("Step 6: Prices verified successfully.")
    except AssertionError:
        log_to_report("Step 6: Price verification failed.")
    except Exception as e:
        log_to_report(f"Step 6: Error during price verification. Error: {str(e)}")
    
    # Step 7: Completar la compra
    try:
        driver.find_element(By.ID, "finish").click()
        time.sleep(2)
        take_screenshot(driver, "purchase_completed.png")
        log_to_report("Step 7: Purchase completed successfully.")
    except Exception as e:
        log_to_report(f"Step 7: Purchase completion failed. Error: {str(e)}")
    
    # Step 8: Verificar mensaje de confirmación
    try:
        confirmation_message = driver.find_element(By.CLASS_NAME, "complete-header").text
        assert confirmation_message == "Thank you for your order!"
        log_to_report("Step 8: Order confirmation message verified successfully.")
    except AssertionError:
        log_to_report("Step 8: Order confirmation message verification failed.")
    except Exception as e:
        log_to_report(f"Step 8: Error during order confirmation message verification. Error: {str(e)}")
    
finally:
    driver.quit()
