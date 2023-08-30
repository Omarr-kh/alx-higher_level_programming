#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        x = fct(*args)
        return x
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
