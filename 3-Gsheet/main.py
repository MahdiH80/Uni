import gspread
from google.oauth2.service_account import Credentials
import streamlit as st
import pandas as pd
# نصب نیست نصب میکردم ولی بازم همون ارور میداد c++ از این روش رفتم چون گیر میداد به 
# URL: https://docs.google.com/spreadsheets/d/1pApraLUoLFC9vAwnhWo5sCenXyZjjqH-joQ_rEs6ktQ/edit#gid=0

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials_info = {
    # "type": "service_account",
    # "project_id": "strategic-well-364515",
    # "private_key_id": "e9783091c92aeaa2e2f729176a0225974f519129",
    # "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCtxAFPo6lVuzuN\nyQ+cdoGNmBBInirNBlZjlaWYnY27KgBvXk59GK6mcxCB5dzbiayVHIg0wPxhrvL5\nod8xEgKubMtfouTEgoQbYBV71UpYheq2ICppm7YQM5QX15S/QS6x167wZsjdTwOm\ngArKv+c6VKeGV4m1JYUH2ZSJC0Cr90vOKGPanOBkJhtvu3GIAn/8UNCmpVSJKVQm\n6Eh/C6Mq+sA3j5IOD0ELHY/GvLQfPtz4OgdXdBwp7t31N1rUDl/rGski/jKjaRmN\n7XCIFb7fJ4nIJTGx+Et/yK87+1zgozQJpQ1gDXcgjRGk4qFg2FulIqpBWBldltfh\noJsPfnATAgMBAAECggEAEO4BrLHcMTNKmZqnGo48kBWVMeYLHdT0vMNwkgkjrRe/\nWW+9mO2Qh+dlCoA2lO3PHUCy5To6PLAwEcdGI2tG90SNSgDpELD1+w7Q+QguXqfp\ngXC/1nCVJp3yhfd7PBO3NMeNTp8iXywwGwbq8Oxiib8utTrjz/za/wlMB1AhLxUs\nucR6nFgio4oE7Mj4qmFwH+I/B4XRo3sDhWp66XTK+ynLJWRH8rR7Ai61VaMeHWDT\nt/+U8dyHgwjj5g8/Mqffl56Dz6T9tERb547CcPyrrk55pZRrrCMHOT7T0T6/iWTt\nP6dR+XB0cunGN4qYe35Fab2qUoR1ydLCEk8gSTPFJQKBgQDT8DNrOdyFF09MxpIa\nbA90+c+BfJWIMmTqV+Ay9APaf3qEEfz0/3ZVZgH/y48qDysfT2IzIdTZoGD5KRU8\ntNmHWk3S4xeCo+/elN8xKQDXN/F7sISVEZsokMyPRPb1DtOFNcXGy7vjmMRgaxQy\nO4v/Cfws8KHUSY2AKyPRo7O3nwKBgQDR5C0t/6sPsPb/JBcuHr68IlSpndRVfB1H\neodtGhZMzfn8GPrSSaFfHNtF0ncnNr/DKMY0Jb1az57efBoaJKtpLKahEo6psWj8\nYLdMpUlcGOiOqwhy9fzRnTaaxEHGyY23t+XdqL399l1aBIl+UTrfIoA8KC4aHTBu\nRpmoFYDDDQKBgQDShz+8muyYdJA8duA5SPCNxX1AZk5vzYd7VjGKy+RsDsfYG7pI\ncN/Ocxc3TrD3Gbw/TO8CVfAHAo5x00KaXBfdoXG/NABtsIWdeArB3bZNE/BYav84\nyRV01WmuQ9aBlem94K2HDWil7GHeWV/liktF3FhZF+vZYfsivzfEjrX+hwKBgFTa\nmYVSKlcCpSiK77Aej9/BRVb5TsFslu2x1JRACqnsT9ciRizDxbCNGvzEVJWO5cHB\ndzfX1hCjhUfPBkJxdrbjbU4LEY/7AEWf2Brta5YHH+WlsZnAZwBbPZseIrV6AIg4\nmX6eXIkSk7Tzxp5BurpA2XT4jYLTMCQ0+KPiZZb1AoGBAJa9uf6pS9REyBz2gY2v\ntH6WiJet0zejaU8reXFrCOWxfu8eggGG587wO7Kgpq/5OCtfRX1hziSGJFTBMEuH\niCD3MWoDN3xdW7roIF+rf/zEoCRAi1RA3Zo2PVI/wQ/hWGq7c6gexlmQ0441F4pR\nuKk3utljQekm8qnoV6u0c0IE\n-----END PRIVATE KEY-----\n",
    # "client_email": "python@strategic-well-364515.iam.gserviceaccount.com",
    # "client_id": "109426211235586577610",
    # "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    # "token_uri": "https://oauth2.googleapis.com/token",
    # "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    # "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/python%40strategic-well-364515.iam.gserviceaccount.com",
    # "universe_domain": "googleapis.com"
}

creds = Credentials.from_service_account_info(credentials_info, scopes=scope)
client = gspread.authorize(creds)
sheet = client.open_by_key("1pApraLUoLFC9vAwnhWo5sCenXyZjjqH-joQ_rEs6ktQ").sheet1


def load_data():
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    return df

def insert_contact(name, family, number):
    sheet.append_row([name, family, number])

def delete_contact(index):
    sheet.delete_rows(index + 2)  # +2 to account for header row and 1-indexing

def update_contact(index, name, family, number):
    sheet.update_cell(index + 2, 1, name)
    sheet.update_cell(index + 2, 2, family)
    sheet.update_cell(index + 2, 3, number)

data_df = load_data()
st.write("## Contact List")
st.write(data_df)

new_name = st.text_input("Enter Name:", key="name")
new_family = st.text_input("Enter Family:", key="family")
new_number = st.number_input("Enter Number:", key="number")

if st.button("Insert"):
    insert_contact(new_name, new_family, new_number)
    st.success("Contact added!")
    st.experimental_rerun()

st.write("## Edit or Delete Contacts")
selected_index = st.number_input("Select contact index to edit/delete:", min_value=0, max_value=len(data_df)-1, step=1)
selected_contact = data_df.iloc[selected_index] if not data_df.empty else None

if selected_contact is not None:
    st.write(selected_contact)
    updated_name = st.text_input("Update Name:", selected_contact['Name'], key="update_name")
    updated_family = st.text_input("Update Family:", selected_contact['Family'], key="update_family")
    updated_number = st.number_input("Update Number:", selected_contact['Number'], key="update_number")

    if st.button("Update"):
        update_contact(selected_index, updated_name, updated_family, updated_number)
        st.success("Contact updated!")
        st.experimental_rerun()

    if st.button("Delete"):
        delete_contact(selected_index)
        st.success("Contact deleted!")
        st.experimental_rerun()
