import streamlit as st
import functions as fn


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    fn.write_todos(todos)


todos = fn.get_todos()

st.title("My Todo App")
st.subheader("This is an app")
st.write("This app will increase your productivity")


for index, todo in enumerate(todos):

    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fn.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="dd", label_visibility="hidden",
              placeholder="Add a new todo",
              on_change=add_todo, key="new_todo")
