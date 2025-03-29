import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Configure the website URL and other parameters
WEBSITE_URL = "https://example.com"  # Change this to your target website
WAIT_TIME = 15  # seconds to wait before closing and reloading

def main():
    while True:
        try:
            # Initialize the browser (using Chrome in this example)
            driver = webdriver.Chrome()
            driver.get(WEBSITE_URL)
            
            print(f"Opened {WEBSITE_URL}")
            
            # Maximize window to ensure we can click anywhere
            driver.maximize_window()
            
            # Click at the center of the page
            action = ActionChains(driver)
            action.move_by_offset(100, 100).click().perform()  # Adjust coordinates as needed
            print("Clicked on the page")
            
            # Wait for 15 seconds
            time.sleep(WAIT_TIME)
            
            # Close the browser
            driver.quit()
            print("Browser closed. Restarting...")
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            if 'driver' in locals():
                driver.quit()
            time.sleep(5)  # Wait before retrying

if __name__ == "__main__":
    main()
