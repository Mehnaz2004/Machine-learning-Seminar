import streamlit as st
import json

# Load the apriori results from the JSON file
with open("apriori_results.json") as file:
    apriori_results = json.load(file)

# Initialize session state for cart and frequently bought together list
if "cart" not in st.session_state:
    st.session_state.cart = []
if "frequently_bought" not in st.session_state:
    st.session_state.frequently_bought = []

# Function to add items to the cart
def add_to_cart(item):
    if item not in st.session_state.cart:
        st.session_state.cart.append(item)
        # Update the frequently bought together list
        for fb_item in apriori_results.get(item, []):
            if fb_item not in st.session_state.frequently_bought:
                st.session_state.frequently_bought.append(fb_item)

# Function to clear the cart and frequently bought together list
def clear_cart():
    st.session_state.cart = []
    st.session_state.frequently_bought = []

st.header("Product Recommendation System \n")
# Layout with even more space for each section
col_left, col_center, col_right = st.columns([3, 7, 4], gap="large")

# Left Column: Cart Section
with col_left:
    st.subheader("Your Cart")
    st.write("###")  # Add space between the header and content
    if st.session_state.cart:
        for item in st.session_state.cart:
            st.write(item)
    else:
        st.write("Your cart is empty.")
    st.write("###")  # Add space before the clear button
    if st.button("Clear Cart"):
        clear_cart()

# Center Column: Available Items
with col_center:
    st.subheader("Available Items")
    st.write("###")  # Add space below the header
    item_cols = st.columns(2, gap="large")  # Only 2 items per row for maximum space
    for idx, item in enumerate(apriori_results.keys()):
        with item_cols[idx % 2]:  # Only 2 items per row
            st.write(item)
            st.button("Add to Cart", key=f"button_{item}", on_click=add_to_cart, args=(item,))

# Right Column: Frequently Bought Together Section
with col_right:
    st.subheader("Frequently Bought Together")
    st.write("###")  # Add space below the header
    if st.session_state.frequently_bought:
        fb_cols = st.columns(1, gap="large")  # 1 item per row for more space
        for fb_item in st.session_state.frequently_bought:
            with fb_cols[0]:
                st.write(fb_item)
                st.button("Add to Cart", key=f"fb_button_{fb_item}", on_click=add_to_cart, args=(fb_item,))
    else:
        st.write("No recommendations yet.")
