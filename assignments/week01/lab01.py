# Exercise 1: Personal Profile Creator
print("=== Personal Profile Creator ===")
# Create a program that asks for:
# - Full name
# - Age
# - Email
# - Phone number
# - Favorite hobby
# Then display it as a profile

# Write your solution here:
name = input ("What is your name")
age = input ("How old are you?")
Email = input("What you email")
Phone_number = input ("What is your phone number? :")
hobby = input ("What is your favorite hobby? :")

print("==Your Profile==")
print("Full name: ",full_name)
print("Age: ",age)
print("Email: ",email)
print("Phone number: ",phone_number)
print("Favorite Hobby: ",hobby)




def weather_suggestion(temp):
    if temp >35:
        print("very hot,stay indoor")
    elif  25 <= temp <=35:
        print("nice weather")
    elif  20<= temp <=24:
        print("quite cool")
    else #temp <20
        print("cool,wear jacket")
temps = [38,30,22,18]
for t in temps
    print(f"Temperature{t}:{weather_suggestion(t)}")
