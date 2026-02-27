import json
import random
import string
from pathlib import Path


class Bank:
    database = "data.json"

    @classmethod
    def load_data(cls):
        if Path(cls.database).exists():
            with open(cls.database, "r") as f:
                return json.load(f)
        return []

    @classmethod
    def save_data(cls, data):
        with open(cls.database, "w") as f:
            json.dump(data, f, indent=4)

    @classmethod
    def generate_account_number(cls):
        chars = random.choices(string.ascii_uppercase, k=3) + \
                random.choices(string.digits, k=4)
        random.shuffle(chars)
        return "".join(chars)

    @classmethod
    def create_account(cls, name, age, email, pin):
        data = cls.load_data()

        if age < 18 or not str(pin).isdigit() or len(str(pin)) != 4:
            return None, "Age must be 18+ and PIN must be 4 digits"

        acc_no = cls.generate_account_number()

        user = {
            "name": name,
            "age": age,
            "email": email,
            "pin": str(pin),
            "accountNo.": acc_no,
            "balance": 0
        }

        data.append(user)
        cls.save_data(data)

        return user, "Account created successfully"

    @classmethod
    def find_user(cls, acc_no, pin):
        data = cls.load_data()
        for user in data:
            if user["accountNo."] == acc_no and user["pin"] == str(pin):
                return user
        return None

    @classmethod
    def deposit(cls, acc_no, pin, amount):
        data = cls.load_data()
        for user in data:
            if user["accountNo."] == acc_no and user["pin"] == str(pin):
                if 0 < amount <= 10000:
                    user["balance"] += amount
                    cls.save_data(data)
                    return True, "Deposit successful"
                return False, "Amount must be between 1 and 10000"
        return False, "Invalid account or PIN"

    @classmethod
    def withdraw(cls, acc_no, pin, amount):
        data = cls.load_data()
        for user in data:
            if user["accountNo."] == acc_no and user["pin"] == str(pin):
                if amount <= user["balance"]:
                    user["balance"] -= amount
                    cls.save_data(data)
                    return True, "Withdrawal successful"
                return False, "Insufficient balance"
        return False, "Invalid account or PIN"

    @classmethod
    def update_user(cls, acc_no, pin, name=None, email=None, new_pin=None):
        data = cls.load_data()
        for user in data:
            if user["accountNo."] == acc_no and user["pin"] == str(pin):
                if name:
                    user["name"] = name
                if email:
                    user["email"] = email
                if new_pin and str(new_pin).isdigit() and len(str(new_pin)) == 4:
                    user["pin"] = str(new_pin)

                cls.save_data(data)
                return True, "User details updated"
        return False, "User not found"

    @classmethod
    def delete_user(cls, acc_no, pin):
        data = cls.load_data()
        for i, user in enumerate(data):
            if user["accountNo."] == acc_no and user["pin"] == str(pin):
                data.pop(i)
                cls.save_data(data)
                return True, "Account deleted"
        return False, "Account not found"