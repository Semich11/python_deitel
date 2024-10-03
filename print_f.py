from random import randrange


# print("My name is {1}, my Age is {0}, my phone number is 080{0}{0}{0}{0}{0}{0}".format( "12", "Ola"))

class Account:
    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone
        self.__balance = 0.0
        self.account_number = self.__generate_account_number()

    @property  #property is a class function, we use it to annotate an instance method creation "usually, an instance method declaration should come after this annotation."

    def __phone(self):
        # creating a getter for instance variable "__phone". # we must use the name of the instance variable we are creating a getter method for.

        return self.samad #Note!: I use any name here(samad), the name can be anything "You can use your name"# the name i use here must be the name I will use in setting the instance variable

    @__phone.setter # In line 15 we create a property(__phone) which is the getter method for instance variable __phone. and now we are setting the __phone instance variable using the __phone property.
    def __phone(self, phone_number): # the setter method name should be the name of the instance variable we want to set.
        if len(phone_number) != 11:
            raise ValueError("Invalid Phone Number")
        self.samad  = phone_number # I made mention of the name samad in line 18, that the name of that I use to set the instance variable here will be the same name that I'm returning in the getter method. and the name can be any name.

    def __generate_account_number(self):
        return "222" + str(randrange(1000000, 9999999))

    def __str__(self):
        return f"""
        name: {self.__name}
        balance: {self.__balance}
        phone: {self.__phone}
        account_number: {self.account_number}"""


account = Account("chris", "07062206145", )
print(Account.__dict__)
