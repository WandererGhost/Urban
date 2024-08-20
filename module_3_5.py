def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) <= 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))
   

result = get_multiplied_digits(23)
print(result)

#Почему если я убираю конструкцию if - else, то код ломается?
