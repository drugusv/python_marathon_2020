#convertire celsius in fahrenheit si invers

temp_f = float(input("Introduceti temperatura in Fahrenheit: "))
cels = ((temp_f - 32) * 5/9)
print('%.2f Fahrenheit sunt: %0.2f Celsius' %(temp_f, cels))

temp_c = float(input("Introduceti temperatura in Celsius: "))
farh = ((temp_c * 9/5) + 32)
print("%.2f Celsius sunt: %0.2f Fahrenheit" %(temp_c, farh))
