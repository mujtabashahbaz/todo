import streamlit as st

# Page configuration
st.set_page_config(page_title="To-Do List", page_icon="📝", layout="centered")

# App styling
st.markdown(
    """
    <style>
    body {
        background-color: #87ceeb; /* Sky blue */
    }
    .stApp {
        background-color: #87ceeb; /* Sky blue */
    }
    .title {
        color: #ff69b4; /* Hot pink */
        text-align: center;
        font-size: 4rem; /* 400% increase */
    }
    .add-task-button {
        background-color: #ff69b4 !important; /* Hot pink */
        color: white !important;
        font-size: 1.5rem !important; /* 400% increase */
        border-radius: 10px !important;
    }
    .delete-button, .complete-button {
        font-size: 1rem !important;
        border-radius: 5px !important;
        padding: 10px;
    }
    .delete-button {
        background-color: #ff1493 !important; /* Deep pink */
        color: white !important;
    }
    .delete-button:hover {
        background-color: #c71585 !important; /* Medium violet red */
    }
    .complete-button {
        background-color: #ff69b4 !important; /* Hot pink */
        color: white !important;
    }
    .complete-button:hover {
        background-color: #ff1493 !important; /* Deep pink */
    }
    .task-item {
        background-color: #e0f7fa !important; /* Light blue */
        border-radius: 10px !important;
        padding: 15px !important;
        margin-bottom: 10px !important;
        font-size: 1.5rem !important;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .task-item.completed {
        text-decoration: line-through !important;
        background-color: #b3e5fc !important; /* Lighter blue */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App header
st.markdown('<h1 class="title">To-Do List</h1>', unsafe_allow_html=True)

# Session state to store tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add new task
new_task = st.text_input("Add a new task:")
if st.button("Add Task", key="add", help="Add a new task"):
    if new_task.strip():
        st.session_state.tasks.append({"text": new_task, "completed": False})

# Display tasks
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        task_class = "completed" if task["completed"] else ""
        st.markdown(
            f'<div class="task-item {task_class}">{task["text"]} '
            f'<button class="complete-button" onclick="document.getElementById(\'complete-{i}\').click()">Complete</button> '
            f'<button class="delete-button" onclick="document.getElementById(\'delete-{i}\').click()">Delete</button></div>',
            unsafe_allow_html=True,
        )

        # Hidden buttons for Streamlit
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button(f"Complete-{i}", key=f"complete-{i}"):
                task["completed"] = not task["completed"]
        with col2:
            if st.button(f"Delete-{i}", key=f"delete-{i}"):
                st.session_state.tasks.pop(i)
                break
