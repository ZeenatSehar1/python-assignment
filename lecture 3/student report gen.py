import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Report", layout="centered")

st.title("🎓 Student Report Generator")
st.write("Enter student details and generate a report")

students = {}

n = st.number_input("Number of students", min_value=1, step=1)

for i in range(n):
    st.subheader(f"Student {i+1}")

    name = st.text_input("Name", key=f"name{i}")
    age = st.text_input("Age", key=f"age{i}")

    subjects = set()
    marks = []

    s = st.number_input("Number of subjects", min_value=1, step=1, key=f"subcount{i}")

    for j in range(s):
        sub = st.text_input(f"Subject {j+1}", key=f"sub{i}{j}")
        mark = st.number_input(f"Marks for Subject {j+1}", min_value=0, max_value=100, key=f"mark{i}{j}")

        if sub:
            subjects.add(sub)
            marks.append(mark)

    if name and age:
        students[(name, age)] = {"subjects": subjects, "marks": marks}

if st.button("Generate Report"):
    st.subheader("📄 Student Report")

    report_data = []

    for info, data in students.items():
        avg = sum(data["marks"]) / len(data["marks"])
        report_data.append([info[0], info[1], ", ".join(data["subjects"]), data["marks"], avg])

    df = pd.DataFrame(report_data, columns=["Name", "Age", "Subjects", "Marks", "Average"])
    st.dataframe(df, use_container_width=True)

    st.success("✅ Report Generated Successfully")
