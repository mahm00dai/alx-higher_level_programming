#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    
    for i in range(list_length):
        try:
            # Try dividing corresponding elements from both lists
            result = my_list_1[i] / my_list_2[i]
        except IndexError:
            # Handle case where one of the lists is too short
            print("out of range")
            result = 0
        except TypeError:
            # Handle case where the elements are not integers or floats
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            # Handle division by zero case
            print("division by 0")
            result = 0
        finally:
            # Append result (either the division or 0 in case of an error)
            new_list.append(result)
    
    return new_list
