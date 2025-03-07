import requests
import streamlit as st

class Api:
    def __init__(self):
        self.base_url = st.secrets.api.base_url

    #Auth
    def login(self, email: str, password: str):
        url = f"{self.base_url}/login/"
        data = {"login": email, "password": password}
        response = requests.post(url, json=data)

        return response

    
    #data
    def get_transactions(self, token: str):
        url = f"{self.base_url}/transactions/"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url, headers=headers)
        return response

    

def get_consumer_data():
    return {
        "name": "Masami",
        "last_name": "Nakada",
        "mail": "nakada2130@gmail.com",
        "phone": "+51952841852",
        "url_photo": "URL_ADDRESSars.githubusercontent.com/u/119874330?v=4",
    }
