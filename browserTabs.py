# Jack Wagner
# December, 2019
#
# browserTabs.py
# Attempt at bypassing the Google Foobar Application Process

import webbrowser
import time
from random import *


def load_dict():
    global search_terms_list
    file = open("searchTerms.txt", "r")
    search_terms_list= []

    for line in file:
        search_terms_list.append(line.lower().strip())
    file.close()


def open_tabs(n):
    count = 0
    print(str(len(search_terms_list)) + " terms with " + str(len(search_terms_list)*len(search_terms_list)) + " possible search combos.")
    while count < n:
        # Choose two random words from the list
        random_term_index_1 = randint(0, len(search_terms_list) - 1)
        random_term_index_2 = randint(0, len(search_terms_list) - 1)

        # Randomize selection of Python of Java
        if randint(0, 1) == 0:
            language = "Python"
        else:
            language = "Java"

        combo_search_string = str(search_terms_list[random_term_index_1]) + " and " + str(search_terms_list[random_term_index_2]) + " in " + str(language)
        url = "https://www.google.com.tr/search?q={}".format(combo_search_string)

        webbrowser.open_new_tab(url)    # Open the URL
        wait_sec = randint(2, 4) * random()        # Wait a random amount of seconds
        time.sleep(wait_sec)
        count += 1


load_dict()
open_tabs(10)
