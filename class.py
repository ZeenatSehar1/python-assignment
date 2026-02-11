weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

bmi_rounded = round(bmi, 2)

print(f"\nYour BMI is: {bmi_rounded}")

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal weight"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Category: {category}")