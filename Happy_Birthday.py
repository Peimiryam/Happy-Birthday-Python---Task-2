#ask for recipient name
a = input("Tell me a name ")

from datetime import datetime

#Get the current date
now = datetime.now()

#Ask for the birthday date
print("Enter the date of birth(YYYY-MM-DD): ")
dob_input = input()

#Parse the user's input into a datetime object
birthday = datetime.strptime(dob_input, "%Y-%m-%d")

#Calculate the difference between the current date and birthday
difference = now - birthday

#calculate the person's age in years
age_in_years = difference.days //365

b = input("we are almost done, write a personalized message: ")

c = input("and finally, who are you? ")

print("gimme a sec to elaborate it for you")
      
print("...")
print("...")
print("...")

print("Dear " + a)

print("Let's celebrate your birthday!")

print(f"You are {age_in_years} years old now. we want to celebrate your birthday, wishing you a day filled with joy and laughter. ")

print("This is an important day for you. I would like to tell you something special: " + b)

print("With love and best wishes, yours " + c)
