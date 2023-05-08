import socket
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_employee_data_from_browser():
    # create a new Chrome browser window
    browser = webdriver.Chrome()

    # navigate to the page with the employee data form
    browser.get("http://localhost:5000")

    # fill out the form and submit it
    first_name_field = browser.find_element(By.NAME, "first_name")
    first_name_field.send_keys("John")

    last_name_field = browser.find_element(By.NAME, "last_name")
    last_name_field.send_keys("Doe")

    age_field = browser.find_element(By.NAME, "age")
    age_field.send_keys("30")

    currently_employed_field = browser.find_element(By.NAME, "currently_employed")
    currently_employed_field.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # wait for the response page to load and extract the JSON data
    json_data = browser.find_element(By.CSS_SELECTOR, "pre").text

    # close the browser window
    browser.quit()

    return json_data


def connect_to_server():
    # create socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    server_address = ('localhost', 8001)

    # connect to the server
    try:
        client_socket.connect(server_address)
    except Exception as e:
        print(f"Error connecting to server: {e}")
        return

    # get employee data from browser
    json_data = get_employee_data_from_browser()

    # send employee data to server
    try:
        client_socket.send(json_data.encode())
    except Exception as e:
        print(f"Error sending data to server: {e}")

    client_socket.close()

if __name__ == '__main__':
    connect_to_server()
