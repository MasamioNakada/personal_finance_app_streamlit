def user_dashboard():
    st.title("Finanzas Personales")
    with st.sidebar:
        #st.header(f"Hola 👋 {consumer_data['name']}")
        st.header(f"Hola 👋 Masami")
        st.divider()

        st.button("Añadir",icon="➕",use_container_width=True)
        st.button("Personalizar",icon="✏️",use_container_width=True)
        st.divider()

        st.button("Preferencias", icon="⚙️",use_container_width=True)

def login():
    actual_email = "wiki"
    actual_password = "wiki"
    with st.popover("Login"):
    with st.form("Login"):
        st.markdown("#### Enter your credentials")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
    if submit and email == actual_email and password == actual_password:
        # If the form is submitted and the email and password are correct,
        # clear the form/container and display a success message
        placeholder.empty()
        st.success("Login successful")
        main()
    elif submit and email != actual_email and password != actual_password:
        st.error("Login failed")
    else:
        pass