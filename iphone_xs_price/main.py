from bs4 import BeautifulSoup
import requests
import pywhatkit
import time
from datetime import datetime
import keyboard as k


def send_message(price, link):
    check__if_already_sent = []
    checked = price in check__if_already_sent
    if not checked:
        check__if_already_sent.append(price)
        message = (
            "UN IPHONE XS A SEULEMENT "
            + str(price)
            + "€ EST EN VENTE SUR BLACKMARKET. CLIQUEZ SUR CE LIEN: "
            + str(link)
        )
        now = datetime.now()
        hour = now.hour
        minute = now.minute

        pywhatkit.sendwhatmsg("+33769531684", message, hour, minute + 1)
        time.sleep(60)
        k.press_and_release("enter")


def check_price(prices_only, link):
    for i in range(len(prices_only)):
        if int(prices_only[i]) <= 350:
            send_message(prices_only[i], link)


def main():
    while True:
        url = "https://www.backmarket.fr/iphone%2Fxs-reconditionnes.html#backbox_grades_list=12%20%C3%89tat%20correct&storage=64000%2064%20Go"
        website = requests.get(url)
        doc = BeautifulSoup(website.text, "html.parser")
        prices_only = []
        result = doc.find_all(class_="_3OcKBk8D _2SrrvPwuOVjCyULC_FKjin")

        for i in range(len(result)):
            result[i] = result[i].string

            result[i] = result[i].strip()
            price = int(result[i][:3:])
            prices_only.append(price)

        check_price(prices_only, url)
        time.sleep(600)


if __name__ == "__main__":
    main()
