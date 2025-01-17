import streamlit as st
import json

# Load apriori results from JSON file
with open("apriori_results.json", "r") as file:
    apriori_data = json.load(file)

# Initialize session state
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'frequently_bought_together' not in st.session_state:
    st.session_state.frequently_bought_together = []

# Helper function to add item to cart
def add_to_cart(item):
    # Add the item to the cart if not already there
    if item not in st.session_state.cart:
        st.session_state.cart.append(item)
    
    # Add frequently bought items to the frequently bought together list
    for fb_item in apriori_data.get(item, []):
        if fb_item not in st.session_state.cart and fb_item not in st.session_state.frequently_bought_together:
            st.session_state.frequently_bought_together.append(fb_item)

# Helper function to clear the cart
def clear_cart():
    st.session_state.cart = []
    st.session_state.frequently_bought_together = []

# Layout
st.title("Apriori Algorithm - Shopping Cart")

# Display available items
st.subheader("Available Items")
cols = st.columns(4)  # Create 4 columns to display items horizontally

# Create buttons for each item in apriori_data
col_idx = 0
for item in apriori_data.keys():
    with cols[col_idx]:
        st.button(item, on_click=add_to_cart, args=(item,), key=f"button_{item}")
    col_idx = (col_idx + 1) % 4

# Cart section
st.subheader("Your Cart")
if st.session_state.cart:
    cart_cols = st.columns(4)
    col_idx = 0
    for item in st.session_state.cart:
        with cart_cols[col_idx]:
            st.write(item)
        col_idx = (col_idx + 1) % 4
    st.button("Clear Cart", on_click=clear_cart)
else:
    st.write("Your cart is empty.")

# Frequently Bought Together section
st.subheader("Frequently Bought Together")
if st.session_state.frequently_bought_together:
    fb_cols = st.columns(4)
    col_idx = 0
    for fb_item in st.session_state.frequently_bought_together:
        with fb_cols[col_idx]:
            st.button(fb_item, on_click=add_to_cart, args=(fb_item,), key=f"fb_button_{fb_item}")
        col_idx = (col_idx + 1) % 4
else:
    st.write("No frequently bought items yet.")
