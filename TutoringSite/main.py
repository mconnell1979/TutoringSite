# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def remove_spaces(string_var):
    string_var = string_var.replace(' ', '')
    my_list = string_var.split(",")
    string_var = string_var.replace('-', ',')
    my_test_list = string_var.split(",")
    print('test:', my_test_list)
    for i in range(0, len(my_test_list)):
        try:
            my_test_list[i] = int(my_test_list[i])
        except ValueError:
            print('Check Your Format')
            return "None"
    # add more code here!
    l = [my_list.index(i) for i in my_list if '-' in i]
    print(l)
    for i in range(0, len(my_list)):
        try:
            my_test_list[i] = int(my_list[i])
        except ValueError:
            print('oops2')
            return "None"
    return my_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

print('Hello World')
str_var = ' 1 -   2,3,   4-5 '
remove_spaces(str_var)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
