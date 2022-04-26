def even_number_of_evens(numbers):
    if isinstance(numbers, list):
        if numbers == []:
            return False
        else:
            return True
    else:
        raise TypeError("A list was not passed into the function")

if __name__ == '__main__':
    print(even_number_of_evens(5))