"""
Practice 3
Name: 蔡淵丞
Student Number: 110502567
Course 2021-CE1003-B
"""
def create_file():
    file = input("Creat a file: ")
    text = input("Write something: ")
    opened_file = open(file,'w')
    opened_file.write(text)
    opened_file.close()
    print("File name",file)
    print("Context:",text)

create_file()