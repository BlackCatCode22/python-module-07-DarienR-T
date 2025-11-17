# "Driver" file for the zookeeper application

#from AnimalObj import Animal
from BearObj import Bear

from datetime import date

#create list of bears
list_of_bears = []

#calc bday
current_year = date.today().year

def calc_birth_date(the_season, the_years):
    year_of_birthday = int(current_year) - int(the_years)

    month_day = ""

    if "spring" in the_season:
        month_day = str(year_of_birthday) + "-03-21"
    elif "summer" in the_season:
        month_day = str(year_of_birthday) + "-06-21"
    elif "fall" in the_season:
        month_day = str(year_of_birthday) + "-09-21"
    elif "winter" in the_season:
        month_day = str(year_of_birthday) + "-12-21"
    else:
        month_day = str(year_of_birthday) + "-01-01"

    return month_day

def process_one_line(one_line):

    parts = one_line.strip().split(",")
    a_species = parts[0]
    a_season = parts[1]
    a_years = parts[2]

    a_birth_date = calc_birth_date(a_season, a_years)

    # create the animal based on its species
    if a_species.lower() == "bear":
        new_animal = Bear(a_species, a_season, a_years, a_birth_date)
        list_of_bears.append(new_animal)

    return new_animal

def main():
    print("Welcome to the Zoo Keepers application!\n")

    sample_lines = [
        "bear,spring,5",
        "bear,fall,2",
        "bear,winter,7"
    ]

    for line in sample_lines:
        new_bear = process_one_line(line)
        print(f"added {new_bear.species} born on {new_bear.birth_date}")

    print("\nAll bears in the zoo:")
    for bear in list_of_bears:
        print(f"{bear.species}: {bear.birth_date}")

if __name__ == "__main__":
    main()