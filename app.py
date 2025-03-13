ercentage_read:.2f}%)'import streamlit as st
import json
import os
import pandas as pd
import matplotlib.pyplot as plt

LIBRARY_FILE = "library_data.json"

# Function to Load and Save Books
def load_library():
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Initialize session state
if "library" not in st.session_state:
    st.session_state.library = load_library()

# Custom Styling
st.markdown(
    """
    <style>
        .stApp {
            background: #1E1E1E;
            color: white;
        }
        .stSidebar {
            background: #0A1F44;
            color: white;
        }
        .stButton>button {
            background-color: #FF6F61;
            color: white;
            border-radius: 8px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
st.title("📖 Advanced Library Manager")

# Sidebar - Add Book
st.sidebar.header("➕ Add a New Book")
title = st.sidebar.text_input("Book Title")
author = st.sidebar.text_input("Author")
year = st.sidebar.number_input("Publication Year", min_value=0, step=1)
genre = st.sidebar.text_input("Genre")
read_status = st.sidebar.radio("Read Status", ["Unread", "Read"])
progress = st.sidebar.slider("Reading Progress (%)", 0, 100, 0)
cover = st.sidebar.file_uploader("Upload Book Cover", type=["jpg", "png"])

# Save Book
if st.sidebar.button("Add Book"):
    cover_path = f"covers/{title}.jpg" if cover else "default_cover.jpg"
    if cover:
        os.makedirs("covers", exist_ok=True)
        with open(cover_path, "wb") as f:
            f.write(cover.getbuffer())

    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status == "Read",
        "progress": progress,
        "cover": cover_path
    }
    st.session_state.library.append(new_book)
    save_library(st.session_state.library)
    st.sidebar.success("📚 Book added successfully!")

# Sidebar - Delete Book
st.sidebar.header("🗑️ Remove a Book")
titles = [book["title"] for book in st.session_state.library]
book_to_remove = st.sidebar.selectbox("Select book to remove", ["None"] + titles)
if st.sidebar.button("Remove Book") and book_to_remove != "None":
    st.session_state.library = [book for book in st.session_state.library if book["title"] != book_to_remove]
    save_library(st.session_state.library)
    st.sidebar.success("📕 Book removed successfully!")

# Sidebar - Sorting
st.sidebar.header("📌 Sort Books")
sort_option = st.sidebar.selectbox("Sort By", ["Title", "Author", "Year"])
st.session_state.library.sort(key=lambda x: x[sort_option.lower()])

# Sidebar - Filter Books
st.sidebar.header("📌 Filter Books")
filter_option = st.sidebar.radio("Show", ["All", "Read", "Unread"])
filtered_books = [
    book for book in st.session_state.library 
    if (filter_option == "All") or 
    (filter_option == "Read" and book["read"]) or 
    (filter_option == "Unread" and not book["read"])
]

# Search Books
st.header("🔍 Search for a Book")
search_query = st.text_input("Enter a title or author")
if st.button("Search"):
    search_results = [
        book for book in st.session_state.library 
        if search_query.lower() in book["title"].lower() or search_query.lower() in book["author"].lower()
    ]
    if search_results:
        st.subheader("📚 Matching Books:")
        for book in search_results:
            status = "✅ Read" if book["read"] else "❌ Unread"
            st.write(f'- **{book["title"]}** by {book["author"]} ({book["year"]}) - {book["genre"]} - {status}')
    else:
        st.write("❌ No books found.")

# Display Books
st.header("📚 Your Library")
if filtered_books:
    for book in filtered_books:
        status = "✅ Read" if book["read"] else "❌ Unread"
        col1, col2 = st.columns([1, 4])
        with col1:
            if book["cover"] != "default_cover.jpg":
                st.image(book["cover"], width=100)
            else:
                st.image("default_cover.jpg", width=100)
        with col2:
            st.write(f'**{book["title"]}** by {book["author"]} ({book["year"]}) - {book["genre"]}')
            st.progress(book["progress"])
else:
    st.write("No books in this category!")

# Statistics
st.header("📊 Library Stats")
total_books = len(st.session_state.library)
read_books = sum(1 for book in st.session_state.library if book["read"])
percentage_read = (read_books / total_books * 100) if total_books > 0 else 0

st.write(f'**Total Books:** {total_books}')
st.write(f'**Books Read:** {read_books} ({percentage_read:.2f}%)')

# Graphical Statistics
st.subheader("📊 Reading Progress Analysis")
fig, ax = plt.subplots()
ax.pie([read_books, total_books - read_books], labels=["Read", "Unread"], autopct='%1.1f%%', colors=["#FF6F61", "#2A5298"])
st.pyplot(fig)

# Export Books as CSV
if total_books > 0:
    df = pd.DataFrame(st.session_state.library)
    df.drop(columns=["cover"], inplace=True)
    st.download_button("Download Library Data (CSV)", df.to_csv(index=False), "library_data.csv", "text/csv")

