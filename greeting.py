name = input("What is your last name? ")
gender = input("What is your gender? (m/f) ")
if gender.lower() == "m":
    print(f"Hello Mr. {name}!")
elif gender.lower() == "f":
    print(f"Hello Ms. {name}!")

year = input("What year were you born? ")
