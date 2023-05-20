import streamlit as st
import webtodo_func

todos=webtodo_func.get_todos()

# st.set_page_config(layout="wide")

def add_todo():
    todo=st.session_state["newtodo"]+"\n"
    todos.append(todo)
    webtodo_func.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my Todo App")
st.write("<i>This app is to increase productivity</i>",unsafe_allow_html=True)

st.text_input(label="Enter a Todo",placeholder="Add a new Todo",
              on_change=add_todo,key="newtodo")

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:    # if checkbox is ticked....further code happensbv
        todos.pop(index)
        webtodo_func.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

