import streamlit as st
import sqlite3
import bcrypt
import jwt
import datetime
from pages import dashboard, leads, contacts, deals, tasks, reports, settings

# Initialize session state
if 'user' not in st.session_state:
    st.session_state.user = None
if 'token' not in st.session_state:
    st.session_state.token = None

# Database connection
def init_db():
    conn = sqlite3.connect('sanji90.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, username TEXT, password TEXT, role TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS leads
                 (id INTEGER PRIMARY KEY, name TEXT, email TEXT, status TEXT, created_at TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (id INTEGER PRIMARY KEY, name TEXT, email TEXT, phone TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS deals
                 (id INTEGER PRIMARY KEY, title TEXT, amount REAL, stage TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY, title TEXT, assigned_to TEXT, due_date TEXT)''')
    conn.commit()
    conn.close()

# Authentication
def authenticate(username, password):
    conn = sqlite3.connect('sanji90.db')
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    conn.close()
    if result and bcrypt.checkpw(password.encode(), result[0].encode()):
        token = jwt.encode({
            'user': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, "secret_key", algorithm="HS256")
        return token
    return None

# Custom CSS
def load_css():
    with open("styles.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Main app
def main():
    init_db()
    load_css()
    st.title("Sanji90 CRM")
    if not st.session_state.user:
        choice = st.sidebar.selectbox("Login/Signup", ["Login", "Signup"])
        if choice == "Login":
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                token = authenticate(username, password)
                if token:
                    st.session_state.token = token
                    st.session_state.user = username
                    st.success("Logged in successfully!")
                else:
                    st.error("Invalid credentials")
        else:
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Signup"):
                conn = sqlite3.connect('sanji90.db')
                c = conn.cursor()
                hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                try:
                    c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                              (username, hashed.decode(), 'user'))
                    conn.commit()
                    st.success("Account created! Please login.")
                except sqlite3.IntegrityError:
                    st.error("Username already exists")
                conn.close()
    else:
        st.sidebar.write(f"Welcome, {st.session_state.user}")
        page = st.sidebar.selectbox("Navigate", ["Dashboard", "Leads", "Contacts", "Deals", "Tasks", "Reports", "Settings"])
        if page == "Dashboard":
            dashboard.show()
        elif page == "Leads":
            leads.show()
        elif page == "Contacts":
            contacts.show()
        elif page == "Deals":
            deals.show()
        elif page == "Tasks":
            tasks.show()
        elif page == "Reports":
            reports.show()
        elif page == "Settings":
            settings.show()

if __name__ == "__main__":
    main()
