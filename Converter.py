choice=input("What are you converting to? Celsius or Fehrenheit: ")

#Converts from Fahrenheit to Celsius
if choice.lower()=="celsius":
    fehrenheit=float(input("What is the temperature in fehrenheit: "))
    f_to_c=(fehrenheit-32)*5/9
    print(f"The temperature in celsius is: {f_to_c:.2f}")

#Converts from Celsius to Fahrenheit
elif choice.lower()=="fehrenheit":
    celsius=float(input("What is the temperature in celsius: "))
    c_to_f=(celsius*9/5)+32
    print(f"The temperature in fehrenheit is: {c_to_f:.2f}")
    
print("I know I am awesome.")
