import streamlit as st
import random

st.set_page_config(page_title="History Quiz", page_icon=":books:", layout="wide")

questions = [
    {
        'question': 'Who discovered America?',
        'options': ['Christopher Columbus', 'Ferdinand Magellan', 'Amerigo Vespucci', 'Marco Polo'],
        'answer': 'Christopher Columbus'
    },
    {
        'question': 'What was the main cause of World War I?',
        'options': ['Ideological differences', 'Territorial disputes', 'Economic competition', 'Assassination of Archduke Franz Ferdinand'],
        'answer': 'Assassination of Archduke Franz Ferdinand'
    },
    {
        'question': 'Who was the first president of the United States?',
        'options': ['George Washington', 'John Adams', 'Thomas Jefferson', 'James Madison'],
        'answer': 'George Washington'
    }
]

def main():
    st.title("History Quiz")
    question = random.choice(questions)
    st.write(question['question'])
    options = question['options']
    random.shuffle(options)
    user_answer = st.selectbox("Choose an option", options)
    if user_answer == question['answer']:
        st.success("Correct!")
    else:
        st.error("Incorrect. The correct answer is: {}".format(question['answer']))

if __name__=="__main__":
    main()