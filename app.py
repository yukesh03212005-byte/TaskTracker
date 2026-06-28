import streamlit as st

from task_manager import (
    add_task,
    delete_task,
    mark_completed,
    mark_pending,
    get_pending_tasks,
    get_completed_tasks
)

from email_service import send_email

st.set_page_config(
    page_title="TaskTrack",
    page_icon="✅",
    layout="centered"
)

st.title("✅ TaskTrack")
st.write("### Personal Task Tracker")

st.divider()

# ==========================
# ADD TASK
# ==========================

col1, col2 = st.columns([5, 1])

with col1:
    new_task = st.text_input(
        "",
        placeholder="Enter a new task...",
        label_visibility="collapsed"
    )

with col2:
    add = st.button(
        "➕",
        use_container_width=True
    )

if add:

    if new_task.strip():

        add_task(new_task.strip())

        st.rerun()

st.divider()

# ==========================
# PENDING TASKS
# ==========================

st.subheader("📋 Pending Tasks")

pending_tasks = get_pending_tasks()

if len(pending_tasks) == 0:

    st.success("No pending tasks.")

for task in pending_tasks:

    col1, col2 = st.columns([8, 1])

    with col1:

        checked = st.checkbox(
            task["title"],
            key=task["id"]
        )

    with col2:

        if st.button(
            "🗑",
            key="delete_" + task["id"]
        ):

            delete_task(task["id"])

            st.rerun()

    if checked:

        mark_completed(task["id"])

        st.rerun()

st.divider()

# ==========================
# COMPLETED TASKS
# ==========================

st.subheader("✅ Completed Tasks")

completed_tasks = get_completed_tasks()

if len(completed_tasks) == 0:

    st.info("No completed tasks.")

for task in completed_tasks:

    col1, col2 = st.columns([8, 1])

    with col1:

        checked = st.checkbox(
            task["title"],
            value=True,
            key="completed_" + task["id"]
        )

    with col2:

        if st.button(
            "🗑",
            key="completed_delete_" + task["id"]
        ):

            delete_task(task["id"])

            st.rerun()

    if not checked:

        mark_pending(task["id"])

        st.rerun()

st.divider()

# ==========================
# EMAIL BUTTON
# ==========================

st.subheader("📧 Reminder")

if st.button("Check Pending Tasks"):

    pending_tasks = get_pending_tasks()

    if len(pending_tasks) == 0:

        st.success("🎉 All tasks are completed.")

    else:

        try:

            send_email(pending_tasks)

            st.success("📧 Reminder email sent successfully!")

        except Exception as e:

            st.error(f"Error: {e}")