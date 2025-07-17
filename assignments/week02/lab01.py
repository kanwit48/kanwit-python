BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese


weight = float(input("Weight: "))
height = float(input("Height: "))
bmi = weight / height ** 2
print("Your BMI: ",bmi)
if bmi < 18.5:
    print("Underweight")
if bmi >= 18.5 and bmi<=24.9:
    print("Normal Weight")
if bmi >= 25.0 and bmi<=29.9:
    print("Overweight")
if bmi >= 30.0:
    print("Obese")
