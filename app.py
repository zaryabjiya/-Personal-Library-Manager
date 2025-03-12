import streamlit as st
import sqlite3
import pandas as pd
import os

# Database Setup
DB_FILE = "library.db"
if not os.path.exists(DB_FILE):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, genre TEXT, status TEXT, cover TEXT)''')
    conn.commit()
    conn.close()

# Database Functions
def get_books():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    conn.close()
    return books

def add_book(title, author, genre, status, cover_path):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO books (title, author, genre, status, cover) VALUES (?, ?, ?, ?, ?)", (title, author, genre, status, cover_path))
    conn.commit()
    conn.close()

def delete_book(book_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    conn.close()

def update_book_status(book_id, new_status):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("UPDATE books SET status=? WHERE id=?", (new_status, book_id))
    conn.commit()
    conn.close()

# Streamlit App UI
st.set_page_config(page_title="📚 Personal Library Manager", layout="wide")
st.title("📚 Personal Library Manager")

# Sidebar for Adding Books
with st.sidebar:
    st.header("➕ Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    genre = st.text_input("Genre")
    status = st.selectbox("Reading Status", ["Unread", "Reading", "Completed"])
    cover = st.file_uploader("Upload Book Cover (Optional)", type=["jpg", "png"])

    if st.button("Add Book"):
        cover_path = f"covers/{title}.jpg" if cover else "default_cover.jpg"
        if cover:
            os.makedirs("covers", exist_ok=True)
            with open(cover_path, "wb") as f:
                f.write(cover.getbuffer())
        add_book(title, author, genre, status, cover_path)
        st.success(f"📖 Book '{title}' added successfully!")
        st.experimental_rerun()

# Display Books
st.subheader("📖 Your Book Collection")
search = st.text_input("🔍 Search by Title or Author")

books = get_books()
filtered_books = [book for book in books if search.lower() in book[1].lower() or search.lower() in book[2].lower()]

if filtered_books:
    for book in filtered_books:
        col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])
        with col1:
            if book[5] != "default_cover.jpg":
                st.image(book[5], width=100)
            else:
                st.image("default_cover.jpg", width=100)

        col2.text(book[1])
        col3.text(book[2])
        col4.text(book[3])
        new_status = col4.selectbox("", ["Unread", "Reading", "Completed"], index=["Unread", "Reading", "Completed"].index(book[4]), key=f"status_{book[0]}")
        
        if new_status != book[4]:
            update_book_status(book[0], new_status)
            st.experimental_rerun()

        if col5.button("❌ Delete", key=f"delete_{book[0]}"):
            delete_book(book[0])
            st.experimental_rerun()
else:
    st.warning("No books found. Try adding some!")

# Export Books as CSV
if books:
    st.subheader("📂 Export Library Data")
    df = pd.DataFrame(books, columns=["ID", "Title", "Author", "Genre", "Status", "Cover"])
    df.drop(columns=["ID", "Cover"], inplace=True)
    st.download_button("Download CSV", df.to_csv(index=False), "library_data.csv", "text/csv")

