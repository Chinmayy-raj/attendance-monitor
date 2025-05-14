import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Custom CSS for styling
st.markdown("""
    <style>
        /* Title Styling */
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #2C3E50;
            text-align: center;
            margin-top: 30px;
        }

        /* Button Styling */
        .button {
            background-color: #3498DB;
            color: white;
            font-size: 18px;
            padding: 15px;
            border-radius: 10px;
            width: 100%;
            text-align: center;
            transition: background-color 0.3s ease;
        }

        .button:hover {
            background-color: #2980B9;
        }

        /* Header Styling */
        .header {
            background-color: #ECF0F1;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }

        /* Card Styling */
        .card {
            background-color: #F7F7F7;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin-bottom: 20px;
            transition: transform 0.3s ease;
        }

        .card:hover {
            transform: scale(1.05);
        }

        /* Table Styling */
        .table-container {
            margin-top: 40px;
        }

        /* Footer Styling */
        .footer {
            text-align: center;
            font-size: 14px;
            color: #7F8C8D;
            padding: 10px;
        }

        /* Form and Stats Styling */
        .form-container {
            background-color: #F7F7F7;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .stats-container {
            display: flex;
            justify-content: space-between;
            gap: 20px;
        }

        .stat-card {
            background-color: #FFF;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
            width: 30%;
        }
    </style>
""", unsafe_allow_html=True)

# Predefined login credentials
USERNAME = "admin"
PASSWORD = "password123"

# Function to mark attendance
def mark_attendance(name, status):
    try:
        df = pd.read_csv("attendance.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Name", "Status", "Time"])

    new_data = {
        "Name": name,
        "Status": status,
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv("attendance.csv", index=False)

# Function to view attendance records
def view_attendance():
    if os.path.exists("attendance.csv"):
        df = pd.read_csv("attendance.csv")
        st.markdown('<div class="header">📊 Attendance Records</div>', unsafe_allow_html=True)
        st.dataframe(df)
    else:
        st.info("No attendance records yet.")

# Function to show data visualizations
def show_data_visualization():
    if os.path.exists("attendance.csv"):
        df = pd.read_csv("attendance.csv")
        st.markdown('<div class="header">📈 Attendance Overview</div>', unsafe_allow_html=True)

        # Generate attendance stats
        attendance_stats = df["Status"].value_counts().reset_index()
        attendance_stats.columns = ["Status", "Count"]
        
        # Bar chart for attendance status
        st.bar_chart(attendance_stats.set_index("Status"))
    else:
        st.info("No data available for visualization.")

# Function to display login page
def login_page():
    st.markdown('<div class="title">📋 Login to Attendance Monitoring System</div>', unsafe_allow_html=True)

    # Username and Password Input
    username = st.text_input("Username", "")
    password = st.text_input("Password", "", type="password")

    login_button = st.button("Login")

    if login_button:
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.session_state.rerun = True  # Set rerun flag to trigger app rerun
            st.success("Login successful! Redirecting to the dashboard...")
        else:
            st.error("Incorrect username or password.")

# Main app function
def app():
    # Check if user is logged in
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        login_page()
        return

    # Trigger rerun if needed
    if 'rerun' in st.session_state and st.session_state.rerun:
        st.session_state.rerun = False
        st.rerun()  # Use st.rerun() to trigger the rerun of the app

    st.markdown('<div class="title">📋 Cloud-Based Attendance Monitoring System</div>', unsafe_allow_html=True)

    # Sidebar for Navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a page", ["Mark Attendance", "View Attendance", "Data Visualization"])

    if page == "Mark Attendance":
        # Section: Mark Attendance
        st.markdown('<div class="header">📝 Mark Your Attendance</div>', unsafe_allow_html=True)

        # Create form layout for user input
        col1, col2 = st.columns([1, 2])

        with col1:
            name = st.text_input("Enter your name", key="name_input")

        with col2:
            status = st.selectbox("Select status", ["Present", "Absent", "Late"], key="status_select")

        submit_button = st.button("Submit Attendance", use_container_width=True, key="submit_button")

        if submit_button:
            if name.strip() == "":
                st.warning("Please enter a valid name.")
            else:
                mark_attendance(name, status)
                st.success(f"Attendance marked for {name} as {status}")

    elif page == "View Attendance":
        # Section: View Attendance
        view_attendance()

    elif page == "Data Visualization":
        # Section: Data Visualization
        show_data_visualization()

    # Footer section
    st.markdown('<div class="footer">Built with 💖 by Your Team</div>', unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    app()
