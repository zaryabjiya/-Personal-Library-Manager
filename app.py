import streamlit as st
import json

LIBRARY_FILE = "library_data.json"

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
            background: linear-gradient(to right, #1E3C72, #2A5298);
            color: white;
        }
        .stSidebar {
            background:#0A1F44;
            color: white;
        }
        .stButton>button {
            background-color: #FF6F61;
            color: white;
            border-radius: 8px;
        }
        .stTextInput>div>div>input {
            background-color: #E3F2FD;
            color: black;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
st.title("📖 My Unique Library Manager")

# Sidebar - Add Book
st.sidebar.header("➕ Add a New Book")
title = st.sidebar.text_input("Book Title")
author = st.sidebar.text_input("Author")
year = st.sidebar.number_input("Publication Year", min_value=0, step=1)
genre = st.sidebar.text_input("Genre")
read_status = st.sidebar.radio("Read Status", ["Unread", "Read"])

if st.sidebar.button("Add Book"):
    new_book = {"title": title, "author": author, "year": year, "genre": genre, "read": read_status == "Read"}
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
        st.write(f'- **{book["title"]}** by {book["author"]} ({book["year"]}) - {book["genre"]} - {status}')
else:
    st.write("No books in this category!")

# Statistics
st.header("📊 Library Stats")
total_books = len(st.session_state.library)
read_books = sum(1 for book in st.session_state.library if book["read"])
percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
st.write(f'**Total Books:** {total_books}')
st.write(f'**Books Read:** {read_books} ({percentage_read:.2f}%)')
