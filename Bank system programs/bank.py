#  hello world this mezbah kkhan from backend developer
#  This version removes heavy third-party dependencies (pandas, numpy)
#  in favour of Python standard-library modules for faster start-up and
#  a dramatically smaller deployment footprint.

import csv
import os
import random
import string

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
        return random.randint(1_000_000_000, 9_999_999_999)
    
    def save_to_file(self):
        """Append user details to a CSV file (header written once)."""
        file_exists = os.path.isfile(self.data_file)
        with open(self.data_file, "a", newline="") as f:
            writer = csv.writer(f)
            # Write header exactly once (when creating the file)
            if not file_exists:
                writer.writerow(["Name", "Age", "Salary", "Account Number"])
            writer.writerow([self.name, self.age, self.salary, self.account_number])
    
    @classmethod
    def view_all_accounts(cls):
        """Read and display all stored account details."""
        if not os.path.isfile(cls.data_file):
            print("No account data found.")
            return

        with open(cls.data_file, newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                print(" | ".join(row))


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
        name = f"AI_User_{random.randint(1000, 9999)}"
        age = random.randint(18, 60)
        salary = random.randint(20_000, 150_000)
        password = self.generate_password()
        super().__init__(name, age, salary)
        self.password = password
        self.save_to_file()
    
    def generate_password(self):
        """Generate a secure random password."""
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.choices(chars, k=12))
    
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

