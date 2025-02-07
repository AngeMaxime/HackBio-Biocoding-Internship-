# Assignment Stage Zero

# https://github.com/sakshimohta17/hackbio-biocoding-internship/blob/main/stage-0/Task1 : sakshi accounts
# https://www.linkedin.com/in/sakshimohta1705 : Sakshi

# https://github.com/AngeMaxime/HackBio-Biocoding-Internship-: Ange accounts
# https://www.linkedin.com/in/%F0%9F%A7%ACtchoutang-ange-maxime-834b6729a

# https://github.com/maero1 : Maero Olori Accounts
# https://www.linkedin.com/in/maeroolori/


# Task: Present in a Data structure of your choice with a specific programming language : R or Python
# these information's:  The names, Sclack username, Email, Hobby, Countries, Disciplines and Preferred Programming language of all member of your team

# Solution:

# We decide to use Python and used a nested-List, which stores data row-wise, with each row representing a different category of information.

hackBio_interns = [["Sakshi Mohta", "ABDULRAHMAN Olamilekan Raji", "OLORI Oghenemaero Oghale", "TCHOUTANG Ange Maxime"], 
["Sakshi","Raji", "Maero","Ange"], ["sakshimohta2018@gmail.com", " rajiabdulrahman6@gmail.com", "oghenemaero.oloripgs@stu.cu.edu.ng",
"angemaxime61@gmail.com"], ["Playing chess", "Studying","Coding","Basketball"],["India","Nigeria","Nigeria","Cameroon"],
["Biotechnology","Biochemistry and Biotechnology","Bioinformatics","Biotechnology"],["Python","Python","Python","R"]]

# 1- The list is called 'hackBio_interns'
# 2- It contains 6 sublist, the sublist are devised into 6: the intern's name, Slack username, emails, hobbies, countries, disciplines, and preferred programming languages.
# 3- For each rows in the list :

# Row 0 → Names of the interns.
# Row 1 → Slack usernames.
# Row 2 → Emails.
# Row 3 → Hobbies.
# Row 4 → Countries.
# Row 5 → Disciplines.
# Row 6 → Preferred programming languages.


print("HackBio Interns Information:\n" +
      "Name: " + hackBio_interns[0][0] + ", Slack Username: " + hackBio_interns[1][0] + ", Email: " + hackBio_interns[2][0] + ", Hobby: " + hackBio_interns[3][0] + ", Country: " + hackBio_interns[4][0] + ", Discipline: " + hackBio_interns[5][0] + ", Preferred Programming Language: " + hackBio_interns[6][0] + "\n" +
      "Name: " + hackBio_interns[0][1] + ", Slack Username: " + hackBio_interns[1][1] + ", Email: " + hackBio_interns[2][1] + ", Hobby: " + hackBio_interns[3][1] + ", Country: " + hackBio_interns[4][1] + ", Discipline: " + hackBio_interns[5][1] + ", Preferred Programming Language: " + hackBio_interns[6][1] + "\n" +
      "Name: " + hackBio_interns[0][2] + ", Slack Username: " + hackBio_interns[1][2] + ", Email: " + hackBio_interns[2][2] + ", Hobby: " + hackBio_interns[3][2] + ", Country: " + hackBio_interns[4][2] + ", Discipline: " + hackBio_interns[5][2] + ", Preferred Programming Language: " + hackBio_interns[6][2] + "\n" +
      "Name: " + hackBio_interns[0][3] + ", Slack Username: " + hackBio_interns[1][3] + ", Email: " + hackBio_interns[2][3] + ", Hobby: " + hackBio_interns[3][3] + ", Country: " + hackBio_interns[4][3] + ", Discipline: " + hackBio_interns[5][3] + ", Preferred Programming Language: " + hackBio_interns[6][3])

# Using this print statement: 

# 1- Strings are concatenates using + to display information for each intern.
# 2- All four interns' information are print in a structured way
# 3- The first intern’s details can be accessed using hackBio_interns[x][0]
# 4- The second intern’s details can be accessed using hackBio_interns[x][1]
# 5- The \n (newline character) is used to insert a line break in the string, moving the cursor to a new line


