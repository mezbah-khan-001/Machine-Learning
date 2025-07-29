
#  hello world this mezbah kkhan from backend developer
#  lets create  the project using numpy labs( numpy , pandas , seaborn ) 
#  Lets do this with proper codes 
import numpy as np
import pandas as pd
# Commented out unused heavy libraries (matplotlib, seaborn, sklearn) to trim
# dependency footprint. Uncomment only if needed for plotting or ML tasks.
# import matplotlib.pyplot as plt
# import seaborn as sns
# import sklearn as skn

class FirstCls:
    hello01 = "This is a mini project by Mezbah Khan."
    def __init__(self, names, ages, salaries):
        self.names = np.array(names, dtype=str)
        self.ages = np.array(ages, dtype=int)
        self.salaries = np.array(salaries, dtype=int)

    @staticmethod
    def warn():
        return "The user data is incorrect!"

    def save_user_data(self):
        data = {
            "Names": self.names.tolist(),
            "Ages": self.ages.tolist(),
            "Salaries": self.salaries.tolist()}

        if self.names.size > 0 and self.ages.size > 0 and self.salaries.size > 0:
            with open("demo.txt", "w") as file:
                for key, value in data.items():
                    file.write(f"{key}: {', '.join(map(str, value))}\n")
            print("User data saved successfully!")
        else:
            print(self.warn())

# User Input for First Class ----> 
try:
    names = input("Enter user names (comma-separated): ").split(',')
    ages = list(map(int, input("Enter ages (comma-separated): ").split(',')))
    salaries = list(map(int, input("Enter salaries (comma-separated): ").split(',')))

    first_instance = FirstCls(names, ages, salaries)
    first_instance.save_user_data()
except ValueError:
    print("Error: Please enter valid numbers for ages and salaries.")

class SecondCls(FirstCls):
    hello02 = "This system is created by Mezbah Khan!"

    def __init__(self, names, ages, salaries, data, array):
        super().__init__(names, ages, salaries)
        self.data = np.array(data.split(','), dtype=int)
        self.array = np.array(array.split(','), dtype=int)

    @staticmethod
    def alert():
        return "This system is for storing personal data only!"

    def save_additional_data(self):
        if self.data.size > 0 and self.array.size > 0:
            with open("demo.txt", "a") as file:
                file.write(f"\nStored Data: {', '.join(map(str, self.data))}\n")
                file.write(f"Stored Array: {', '.join(map(str, self.array))}\n")
            print("Additional data saved successfully!")
        else:
            print(self.warn())

# User Input for Second Class ----> 
try:
    data_input = input("Enter your data (comma-separated): ")
    array_input = input("Enter your arrays (comma-separated): ")

    second_instance = SecondCls(names, ages, salaries, data_input, array_input)
    print(second_instance.hello01)
    print(second_instance.hello02)

    second_instance.save_user_data()
    second_instance.save_additional_data()
except ValueError:
    print("Error: Please enter valid integer values for data and arrays.")
try:
    df = pd.read_csv("demo.txt", delimiter=":", header=None, names=["Key", "Value"])
    print("\nSaved Data:\n", df)
except Exception as e:
    print("Error reading file:", e)

      # The code is written by mezbah khan 
      # codes for github projects --> 

   
