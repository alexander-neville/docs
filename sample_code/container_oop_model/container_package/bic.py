def add_check_sum(function):

    def wrap(*args, **kwargs):

        bic = function(*args, **kwargs)
        serial = bic[-5:]
        total = 0
        for number in serial:

            total += int(number)

        check_sum = total % 11

        bic += str(check_sum)

        return bic

    return wrap



@add_check_sum
def new_bic(owner, container_type, serial):

    bic = owner + container_type + serial

    return bic
