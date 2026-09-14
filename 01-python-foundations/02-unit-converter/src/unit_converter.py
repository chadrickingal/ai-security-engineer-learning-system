# CLI Unit Converter


def findUnit(item, unit):
    match unit:
        case 1: # cm - in
            converted = item * 0.0039370079
            print("\n------------------------------------")
            print("\tcentimeter to inches")
            print("------------------------------------")
            return f"{item}cm --> {converted:.4f}in\n"
        case 2: # mm - in
            converted = item * 0.0003937008
            print("\n------------------------------------")
            print("\tmilimeter to inches")
            print("------------------------------------")
            return f"{item}mm --> {converted:.4f}in\n"
        case 3: # meter - feet
            converted = item * 0.032808399 
            print("\n------------------------------------")
            print("\tmeter to feet")
            print("------------------------------------")
            return f"{item}m --> {converted:.4f}ft\n"
        case 4: # km - miles
            converted = item * 0.0062137119 
            print("\n------------------------------------")
            print("\tkilometer to miles")
            print("------------------------------------")
            return f"{item}km --> {converted:.4f}mi\n"
        case 5: # cm - feet
            converted = item * 0.000328084 
            print("\n------------------------------------")
            print("\tcentimeter to feet")
            print("------------------------------------")
            return f"{item}cm --> {converted:.4f}ft\n"
        case 6: # in - feet
            converted = item * 0.0008333333 
            print("\n------------------------------------")
            print("\tinches to feet")
            print("------------------------------------")
            return f"{item}in --> {converted:.4f}ft\n"
        case 7: # meter - yard
            converted = item * 0.010936133 
            print("\n------------------------------------")
            print("\tmeter to yard")
            print("------------------------------------")
            return f"{item}m --> {converted:.4f}yd\n"
        case 8: # cm - km
            converted = item * 0.0000001
            print("\n------------------------------------")
            print("\tcemtimeter to kilometer")
            print("------------------------------------")
            return f"{item}cm --> {converted:.4f}km\n"
        case _:
            print("Unit Not Found [404]")
        
def inputFromUser():
    try:  
        print("""
        ================================================================
                             CLI UNIT CONVERTER
        ================================================================
        +--------------------------------------------------------------+
        | No. | Units         | No. | Units      | No. | Units         |
        +-----+---------------+-----+------------+-----+---------------+
        | (1) | cm -> in      | (2) | mm -> in   | (3) | meter -> feet |
        +-----+---------------+-----+------------+-----+---------------+
        | (4) | km -> miles   | (5) | cm -> feet | (6) |in -> feet     |
        +-----+---------+-----+-----+------------+-----+---------------+
        | (7) | meter -> yard | (8) | cm -> km   |     |               |
        +--------------------------------------------------------------+
        """)
        print("Please provide values below")
        print("-------------------------------")
        unit = int(input("Unit: "))
        number = float(input("Number: "))

        print(findUnit(number, unit))
    except ValueError:
        print("Invalid input") 


while True:
    inputFromUser()
    print("____________________________________")
    print("You want to convert again? Y/n")
    choice = input(": ").lower()
    if choice == 'n':
        break
    elif choice == 'y':
        pass
    else:
        print("Your Choice not found")
        
    