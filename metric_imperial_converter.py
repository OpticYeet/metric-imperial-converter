import sys
import customtkinter

# set defaults for ctk
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

# gui creation


choice = ""


def convertToKilograms(pounds):
    kilograms = int(pounds) / 2.20462
    kiloRounded = round(kilograms, 2)
    print(f"Kilograms: {kiloRounded}")
    takeInput()


def convertToPounds(kilograms):
    pounds = int(kilograms) * 2.20462
    poundsRounded = round(pounds, 2)
    print(f"Pounds: {poundsRounded}")
    takeInput()


def convertToCelsius(fahrenheit):
    celsius = (int(fahrenheit) - 32) * (5/9)
    celsiusRounded = round(celsius, 2)
    print(f"Celsius: {celsiusRounded}")
    takeInput()


def convertToFahrenheit(celsius):
    fahrenheit = (int(celsius) / (5/9)) + 32
    fahrenheitRounded = round(fahrenheit, 2)
    print(f"Fahrenheit: {fahrenheitRounded}")
    takeInput()

# check metric -> imperial or imperial -> metric


def takeInput():
    print("\n1. Pounds to Kilograms")
    print("2. Kilograms to Pounds")
    print("3. Fahrenheit to Celsius")
    print("4. Celsius to Fahrenheit")
    print("5. Exit")
    choice = input("Choose one: ")
    # Pounds to Kilograms
    if (choice == "1"):
        pounds = input("Please enter weight in pounds: ")
        convertToKilograms(pounds)
    # Kilograms to Pounds
    elif (choice == "2"):
        kilograms = input("Please enter weight in kilograms:")
        convertToPounds(kilograms)
    # Fahrenheit to Celsius
    elif (choice == "3"):
        fahrenheit = input("Please enter degrees in Fahrenheit: ")
        convertToCelsius(fahrenheit)
    # Celsius to Fahrenheit
    elif (choice == "4"):
        celsius = input("Please enter degrees in Celsius: ")
        convertToFahrenheit(celsius)
    # Exit
    elif (choice == "5"):
        sys.exit(0)
    # Exception
    else:
        print("Invalid input. Please try again.")


takeInput()
