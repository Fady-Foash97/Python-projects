def temp_conv():
  while True:
       ## Greeting message
       print("Welcome to the Temperature Converter ")
       ## Declare values for Celsius and Fahrenheit variables
       Celsius = "C"
       Fahrenheit = "F"
       ## Conversion question 
       user_input = input("Which conversion you want to perform: Celsius (C) to Fahrenheit (F) or Fahrenheit (F) to Celsius (C)? ")
       ## if conditions
       if user_input == Celsius:
         var_c = float(input("Enter the temperature in Celsius: "))    # Var_c is the written value for the Celsius variable
         # Conversion formula for converting Fahrenheit to Celsius
         var_f = (var_c * 9/5) + 32
         print(f"The temperature in Fahrenheit is {var_f: .2f}°F  ")
         repeat = input("Do you want to perform another conversion? (yes/no) ")
         if repeat == "yes":
            continue
         elif repeat == "no":
            print("Thank you for using the temperature converter!")
            break
       elif user_input == Fahrenheit:
         var_f = float(input("Enter the temperature in Fahrenheit: "))   # Var_f is the written value for the Fahrenheit variable
         # Conversion formula for converting Celsius to Fahrenheit
         var_c = (var_f - 32) * 5/9  
         print(f"The temperature in Celsius is {var_c: .2f} °C ")
         repeat = input("Do you want to perform another conversion? (yes/no) ")
         if repeat == "yes":
            continue
         elif repeat == "no":
            print("Thank you for using the temperature converter!")
            break

        
temp_conv()