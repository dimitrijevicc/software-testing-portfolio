from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# Podesite putanju do GeckoDriver-a
geckodriver_path = r"D:\geckodriver-v0.36.0-win64\geckodriver.exe"

# Kreirajte Service objekat
service = Service(executable_path=geckodriver_path)

# Podesite opcije za Firefox
options = Options()
options.headless = False  # Postavite na True ako želite da Firefox radi u headless režimu

# Inicijalizujte WebDriver
driver = webdriver.Firefox(service=service, options=options)

# Otvorite stranicu
driver.get("https://practice.expandtesting.com/login")

# Pronađite polja za korisničko ime i lozinku
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

# Unesite kredencijale
username_field.send_keys("practice")
password_field.send_keys("SuperSecretPassword!")

# Kliknite na dugme za prijavu
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Sačekajte da se stranica učita
driver.implicitly_wait(5)

# Proverite da li je prijava uspešna
if "Welcome" in driver.page_source:
    print("Prijava je uspešna!")
else:
    print("Prijava nije uspela.")

# Zatvorite pretraživač
driver.quit()
