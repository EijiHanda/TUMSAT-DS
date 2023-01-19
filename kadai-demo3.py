import streamlit as st
import random

st.set_page_config(page_title="Math Quiz", page_icon=":chart_with_upwards_trend:", layout="wide")

operations = ['+', '-', '*', '/']

def generate_quiz():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.choice(operations)
    if operation == '+':
        result = num1 + num2
        question = f'{num1} + {num2} = ?'
    elif operation == '-':
        result = num1 - num2
        question = f'{num1} - {num2} = ?'
    elif operation == '*':
        result = num1 * num2
        question = f'{num1} * {num2} = ?'
    else:
        while num1 % num2 != 0:
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
        result = num1 / num2
        question = f'{num1} / {num2} = ?'
    options = [result + random.randint(-3,3) for _ in range(3)]
    options.append(result)
    random.shuffle(options)
    return question, options, result

def main():
    st.title("Math Quiz")
    question, options, correct_answer = generate_quiz()
    st.write(question)
    user_answer = st.selectbox("Choose an option", options)
    if user_answer == correct_answer:
        st.success("Correct!")
    else:
        st.error("Incorrect. The correct answer is: {}".format(correct_answer))

if __name__=="__main__":
    main()
