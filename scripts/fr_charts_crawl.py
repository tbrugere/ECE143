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
    assert min_year <= year_n <= max_year
    assert 1 <= week_n <= max_week
    year_n = year_n % 100
    return f"http://www.chartsinfrance.net/charts/{year_n:02}{week_n:02}/singles.php"


def get_info(el):
    return dict(
    position = int(el.find_element_by_class_name("c1_td2").text),
    evol = el.find_element_by_class_name("c1_td3").find_element_by_tag_name("font").text,
    artist = el.find_element_by_css_selector("font.noir13b").text,
    title = el.find_element_by_css_selector("font.noir11").text,
    )



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
df.to_csv("./french_charts.csv")
