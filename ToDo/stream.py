import streamlit as st

if 'tasks' not in st.session_state:
    st.session_state.tasks = []

def show_tasks(filter_by=None):
    if not st.session_state.tasks:
        st.info("No tasks available.")
        return

    for i, task in enumerate(st.session_state.tasks, start=1):
        if filter_by == "completed" and not task['done']:
            continue
        if filter_by == "pending" and task['done']:
            continue

        col1, col2, col3 = st.columns([6, 2, 2])
        col1.markdown(f"**{i}. {task['name']}**")
        col2.markdown("✅" if task["done"] else "❌")
        if not task["done"]:
            if col3.button("Mark Done", key=f"mark_{i}"):
                task["done"] = True
                st.rerun()
        else:
            if col3.button("Remove", key=f"remove_{i}"):
                st.session_state.tasks.pop(i - 1)
                st.rerun()

st.title("📝 ToDo List App")

st.subheader("Add New Task")
new_task = st.text_input("Enter task name", key="new_task_input")
if st.button("Add Task"):
    if not new_task.strip():
        st.warning("Task name cannot be empty.")
    elif any(t["name"] == new_task for t in st.session_state.tasks):
        st.warning("Task already exists.")
    else:
        st.session_state.tasks.append({"name": new_task, "done": False})
        st.success("Task added.")
        st.rerun()

st.subheader("Tasks")
filter_option = st.radio("Show", ["All", "Pending", "Completed"], horizontal=True)

if filter_option == "All":
    show_tasks()
elif filter_option == "Pending":
    show_tasks("pending")
else:
    show_tasks("completed")
