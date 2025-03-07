import streamlit as st

from utils.data_loaders import Api

def user_dashboard():

    api = Api()

    user_data = st.session_state["user"]
    token = st.session_state["token"]

    st.title("Finanzas Personales")
    with st.sidebar:
        #st.header(f"Hola 👋 {consumer_data['name']}")
        st.header(f"Hola 👋 {user_data['first_name']}")
        st.divider()

        st.button("Añadir",icon="➕",use_container_width=True)
        st.button("Personalizar",icon="✏️",use_container_width=True)
        st.divider()

        st.button("Preferencias", icon="⚙️",use_container_width=True)

    with st.spinner("Loading data"):
        response = api.get_transactions(token)

    if response.status_code == 200:
        transactions = response.json()
        
        # Process transactions to format tags as comma-separated strings
        formatted_transactions = []

        for t in transactions:
            # Join tag names with commas
            tags = ', '.join([tag['name'] for tag in t['tags']])
            
            # Create formatted transaction record
            formatted_transaction = {
                'Fecha': t['transaction_date'].split('T')[0],  # Show only the date part
                'Tipo': t['transaction_type'].capitalize(),
                'Descripción': t['description'],
                'Monto': f"{t['currency']} {t['amount']}",
                'Tags': tags
            }
            formatted_transactions.append(formatted_transaction)
        
        # Display transactions in a Streamlit dataframe
        st.dataframe(
            formatted_transactions,
            column_config={
                'Fecha': st.column_config.DateColumn('Fecha'),
                'Tipo': st.column_config.TextColumn('Tipo'),
                'Descripción': st.column_config.TextColumn('Descripción'),
                'Monto': st.column_config.TextColumn('Monto'),
                'Tags': st.column_config.TextColumn('Tags')
            },
            hide_index=True,
            use_container_width=True
        )

user_dashboard()