#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    list = dir(hidden_4)
    for module in list:
        if '__' not in module:
            print("{}".format(module))
