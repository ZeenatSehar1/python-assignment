import streamlit as st

# Title
st.title("📊 Student Marks & Averages")

# Student data
students = {
    "Ali": [80, 75, 90],
    "Sara": [85, 70, 88],
    "Ahmed": [70, 65, 75],
    "Zara": [90, 95, 92],
    "Hassan": [60, 70, 68]
}

# Calculate averages
averages = {name: sum(marks)/len(marks) for name, marks in students.items()}

# Sort students by average
sorted_averages = sorted(averages.items(), key=lambda x: x[1], reverse=True)

# Display student marks in a table
st.subheader("📋 Student Marks")
for name, marks in students.items():
    st.write(f"**{name}**: {marks}")

# Display averages
st.subheader("📈 Student Averages")
for name, avg in averages.items():
    st.write(f"**{name}**: {avg:.2f}")

# Display sorted averages
st.subheader("🏆 Students Sorted by Average Marks")
for name, avg in sorted_averages:
    st.write(f"**{name}**: {avg:.2f}")
