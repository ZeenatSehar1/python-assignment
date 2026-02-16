import streamlit as st
import pandas as pd

# 🌟 Page Config
st.set_page_config(page_title="Student Performance Tracker", page_icon="📊", layout="wide")

# Title
st.title("📊 Student Performance Tracker")
st.write("Track students' marks, calculate averages, and view the leaderboard.")

# --- Initial Data ---
students = {
    "Ali": [80, 75, 90],
    "Sara": [85, 70, 88]
}

# --- Sidebar: Add New Students ---
st.sidebar.header("➕ Add New Student")
new_name = st.sidebar.text_input("Student Name")
new_marks = st.sidebar.text_area("Marks in 3 subjects (comma separated)")

if st.sidebar.button("Add Student"):
    try:
        marks_list = list(map(int, new_marks.split(",")))
        if len(marks_list) != 3:
            st.sidebar.error("Please enter exactly 3 marks.")
        elif new_name.strip() == "":
            st.sidebar.error("Enter a valid student name.")
        else:
            students[new_name] = marks_list
            st.sidebar.success(f"Student {new_name} added!")
    except:
        st.sidebar.error("Enter valid numbers separated by commas.")

# --- Add Three Default Students (if not already added) ---
default_students = {
    "Ahmed": [70, 65, 75],
    "Zara": [90, 95, 92],
    "Hassan": [60, 70, 68]
}

for name, marks in default_students.items():
    if name not in students:
        students[name] = marks

# --- Calculate Averages ---
averages = {name: sum(marks)/len(marks) for name, marks in students.items()}

# Add averages into the dictionary as new keys
for name, avg in averages.items():
    students[name + "_avg"] = avg

# --- Convert to DataFrame for display ---
df_marks = pd.DataFrame({k: v for k, v in students.items() if not k.endswith("_avg")}).T
df_marks.columns = ["Subject 1", "Subject 2", "Subject 3"]
df_marks["Average"] = df_marks.mean(axis=1).round(2)

# --- Sort by Average ---
df_sorted = df_marks.sort_values("Average", ascending=False)

# --- Display Marks Table ---
st.subheader("📋 Student Marks and Averages")
st.dataframe(df_sorted.style.background_gradient(subset=["Average"], cmap="YlGnBu"))

# --- Sorted Average List ---
st.subheader("🏆 Students Sorted by Average Marks")
sorted_list = sorted(averages.items(), key=lambda x: x[1], reverse=True)
for i, (name, avg) in enumerate(sorted_list, 1):
    if not name.endswith("_avg"):
        st.markdown(f"**{i}. {name}** — Average: {avg:.2f} 🎯")
