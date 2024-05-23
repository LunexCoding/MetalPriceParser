def convertStringToNumber(number):
    number = number.replace(" ", "")
    try:
        num = float(number)
        if num == 0.0:
            return 0
        else:
            return num
    except ValueError:
        return int(number)
