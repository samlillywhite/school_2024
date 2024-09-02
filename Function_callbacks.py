def my_function():
    print("Hello from my_function!")


def function_that_takes_a_callback(callback):
    print("Before calling the callback")
    print(type(callback))
    callback()
    print("After calling the callback")


function_that_takes_a_callback(my_function)