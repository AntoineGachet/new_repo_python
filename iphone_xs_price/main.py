from bs4 import BeautifulSoup
import requests
import pywhatkit
import time
from datetime import datetime
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure


def send_message(price, link):
    check__if_already_sent = []
    checked = price in check__if_already_sent
    if not checked:
        account_sid = os.environ["AC85e4f450863b460591651b1dc56c7129"]
        auth_token = os.environ["366308a2515a5b9aaecfc411f5165dda"]
        client = Client(account_sid, auth_token)

        check__if_already_sent.append(price)
        message_body = (
            "UN IPHONE XS A SEULEMENT "
            + str(price)
            + "€ EST EN VENTE SUR BLACKMARKET. CLIQUEZ SUR CE LIEN: "
            + str(link)
        )
        message = client.messages.create(
            body=message_body,
            messaging_service_sid="MGed87f09517167ce400e09e7b4ca0c377",
            to="+33769531684",
        )
        print(message.sid)


def check_price(prices_only, link):
    for i in range(len(prices_only)):
        if int(prices_only[i]) <= 550:
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
        # time.sleep(600)


if __name__ == "__main__":
    main()
