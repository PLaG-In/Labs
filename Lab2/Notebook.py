#PyCharm 2018.1, Python 3.5
#Алитов Владимир Валерьевич
#ПСм-22
#Алгоритмическая задача II
#Прмерно 20 минут
#O(n)
#Храним данные в массиве notebook_array. Ищем элементы перебором массива и определяем их с помощью startswith


notebook_array = []


def find_contacts(input_str):
    count = 0
    for i in range(len(notebook_array)):
        if notebook_array[i].startswith(input_str):
            count += 1
    print(input_str + " -> " + str(count))


def add_contact(input_str):
    if input_str not in notebook_array:
        notebook_array.append(input_str)
        print("Added contact: " + input_str)
    else:
        print("This contact already exists.")


def main():
    print("Example of commands: Add _name_, Find _name_, Exit")
    input_str = input("Enter command: ").lower()
    if input_str.startswith("add "):
        input_str = input_str[4:]
        add_contact(input_str)
    elif input_str.startswith("find "):
        input_str = input_str[5:]
        find_contacts(input_str)
    elif input_str.startswith("exit"):
        print("Program is finished")
        quit()
    else:
        print("Invalid command, try again.")
    main()


main()
