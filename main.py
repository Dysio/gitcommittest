# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name: str):
    # Use a breakpoint in the code line below to debug your script.
    '''Function print_hi prints Hi and argument'''
    name = str(name).capitalize()
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def square(num: int):
    square = num**2
    return square


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print_hi('name')
    print(square(5))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
