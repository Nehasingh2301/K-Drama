from show_search_functions import show_search

def is_search_correct():
    is_correct = input("Is this the correct show? Y/N ")
    if is_correct == 'Y':
        print("Correct")
        # append the entry to DB or file
    elif is_correct == 'N':
        print("Wrong")
        # pull up second result if available
    else:
          print("Input not accepted")
    return is_correct


is_search_correct()
if __name__ == '__main__':
    show_search()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
