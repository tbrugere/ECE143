"""
Web crawling script for the uk charts
"""
from argparse import ArgumentParser
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pandas as pd
from time import sleep
from datetime import date, timedelta

# first_week = 47
# min_year = 1984
# max_year = 2021
# max_week=52

initial_date = date(1952,11,14)

max_date = date(2021, 12, 31)


def weeks(initial_date, max_date):
    """
    iterator over the weeks (as datetime.date) from initial_date to max_date

    :param initial_date date:
    :param max_date date:
    """
    dt = initial_date
    while dt <= max_date:
        year, week, weekday = dt.isocalendar()
        assert weekday == 5 #charts are on fridays!
        yield year, week, dt 
        dt = dt + timedelta(days=7)


def selenium_http_request(driver, address):
    """performs a get request using the javascript api
    and deserializes it
    """
    return driver.execute_async_script("""
                complete = arguments[1];
                fetch(arguments[0])
                    .then(response => response.json())
                    .then(value => complete(value))
                """, address)

#official but incomplete
# def get_url_singles(year_n:int, week_n:int):
#     assert min_year <= year_n <= max_year
#     assert 1 <= week_n <= max_week
#     return f"http://snepmusique.com/les-tops/le-top-de-la-semaine/top-albums/?semaine={week_n:02}&annee={year_n:04}&categorie=Top%20Singles"

#official publisher of french charts
def get_url_singles(d : date):
    """
    gives you the url for the uk billboards for given date

    :param d date:
    """
    return f"https://www.officialcharts.com/charts/singles-chart/{d.year:04}{d.month:02}{d.day:02}/7501"


def get_info(el):
    """
    extracts info from a html row extracted from the billboard page

    :param el: selenium element
    """
    classes = ["position", "last-week", "title", "artist", "label-cat"]
    values = {cl: el.find_element_by_class_name(cl).text for cl in classes}
    tds = el.find_elements_by_tag_name("td")
    pkpos = int(tds[3].text)
    woc = int(tds[4].text)
    values["peak position"] = pkpos
    values["weeks of charts"] = woc
    return values



# el = elements[0]

def scrape_charts(output_filename):
    """
    Scrapes the uk charts, and puts them into output_filename as csv data

    :param output_filename str: output file name.
    """
    list_of_dicts = []

    driver = webdriver.Firefox()
    driver.get(get_url_singles(initial_date))
    input() #wait for user to accept cookies and refuse mailing list

    for year, week, date in weeks(initial_date, max_date):
        while True:
            try:
                driver.get(get_url_singles(date))
            except TimeoutException:
                pass
            else:
                break
            finally:
                sleep(2)
        # sleep(2)
        table = driver.find_element_by_css_selector("table.chart-positions")
        elements = table.find_elements_by_tag_name("tr") #table row
        for el in elements:
            el_cls = el.get_attribute("class").split()
            if "headings" in el_cls or "mobile-actions" in el_cls or "actions-view" in el_cls: continue
            try:
                values = get_info(el)
            except NoSuchElementException:
                continue
            values["year"] = year
            values["week"] = week
            values["date"] = date
            list_of_dicts.append(values)
    driver.close()

    df = pd.DataFrame(list_of_dicts)
    df.to_csv(output_filename)


if __name__ == "__main__":
    parser = ArgumentParser(description="scrape the uk billboards")
    parser.add_argument("filename", default="data/uk_charts.csv", type=str,
                        help="the output filename")
    args = parser.parse_args()
    scrape_charts(args.filename)
