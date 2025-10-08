weight = float(input('Enter weight in kg: '))
height = float(input('Enter height in meters: '))

def bmi(weight, height):
    bmi_value = weight / (height **2)
    if bmi_value <= 18.5:
        return "Underweight"
    elif 18.5 < bmi_value <= 25.0:
        return "Normal"
    elif 25.0 < bmi_value <= 30.0:
        return "Overweight"
    else:
        return "Obese"

print(bmi(weight, height))