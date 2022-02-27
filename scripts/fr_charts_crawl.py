"""
Web crawling script for the french charts
"""
from argparse import ArgumentParser
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import pandas as pd
from time import sleep


first_week = 47
min_year = 1984
max_year = 2021
max_week=52

#official but incomplete
# def get_url_singles(year_n:int, week_n:int):
#     assert min_year <= year_n <= max_year
#     assert 1 <= week_n <= max_week
#     return f"http://snepmusique.com/les-tops/le-top-de-la-semaine/top-albums/?semaine={week_n:02}&annee={year_n:04}&categorie=Top%20Singles"

#official publisher of french charts
def get_url_singles(year_n:int, week_n:int):
    """
    gives you the url for the french billboards for given week

    :param year_n int: year
    :param week_n int: week number (starting from week 1, according to the iso calendar)
    """
    assert min_year <= year_n <= max_year
    assert 1 <= week_n <= max_week
    year_n = year_n % 100
    return f"http://www.chartsinfrance.net/charts/{year_n:02}{week_n:02}/singles.php"


def get_info(el):
    """
    extracts info from a html row extracted from the billboard page

    :param el: selenium element
    """
    return dict(
    position = int(el.find_element_by_class_name("c1_td2").text),
    evol = el.find_element_by_class_name("c1_td3").find_element_by_tag_name("font").text,
    artist = el.find_element_by_css_selector("font.noir13b").text,
    title = el.find_element_by_css_selector("font.noir11").text,
    )


def scrape_charts(output_filename="data/french_charts.csv"):
    """
    Scrapes the french charts, and puts them into output_filename as csv data

    :param output_filename str: output file name.
    """
    # el = elements[0]

    list_of_dicts = []


    driver = webdriver.Firefox()
    driver.get(get_url_singles(min_year, first_week))
    input() #wait for user to accept cookies
    for year in range(min_year, max_year + 1):
        for week in range(1, max_week + 1): 
            if year == min_year and week < first_week:
                continue
            while True:
                try:
                    driver.get(get_url_singles(year, week))
                except TimeoutException:
                    pass
                else:
                    break
                finally:
                    sleep(2)
            # sleep(2)
            elements = driver.find_elements_by_css_selector("div.b572")
            for el in elements:
                values = get_info(el)
                values["year"] = year
                values["week"] = week
                list_of_dicts.append(values)
    driver.close()

    df = pd.DataFrame(list_of_dicts)
    df.to_csv(output_filename)

if __name__ == "__main__":
    parser = ArgumentParser("scrape the french billboards")
    parser.add_argument("filename", default="data/french_charts.csv", type=str,
                        help="the output filename")
    args = parser.parse_args()
    scrape_charts(args.filename)
