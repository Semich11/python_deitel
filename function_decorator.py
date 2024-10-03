def custom(func):
    def inner(*args, **kwargs):
        print("*********************")
        return func(*args, **kwargs)
        # print("*********************")


    return inner

@custom
def display(name):
    return  f"Hello {name}"

print(display("sam"))