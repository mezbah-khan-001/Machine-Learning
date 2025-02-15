#  hello world this mezbah kkhan from backend developer
#  lets create  the project using numpy labs( numpy , pandas , seaborn ) 
#  Lets do this with proper codes 

import numpy as np
import pandas as pd

class BankSystem:
    """Base class for bank account management."""
    data_file = "bank_data.csv"
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.account_number = self.generate_account_number()
    
    def generate_account_number(self):
        """Generate a unique 10-digit account number."""
        return np.random.randint(1000000000, 9999999999)
    
    def save_to_file(self):
        """Save user details to a CSV file."""
        data = pd.DataFrame([[self.name, self.age, self.salary, self.account_number]],
                            columns=["Name", "Age", "Salary", "Account Number"])
        try:
            existing_data = pd.read_csv(self.data_file)
            data = pd.concat([existing_data, data], ignore_index=True)
        except FileNotFoundError:
            pass
        data.to_csv(self.data_file, index=False)
    
    @classmethod
    def view_all_accounts(cls):
        """Read and display all stored account details."""
        try:
            data = pd.read_csv(cls.data_file)
            print(data)
        except FileNotFoundError:
            print("No account data found.")


class HumanoidAccount(BankSystem):
    """Handles manually created bank accounts."""
    def __init__(self, name, age, salary, password):
        super().__init__(name, age, salary)
        self.password = password
        self.save_to_file()
    
    def display_details(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Account: {self.account_number}"


class AIAccount(BankSystem):
    """Handles AI-generated bank accounts with random passwords."""
    
    def __init__(self):
        name = f"AI_User_{np.random.randint(1000, 9999)}"
        age = np.random.randint(18, 60)
        salary = np.random.randint(20000, 150000)
        password = self.generate_password()
        super().__init__(name, age, salary)
        self.password = password
        self.save_to_file()
    
    def generate_password(self):
        """Generate a secure random password."""
        return ''.join(np.random.choice(list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"), 12))
    
    def display_details(self):
        return f"AI Account Created: {self.name}, Age: {self.age}, Salary: {self.salary}, Account: {self.account_number}"


# Example Usage
if __name__ == "__main__":
    while True:
        print("\n1. Create Humanoid Account\n2. Create AI Account\n3. View All Accounts\n4. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            salary = int(input("Enter Salary: "))
            password = input("Set Password: ")
            user = HumanoidAccount(name, age, salary, password)
            print("Account Created Successfully!", user.display_details())
        
        elif choice == "2":
            ai_user = AIAccount()
            print("AI Account Generated!", ai_user.display_details())
        
        elif choice == "3":
            BankSystem.view_all_accounts()
        
        elif choice == "4":
            break
        else:
            print("Invalid Choice! Try Again.") 

    #Hope You love that projects ---> 

