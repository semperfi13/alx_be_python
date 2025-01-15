from error_class import ErroClass

product = {"bean": 12, "apple": 0, "orange": 12, "eat": 0}


def inventory(item, quantity):
    try:
        if product[item] == 0:
            raise ErroClass(item)
        else:
            print(f"Purchase successfull: {quantity} {item} (s)")
            product[item] -= quantity
    except KeyError:
        print(f"Sorry, '{item}' is not available in our inventory")


try:
    inventory("mannna", 12)
except ErroClass as e:
    print(e)
