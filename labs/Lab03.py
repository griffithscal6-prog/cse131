# ------------------------------------------------------------
# 1. Name:
#      Calvin Griffiths
# 2. Assignment Name:
#      Lab 03: Calendar
# 3. Assignment Description:
#      This program displays a calendar for any month and year
#      from 1753 onward. It calculates the number of days in
#      the requested month, determines the day of the week on
#      which the month begins, and displays the calendar.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was determining the day of the week for
#      the first day of a month without using Python's datetime
#      library or a calendar formula. I had to count the number
#      of days from January 1, 1753 and account for leap years.
#
#      Another challenging part was making sure the input
#      validation worked correctly for both the month and year
#      and that the calendar displayed the days in the correct
#      columns.
# 5. How long did it take for you to complete the assignment?
#      It took me approximately 2 hours to complete the assignment, including the time spent on designing the program, (including the: Structure Chart, Pseudocode, and flow chart for the week of lab02), writing the code, and testing it to ensure it worked correctly.
# ------------------------------------------------------------

def display_table(dow, num_days):
    '''Display a calendar table'''
    assert(type(num_days) == type(dow) == type(0))
    assert(0 <= dow <= 6)
    assert(28 <= num_days <= 31)

    # Display a nice table header
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week
    for indent in range(dow):
        print("    ", end='')

    # Display the days of the month
    for dom in range(1, num_days + 1):
        print(repr(dom).rjust(4), end='')
        dow += 1
        # Newline after Saturdays
        if dow % 7 == 0:
            print("") # newline

    # We must end with a newline
    if dow % 7 != 0:
        print("") # newline

def is_leap_year(year):
    """Return True if year is a leap year."""
    assert year >= 1753

    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def days_in_month(month, year):
    """Return the number of days in a given month."""
    assert 1 <= month <= 12
    assert year >= 1753

    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31

    if month in [4, 6, 9, 11]:
        return 30

    if is_leap_year(year):
        return 29

    return 28


def get_integer(prompt):
    """Prompt until the user enters a valid integer."""
    while True:
        value = input(prompt)

        try:
            return int(value)
        except ValueError:
            print("Error: Please enter a valid integer.")


def get_year(prompt):
    """Prompt until the user enters a valid year."""
    while True:
        year = get_integer(prompt)

        if year >= 1753:
            return year

        print("Error: Year must be 1753 or later.")


def get_month(prompt):
    """Prompt until the user enters a valid month."""
    while True:
        month = get_integer(prompt)

        if 1 <= month <= 12:
            return month

        print("Error: Month must be between 1 and 12.")

def compute_offset(month, year):
    total_days = 0

    # Count all days in the complete years before the requested year
    for current_year in range(1753, year):
        total_days += 365

        if is_leap_year(current_year):
            total_days += 1

    # Count all days in the complete months before the requested month
    for current_month in range(1, month):
        total_days += days_in_month(current_month, year)

    # Calculate the day of the week
    dow = (total_days + 1) % 7

    return dow





def main():
    print("Days of the Month Calculator")
    month = get_month(prompt="Please Enter a valid month (1-12): ")
    year = get_year(prompt="Please Enter a valid year (1753 or later): ")

    num_days = days_in_month(month, year)
    dow = compute_offset(month, year)

    display_table(dow, num_days)



if __name__ == "__main__":
    main()