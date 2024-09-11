def average(arg1, *args):
    return (arg1 + sum(args)) / (len(args) + len(str(arg1)))