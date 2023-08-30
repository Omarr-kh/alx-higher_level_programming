#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = []

    for idx in range(list_length):
        try:
            n_list.append(my_list_1[idx] / my_list_2[idx])
        except ZeroDivisionError:
            n_list.append(0)
            print('division by 0')
            continue
        except IndexError:
            n_list.append(0)
            print('out of range')
            continue
        except TypeError:
            n_list.append(0)
            print('wrong type')
            continue
        finally:
            pass
    return n_list
