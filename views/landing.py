import streamlit as st
from utils.data_loaders import Api

def landing():
    st.title("Finanzas Personales")
    st.write("Bienvenido a la aplicación de Finanzas Personales.")
    st.write("Aquí podrás gestionar tus finanzas de manera eficiente.")
    st.write(
        "Comienza ahora mismo y descubre todo lo que puedes hacer con esta aplicación."
    )

    api = Api()

    login, register, guest = st.columns([2, 2, 1], border=True)

    login.subheader("Login")
    with login.form("Login"):
        st.markdown("#### Enter your credentials")
        email = st.text_input("Email", value="nakada2130@gmail.com")
        password = st.text_input("Password", type="password", value="3430143")
        submit = st.form_submit_button("Login")

        if submit:
            response = api.login(email, password)
            if response.status_code == 200:
                st.success("Login successful")
                login_data = response.json()
                
                st.session_state["user"] = login_data['user']
                st.session_state["token"] = login_data["token"]

                st.switch_page("views/dashboard/user_dashboard.py")
            else:
                st.error("Login failed")

    register.subheader("Register")
    with register.form("Register"):
        st.markdown("#### Enter your credentials")
        name = st.text_input("Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        repeat_password = st.text_input("Repeat Password", type="password")

        submit = st.form_submit_button("Register")
        if submit:
            st.success("Register successful")

    guest.subheader("Guest")
    guest.button("Continue as guest")

landing()
    