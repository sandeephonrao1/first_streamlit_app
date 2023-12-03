import streamlit

streamlit.title('My parents new Healthy Diner')

st.header('Breakfast Menu')

# List of Breakfast items
breakfast_items = ['Idli', 'Pohe', 'Vada Sambhar', 'Chai', 'Coffee', 'Dosa']

# Display the list of Breakfast items
for item in breakfast_items:
    st.write(f'- {item}')

