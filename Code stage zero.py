# Assignment for the leucine group

# Topic Covered: Coding Syntax, Dat types and Data structures

# Task: Present in a Data structure of our choice with a specific programming language : R or Python
# these information's: our names, Sclack username, Email, Hobby, Countries, Disciplines, Preferred Programming language

# Solution:

# We decide to use the dictionary, which is a collection of key-value pairs

Group_description = {
    "Member_1": {
        "Names": "TCHOUTANG Ange Maxime",
        "Sclack Username": "Ange",
        "Email": "angemaxime61@gmail.com",
        "Hobby": "Basketball",
        "Discipline": "Biotechnology",
        "Country": "Cameroon",
        "Preferred Programming Language": "R"
    },
    "Member_2": {
        "Names": "OLORI Oghenemaero Oghale",
        "Sclack Username": "Oghale",
        "Email": "oghenemaero.oloripgs@stu.cu.edu.ng",
        "Hobby": "Coding",
        "Discipline": "Bio-informatics",
        "Country": "Nigeria",
        "Preferred Programming Language": "Python"   
    },
    "Member_3": {
        "Names": "ABDULRAHMAN Olamilekan Raji",
        "Sclack Username": "Raji",
        "Email": "rajiabdulrahman6@gmail.com",
        "Hobby": "Studying",
        "Discipline": "Biochemistry and Biotechnology",
        "Country": "Nigeria",
        "Preferred Programming Language": "Python"
    },
    "Member_4": {
        "Names": "SAKSHI Mohta",
        "Sclack Username": "Sakshi",
        "Email": "sakshimohta2018@gmail.com",
        "Hobby": "Playing chess",
        "Discipline": "Biotechnology",
        "Country": "India",
        "Preferred Programming Language": "Python"
    }
}

print(Group_description)

# How to have each team members information's: 

print(Group_description["Member_1"]) # All information's available for the Team member 1
print(Group_description["Member_2"]) # All information's available for the Team member 2
print(Group_description["Member_3"]) # All information's available for the Team member 3
print(Group_description["Member_4"]) # All information's available for the Team member 4


# How to have each members information's using one single print statement

print(
    "Member_1:", Group_description["Member_1"], "\n",
    "Member_2:", Group_description["Member_2"], "\n",
    "Member_3:", Group_description["Member_3"], "\n",
    "Member_4:", Group_description["Member_4"]
)


