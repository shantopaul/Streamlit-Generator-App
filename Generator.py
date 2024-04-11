# IMPORT LIBRARIES
import streamlit as st
import string
import random

st.set_page_config(
    page_title="Password Generator",
    layout="centered",
)


def random_password():
    import random
    capital_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_letter = "abcdefghijklmnopqrstuvwxyz"
    special_letter = "$@#%&"
    number_letter = "0123456789"

    password = ""

    for x in range(1,3):
            capital_char = random.choice(capital_letter) #   capital_letter
            password = password + capital_char

    for x in range(1,3):
            small_char = random.choice(small_letter) #    small_letter
            password = password + small_char

    for x in range(1,3):
            special = random.choice(special_letter) #   special_letter
            password = password + special

    for x in range(1,3):
            number = random.choice(number_letter) #    number_letter
            password = password + number

        #............................................................................

    for x in range(1,3):
            small_char = random.choice(small_letter) #    small_letter
            password = password + small_char

    for x in range(1,3):
            capital_char = random.choice(capital_letter) #   capital_letter
            password = password + capital_char

    for x in range(1,3):
            special = random.choice(special_letter) #   special_letter
            password = password + special

    for x in range(1,3):
            number = random.choice(number_letter) #    number_letter
            password = password + number

    return password


st.header("Password Generator")

if st.button('Generate Password'):
    output_password = random_password()
    st.code(output_password)
    


