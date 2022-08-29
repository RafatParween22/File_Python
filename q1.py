# # f = open("student.txt", "a")
# # f.write("Now the file has more content!")
# # f.close()
# # f = open("student.txt", "r")
# # print(f.read())

# f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

# #open and read the file after the appending:
# f = open("demofile3.txt", "r")
# print(f.read())

# my_file = open("student.txt")
# file_data = my_file.read()
# print (file_data)
# my_file.close()


batch1_students = ["Shivam", "Rahul", "Kavay", "Dhannu", "Deepanshu", "Nitin", "Manoj", "Shakrudin", "Tara", "Suraj", "Krishna"]
students_file = open("navgurukul_students.html", "w")
for student in batch1_students:
    students_file.write("" + student + "\n")
students_file.close()








