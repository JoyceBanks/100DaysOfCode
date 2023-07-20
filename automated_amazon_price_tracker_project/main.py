import requests
import html5lib
import smtplib
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/SGIN-Windows-Laptops-Graphics-Bluetooth/dp/B0C27XP3QV/ref=psdc_565108_t2_B0BL86VM7F?th=1"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 1https://www.amazon.com/SGIN-Windows-Laptops-Graphics-Bluetooth/dp/B0C27XP3QV/ref=psdc_565108_t2_B0BL86VM7F?th=10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}
MY_EMAIL = "EMAIL ADDRESS"
MY_PASSWORD = "PASSWORD"

response = requests.get(url=URL, headers=HEADERS)
product_webpage = response.text

# Note: Website is dynamically generated thus, may have to take a few tries for code to run successfully
soup = BeautifulSoup(product_webpage, "html5lib")
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = float(price.split("$")[1])
print(price_without_currency)

if price_without_currency < 300:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="Destination email address",
            msg=f"Subject: Amazon Price Alert!\n\n SGIN Laptop 15.6 Inch, 4GB DDR4 128GB SSD Windows 11 Laptops "
                f"with Intel Celeron Quad Core J4105(up to 2.5 GHz), Intel UHD Graphics 600, Mini HDMI, WiFi, Webcam"
                f"USB3.0, Bluetooth 4.2 is now ${price_without_currency}"
        )
