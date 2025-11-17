from AnimalObj import Animal

class Bear(Animal):

    numOfBears = 0

    bear_sound = "bellowing roar"

    list_of_bear_names = []
    file_path = r'C:\Users\dr046\Desktop\CIT-95\ZookeepersChallenge\animalNames.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()

        line_num = 1
        for line in lines:
            if line_num == 3:
                list_of_bear_names.extend(line.strip().split(', '))
                break
            else:
                line_num += 1

    #def __init__(self, name = "a_name", animal_id="an_id", birth_date="2099-01"):