# Cloud-Based Attendance Monitoring System

A modern and interactive Attendance Monitoring System developed using Python and Streamlit for real-time attendance management and visualization. The application provides secure login authentication, attendance tracking, record management, and graphical insights through a clean and responsive interface. 

---

# Overview

The Cloud-Based Attendance Monitoring System is designed to simplify attendance management through a web-based platform. The system enables users to mark attendance, view attendance records, and analyze attendance statistics using interactive visualizations.

The project demonstrates the integration of Python-based web application development with data handling and visualization techniques.

---

# Features

* Secure Login Authentication
* Attendance Marking System
* Attendance Records Dashboard
* Data Visualization and Analytics
* Interactive Streamlit Interface
* CSV-based Data Storage
* Custom Styled User Interface
* Real-Time Attendance Updates

---

# Technologies Used

| Technology | Purpose                        |
| ---------- | ------------------------------ |
| Python     | Core Programming               |
| Streamlit  | Web Application Framework      |
| Pandas     | Data Processing and Management |
| CSV        | Local Database Storage         |
| HTML/CSS   | User Interface Styling         |
| Datetime   | Timestamp Generation           |

---

# Project Structure

```bash
Attendance-Monitoring-System/
│
├── app.py
├── attendance.csv
├── requirements.txt
└── README.md
```

---

# System Workflow

1. User logs into the system using predefined credentials
2. User selects attendance status (Present, Absent, or Late)
3. Attendance details are stored with a timestamp
4. Records are saved in `attendance.csv`
5. Dashboard displays attendance history
6. Visualization module generates attendance statistics charts

---

# Login Credentials

```text
Username: admin
Password: password123
```

---

# Functional Modules

## Login Module

Provides secure access to the application using authentication credentials.

## Attendance Module

Allows users to:

* Enter their name
* Select attendance status
* Submit attendance records

## Attendance Records Module

Displays all attendance entries dynamically in tabular format.

## Data Visualization Module

Generates graphical attendance statistics using Streamlit charts.

---

# Installation and Setup

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/attendance-monitoring-system.git
```

## 2. Navigate to Project Directory

```bash
cd attendance-monitoring-system
```

## 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the Application

```bash
streamlit run app.py
```

---

# Required Libraries

```txt
streamlit
pandas
```

Install manually if required:

```bash
pip install streamlit pandas
```

---

# Future Enhancements

* Cloud Database Integration
* Face Recognition Attendance
* QR Code-Based Attendance
* Admin Panel and User Roles
* Attendance Export to Excel/PDF
* Email Notifications
* Real-Time Analytics Dashboard

---

# Learning Outcomes

* Developed hands-on experience with Streamlit application development
* Learned attendance data management using Pandas
* Implemented authentication and session handling
* Improved frontend styling using custom CSS
* Built interactive dashboards and visualizations

---

# Author

**Chinmay Raj**

Email: [chinmayraj976@gmail.com](mailto:chinmayraj976@gmail.com)

[LinkedIn](https://www.linkedin.com/in/chinmay-raj-50944a267/?utm_source=chatgpt.com)

[GitHub](https://github.com/Chinmayy-raj?utm_source=chatgpt.com)
