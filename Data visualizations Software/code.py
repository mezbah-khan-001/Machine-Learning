# hello wrold this is mezbah khan from backend developer 
# Lets create the program of data visualizations with pylabs (numpy, matplotlib, seaborn )
# Lets do this with proper codes and modules 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from faker import Faker
import seaborn as sns

# First Class - Handles basic user input and data storage
class FirstCls:
    greeting = 'Welcome to this project!'
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    @staticmethod
    def warn():
        print('[ERROR] Invalid data input!')

    def save_user_data(self):
        if isinstance(self.name, str) and isinstance(self.age, int) and isinstance(self.salary, int): 
            with open('user_data.txt', 'a') as file:
                file.write(f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}\n')
            return {'Name': self.name, 'Age': self.age, 'Salary': self.salary}
        else: 
            return self.warn()
    
    def create_dataset(self):
        try:
            dataset = {
                'Name': [str(i).strip() for i in self.name.split(',')],
                'Age': [int(x) for x in self.age.split(',')],
                'Salary': [int(s) for s in self.salary.split(',')]}
            return dataset
        except ValueError:
            print('[ERROR] Please enter valid numeric values for age and salary!')
            return {}

# Second Class - Inherits FirstCls, Generates AI-generated random data ---> 
class SecondCls(FirstCls):
    greeting = 'This project is created by Mezbah Khan!'
    
    def __init__(self, name, age, salary, start, stop):
        super().__init__(name, age, salary)
        self.start = start
        self.stop = stop
    
    @staticmethod
    def alert(): 
        return '[ERROR] System only stores int64 and str128 values!'
    
    def generate_ai_dataset(self): 
        try:
            fake = Faker()
            dataset = {
                'Name': [fake.name() for _ in range(10)],
                'Age': np.random.randint(18, 65, 10),
                'Salary': np.random.randint(30000, 120000, 10)
            }
            return dataset
        except Exception as e: 
            print(f'[ERROR] Data generation failed: {e}')
            return {}

# Third Class - Handles Visualization ---> 
class ThirdCls(SecondCls): 
    greeting = 'This project can also store and visualize data!'
    
    def __init__(self, name, age, salary, start, stop):
        super().__init__(name, age, salary, start, stop)
    
    @classmethod
    def get_choice(cls): 
        print('\n[1] Enter your data and visualize (Human dataset)')
        print('[2] Generate random AI data and visualize')
        choice = input('Enter your choice (1 or 2): ')
        
        if choice == '1':
            name_input = input('Enter user names (comma-separated): ')
            age_input = input('Enter user ages (comma-separated): ')
            salary_input = input('Enter user salaries (comma-separated): ')
            
            instance = cls(name_input, age_input, salary_input, 0, 0)
            data = instance.create_dataset()
            
            if data:
                df = pd.DataFrame(data)
                print(df)
                sns.barplot(x='Age', y='Salary', data=df, palette='coolwarm')
                plt.grid(True)
                plt.xlabel('Age')
                plt.ylabel('Salary')
                plt.title('Age vs Salary Distribution')
                plt.show()
        
        elif choice == '2': 
            instance = cls('', '', '', 0, 0)
            data = instance.generate_ai_dataset()
            
            if data:
                df = pd.DataFrame(data)
                print(df)
                sns.barplot(x='Age', y='Salary', data=df, palette='coolwarm')
                plt.grid(True)
                plt.xlabel('Age')
                plt.ylabel('Salary')
                plt.title('AI Generated Age vs Salary Distribution')
                plt.show()
        
        else: 
            print('[ERROR] Invalid choice! Please enter 1 or 2.')

# Fourth Class - Extends ThirdCls
class FourthCls(ThirdCls): 
    greeting = 'This project can handle multiple data inputs and visualizations!'
    
    def __init__(self, name, age, salary, start, stop):
        super().__init__(name, age, salary, start, stop)

# Run the program
if __name__ == '__main__':
    FourthCls.get_choice()

