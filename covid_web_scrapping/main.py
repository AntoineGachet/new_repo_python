from bs4 import BeautifulSoup
import requests
import datetime


class Covid_cases:
    def __init__(self, starting_date, ending_date):
        self.starting_date = starting_date
        self.ending_date = ending_date
        self.every_date = list

    def int_diffrente_date(self):
        starting_date = self.starting_date.split("-")
        ending_date = self.ending_date.split("-")

        start_date = datetime.date(
            int(starting_date[0]), int(starting_date[1]), int(starting_date[2])
        )
        end_date = datetime.date(
            int(ending_date[0]), int(ending_date[1]), int(ending_date[2])
        )
        delta = datetime.timedelta(days=1)

        while start_date <= end_date:
            date = str(start_date)

            self.every_date.append(date)
            start_date += delta
        return self.every_date

    url = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data"
    website = requests.get(url)


class Cases_over_time(Covid_cases):
    def __init__(self, first_country, second_country=None):
        super().__init__()
        self.first_country = first_country
        self.second_country = second_country

    def url(self):
        url1 = (
            "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_" + self.first_country
        )
        url2 = (
            "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_" + self.second_country
        )
        result1 = requests.get(url1)
        result2 = requests.get(url2)
        first_doc = BeautifulSoup(result1.text, "html.parser")
        second_doc = BeautifulSoup(result2.text, "html.parser")

        return first_doc, second_doc

    def find_cases(self, first_doc, second_doc, total_day):
        for n in range(total_day):
            if n == 31:
                n = 0


class Death(Cases_over_time):
    pass


class Compare(Cases_over_time):
    pass


get_total_day = Covid_cases("2021-08-21", "2021-08-29")
total_day = get_total_day.int_diffrente_date()
print(total_day)
b = Cases_over_time("France", "Brazil")
a, c = b.url()
print(b.find_cases(a, c))
