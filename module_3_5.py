def get_multiplied_digits(number):
    str_number = str(number)
    first=int(str_number[0])
    if first == 0:
        return 1
    else:
        if len(str_number)>1:
            return first * get_multiplied_digits(int(str_number[1:]))
        else:
            return first

ishod="00402030000"
ishod = ishod.strip("0")
print(ishod)
result = get_multiplied_digits(int(ishod))
print(result)
