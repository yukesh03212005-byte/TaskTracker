import streamlit as st


def show_task(task):

    with st.expander(task["title"], expanded=False):

        completed = st.checkbox(
            "Completed",
            value=task["completed"],
            key=f"check_{task['id']}"
        )

        priority = st.selectbox(
            "Priority",
            ["High", "Medium", "Low"],
            index=["High", "Medium", "Low"].index(task["priority"]),
            key=f"priority_{task['id']}"
        )

        due_date = st.text_input(
            "Due Date",
            value=task["due_date"],
            key=f"date_{task['id']}"
        )

        due_time = st.text_input(
            "Due Time",
            value=task["due_time"],
            key=f"time_{task['id']}"
        )

        email = st.text_input(
            "Notify Email",
            value=task["notify_email"],
            key=f"email_{task['id']}"
        )

        save = st.button(
            "💾 Save",
            key=f"save_{task['id']}"
        )

        delete = st.button(
            "🗑 Delete",
            key=f"delete_{task['id']}"
        )

        return completed, priority, due_date, due_time, email, save, delete