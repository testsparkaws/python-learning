# BMI = Calcute BMI Weight(kg) / Height(m)^2
# BMI = weight(kg)/height(cm)/height(cm) * 10000

weight = float(input("Enter Weight in KG: "))
height = float(input("Enter Height in m: "))
bmi = weight / height**2
print("Your BMI is : ", bmi)
print("Your BMI is : ", format(bmi,'.2f'))
# 
#height = int(input("Enter Height in CM: "))
#bmi = weight / height/height/height * 10000
#print(bmi)
