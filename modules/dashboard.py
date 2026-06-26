import streamlit as st

from database.db import (
    create_tables,
    get_connection
)


def show():

    create_tables()

    st.title("📊 Student Dashboard")

    task = st.text_input("New Task")

    if st.button("Add Task"):

        if task:

            conn = get_connection()

            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO tasks(task,completed) VALUES(?,?)",
                (task,0)
            )

            conn.commit()

            conn.close()

            st.success("Task Added")

            st.rerun()

    st.divider()

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()

    conn.close()

    completed = 0

    for t in tasks:

        checked = st.checkbox(
            t[1],
            value=bool(t[2]),
            key=t[0]
        )

        if checked != bool(t[2]):

            conn = get_connection()

            cursor = conn.cursor()

            cursor.execute(
                "UPDATE tasks SET completed=? WHERE id=?",
                (1 if checked else 0, t[0])
            )

            conn.commit()

            conn.close()

            st.rerun()

        if checked:
            completed += 1

    st.divider()

    total = len(tasks)

    progress = completed / total if total else 0

    st.subheader("Progress")

    st.progress(progress)

    st.metric(
        "Completed",
        f"{completed}/{total}"
    )