
import streamlit as st

# Define explanations and quizzes for supported topics
topics = {
    "photosynthesis": {
        "explanation": "Photosynthesis is the process by which green plants use sunlight to synthesize food from carbon dioxide and water. It typically occurs in the chloroplasts of plant cells.",
        "quiz": [
            {
                "question": "What gas do plants absorb during photosynthesis?",
                "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
                "answer": "Carbon Dioxide"
            },
            {
                "question": "What part of the plant cell carries out photosynthesis?",
                "options": ["Nucleus", "Mitochondria", "Chloroplast", "Ribosome"],
                "answer": "Chloroplast"
            }
        ]
    },
    "gravity": {
        "explanation": "Gravity is a force that attracts two bodies toward each other. On Earth, it gives weight to physical objects and causes them to fall toward the ground when dropped.",
        "quiz": [
            {
                "question": "Who formulated the law of universal gravitation?",
                "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla"],
                "answer": "Isaac Newton"
            },
            {
                "question": "What does gravity do to objects on Earth?",
                "options": ["Pushes them upward", "Makes them float", "Pulls them toward the ground", "Makes them spin"],
                "answer": "Pulls them toward the ground"
            }
        ]
    },
    "mitosis": {
        "explanation": "Mitosis is a type of cell division that results in two daughter cells each having the same number and kind of chromosomes as the parent nucleus.",
        "quiz": [
            {
                "question": "What is the purpose of mitosis?",
                "options": ["To produce energy", "To divide the nucleus", "To create new cells", "To digest food"],
                "answer": "To create new cells"
            },
            {
                "question": "How many daughter cells are produced in mitosis?",
                "options": ["One", "Two", "Three", "Four"],
                "answer": "Two"
            }
        ]
    }
}

# Streamlit app
st.title("📚 Study Buddy Chatbot")
st.write("Hi there! I'm your Study Buddy 🤓. What topic are you working on today?")

# Topic selection
topic_input = st.text_input("Enter a topic (e.g., photosynthesis, gravity, mitosis):").strip().lower()

if topic_input:
    if topic_input in topics:
        st.subheader("📖 Explanation")
        st.write(topics[topic_input]["explanation"])

        st.subheader("📝 Quiz Time!")
        score = 0
        for i, q in enumerate(topics[topic_input]["quiz"], 1):
            st.write(f"**Q{i}: {q['question']}**")
            user_answer = st.radio(f"Choose your answer for Q{i}:", q["options"], key=f"q{i}")
            if user_answer == q["answer"]:
                st.success("Correct! 🎉")
                score += 1
            else:
                st.error(f"Oops! The correct answer is: {q['answer']}")

        st.info(f"Your score: {score} out of {len(topics[topic_input]['quiz'])}")
    else:
        st.warning("Sorry, I don't have information on that topic yet. Try 'photosynthesis', 'gravity', or 'mitosis'.")
