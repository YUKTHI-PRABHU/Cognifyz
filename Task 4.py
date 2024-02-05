


temperature = int(input("Enter temperature value "))
select = input("Enter the notation for the entered temperature (celsius) C or (Fahrenheit) F (Kelvin) K ? " )
if select.upper() == "F":
    x = int(round((temperature-32)/9 *5))
    print("Temerature",temperature,select)
    print(x,"C")
if select.upper() == "F":
    x = int(round(((temperature-32)* 5/9)+ 273.15)  )   
    print(x,"K")
if select.upper()=='C':
    x = int(round((temperature *9) /5 +32))
    print(x, "F")
if select.upper()=='C':
    x = int(round((temperature +273.15)))
    print(x, "K")
if select.upper()=='K':
    x = int(round((temperature -273.15)))
    print(x, "C")
if select.upper()=='K':
    x = int(round((temperature -273.15)*9/5 + 32))                    
    print(x, "F")


















