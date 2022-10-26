import requests
import json
import flask
import sqlite3
from pprint import pprint as pp
from creditials_API import tmdb_api_key_v3, tmdb_api_key_v4

#need to work out a cleaner way or having variables accesible across all points?
def show_input():
    show_choice = input('What show are you looking for? ')
    show_choice.title()
    return show_choice

#user menu in separate file

#search by show name - create function
def show_search():
    response_show = requests.get(f"https://api.themoviedb.org/3/search/tv?api_key={tmdb_api_key_v3}&query={show_input()}")
    show_info = response_show.json()

    tv_shows = show_info['results']
    korean_tv_shows = list(filter(is_korean_show, tv_shows))
    first_result = korean_tv_shows.pop(0)
    # second_result = korean_tv_shows.pop(1)
    pp(first_result)
    # pp(second_result) #unit testing - if index doesnt exist, throw a specific error?
    #can i use index and then pop to remove the specific searched show and then return it as a variable? then add that vriable to our db/list
    return korean_tv_shows

# def is_search_correct():
#     is_correct = input("Is this the correct show? Y/N ")
#     if is_correct == 'Y':
#     # append the entry to DB or file
#     elif is_correct == 'N':
#     # pull up second result if available
#     else:
#         print("Input not accepted")
#

# next step is to take the result variable, and add it to our DB or file, depending on what we use

#list(filter(new function to filter name, korean_tv_shows)) - can use this to filter by name specifically
# we could also add in a function to assign each index in the list freom the API ti a popped variable, then the user can select the variable
# and append it to a watch list?

def is_korean_show(tv_dict): #filter function for KR shows
    origin_country_list = tv_dict['origin_country']
    if 'KR' in origin_country_list:
        return True
    else:
        return False


#list(filter(new function to filter name, korean_tv_shows)) - can use this to filter by name specifically

show_search()

def if_not_in_list():
    pass
    #throw error if the index doesnt exist in api list - this is a unit test
#user menu option
def user_menu():
    initial_greeting = "Hello, what would you like to do? \n1) View 'Completed' List \n" \
                       "2) View 'To Watch' List \n3) Add to 'Completed' List \n4) Add to 'To Watch' List \n"
    menu_option = int(input(f"{initial_greeting}Please choose option 1, 2, 3, or 4: "))

    if menu_option == 1:
        pass #this will be a DB print
    elif menu_option == 2:
        pass #this will be a DB print
    elif menu_option == 3:
        pass #add to DB
    elif menu_option == 4:
        pass #add to DB
    else:
        print(f"Input not recognised, try again.")