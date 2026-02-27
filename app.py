import streamlit as st
from hello import Bank

st.set_page_config(page_title="Simple Bank App", layout="centered")
st.title("Welcome to Streamlit Bank")

menu = st.sidebar.selectbox(
    "Choose Action",
    ["Create Account", "Deposit", "Withdraw", "Show Details", "Update Info", "Delete Account"]
)

if menu == "Create Account":
    name = st.text_input("Your Name")
    age = st.number_input("Your Age", min_value=0, step=1)
    email = st.text_input("Your Email")
    pin = st.text_input("4-digit PIN", type="password")

    if st.button("Create"):
        if not (name and email and pin):
            st.warning("Fill all fields")
        elif not pin.isdigit() or len(pin) != 4:
            st.error("PIN must be exactly 4 digits")
        else:
            user, msg = Bank.create_account(name, int(age), email, pin)
            st.success(msg)
            if user:
                st.info(f"Account Number: {user['accountNo.']}")

elif menu == "Deposit":
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        if not pin.isdigit():
            st.error("Invalid PIN")
        else:
            success, msg = Bank.deposit(acc_no, pin, int(amount))
            st.success(msg) if success else st.error(msg)

elif menu == "Withdraw":
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        if not pin.isdigit():
            st.error("Invalid PIN")
        else:
            success, msg = Bank.withdraw(acc_no, pin, int(amount))
            st.success(msg) if success else st.error(msg)

elif menu == "Show Details":
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):
        if not pin.isdigit():
            st.error("Invalid PIN")
        else:
            user = Bank.find_user(acc_no, pin)
            if user:
                st.json(user)
            else:
                st.error("No account found")

elif menu == "Update Info":
    acc_no = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")
    name = st.text_input("New Name (Optional)")
    email = st.text_input("New Email (Optional)")
    new_pin = st.text_input("New PIN (Optional)")

    if st.button("Update"):
        if not pin.isdigit():
            st.error("Invalid current PIN")
        else:
            success, msg = Bank.update_user(acc_no, pin, name, email, new_pin)
            st.success(msg) if success else st.error(msg)

elif menu == "Delete Account":
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        if not pin.isdigit():
            st.error("Invalid PIN")
        else:
            success, msg = Bank.delete_user(acc_no, pin)
            st.success(msg) if success else st.error(msg)