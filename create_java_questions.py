import pandas as pd

# Create a list of Java programming questions
questions = [
    {
        "id": 1,
        "text": "What is the default value of Object variable?",
        "option1": "undefined",
        "option2": "0",
        "option3": "null",
        "option4": "not defined",
        "answer": 3
    },
    {
        "id": 2,
        "text": "Which of the following is not a Java features?",
        "option1": "Dynamic",
        "option2": "Architecture Neutral",
        "option3": "Use of pointers",
        "option4": "Object-oriented",
        "answer": 3
    },
    {
        "id": 3,
        "text": "What is the return type of the hashCode() method in the Object class?",
        "option1": "Object",
        "option2": "int",
        "option3": "long",
        "option4": "void",
        "answer": 2
    },
    {
        "id": 4,
        "text": "Which of the following is a valid declaration of a char?",
        "option1": "char ch = '\\utea';",
        "option2": "char ca = 'tea';",
        "option3": "char cr = \\u0223;",
        "option4": "char cc = '\\u0223';",
        "answer": 4
    },
    {
        "id": 5,
        "text": "What is the size of float and double in Java?",
        "option1": "32 and 64",
        "option2": "32 and 32",
        "option3": "64 and 64",
        "option4": "64 and 32",
        "answer": 1
    },
    {
        "id": 6,
        "text": "Which method of the Class.class is used to determine the name of a class represented by the class object?",
        "option1": "getClass()",
        "option2": "intern()",
        "option3": "getName()",
        "option4": "toString()",
        "answer": 3
    },
    {
        "id": 7,
        "text": "In which memory is String stored, when we create a string using new operator?",
        "option1": "Stack",
        "option2": "String memory",
        "option3": "Heap memory",
        "option4": "Random storage space",
        "answer": 3
    },
    {
        "id": 8,
        "text": "What is the default value of byte variable?",
        "option1": "0",
        "option2": "0.0",
        "option3": "null",
        "option4": "undefined",
        "answer": 1
    },
    {
        "id": 9,
        "text": "Which of the following is a marker interface?",
        "option1": "Runnable interface",
        "option2": "Remote interface",
        "option3": "Readable interface",
        "option4": "Result interface",
        "answer": 2
    },
    {
        "id": 10,
        "text": "Which keyword is used for accessing the features of a package?",
        "option1": "package",
        "option2": "import",
        "option3": "extends",
        "option4": "export",
        "answer": 2
    },
    # Add more questions here...
]

# Add more Java questions to reach 100
for i in range(11, 101):
    questions.append({
        "id": i,
        "text": f"Java Question {i}",  # Placeholder for more questions
        "option1": f"Option 1 for Q{i}",
        "option2": f"Option 2 for Q{i}",
        "option3": f"Option 3 for Q{i}",
        "option4": f"Option 4 for Q{i}",
        "answer": ((i % 4) + 1)  # Cycling through 1-4 for answers
    })

# Convert to DataFrame
df = pd.DataFrame(questions)

# Save to Excel file
df.to_excel('papers/java_questions.xlsx', index=False)
print("Java questions Excel file has been created successfully!")
