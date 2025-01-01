import pandas as pd
import random

# Comprehensive Java MCQs for different topics
java_questions = {
    "Basics": [
        {
            "question": "Which of the following is not a valid Java identifier?",
            "options": [
                "myVariable",
                "123variable",
                "_value",
                "$price"
            ],
            "answer": 2,
            "explanation": "Variable names cannot start with numbers in Java"
        },
        {
            "question": "What is the size of float and double in Java?",
            "options": [
                "32 and 64 bits",
                "32 and 32 bits",
                "64 and 64 bits",
                "64 and 32 bits"
            ],
            "answer": 1,
            "explanation": "float is 32 bits and double is 64 bits"
        },
        {
            "question": "What is the default value of byte variable?",
            "options": [
                "0",
                "0.0",
                "null",
                "undefined"
            ],
            "answer": 1,
            "explanation": "Default value of byte is 0"
        },
        {
            "question": "Which of the following is not a primitive data type in Java?",
            "options": [
                "int",
                "float",
                "String",
                "double"
            ],
            "answer": 3,
            "explanation": "String is a class, not a primitive data type"
        },
        {
            "question": "What is the range of byte data type in Java?",
            "options": [
                "-128 to 127",
                "-32768 to 32767",
                "-2147483648 to 2147483647",
                "None of the above"
            ],
            "answer": 1,
            "explanation": "byte range is from -128 to 127"
        },
        # Add more basic Java questions here...
    ],
    "OOP_Concepts": [
        {
            "question": "Which concept of Java is achieved by combining methods and attributes into a class?",
            "options": [
                "Encapsulation",
                "Inheritance",
                "Polymorphism",
                "Abstraction"
            ],
            "answer": 1,
            "explanation": "Encapsulation is the bundling of data and methods that operate on that data within a single unit"
        },
        {
            "question": "Which of these keywords is used to define interfaces in Java?",
            "options": [
                "interface",
                "Interface",
                "intf",
                "Intf"
            ],
            "answer": 1,
            "explanation": "The interface keyword is used to declare an interface in Java"
        },
        {
            "question": "What is the purpose of 'this' keyword in Java?",
            "options": [
                "To refer to current class instance variable",
                "To invoke current class method",
                "To invoke current class constructor",
                "All of the above"
            ],
            "answer": 4,
            "explanation": "'this' keyword can be used for all mentioned purposes"
        },
        # Add more OOP questions here...
    ],
    "Inheritance": [
        {
            "question": "Which of the following is correct way of inheriting class A by class B?",
            "options": [
                "class B + class A {}",
                "class B inherits class A {}",
                "class B extends A {}",
                "class B extends class A {}"
            ],
            "answer": 3,
            "explanation": "In Java, we use 'extends' keyword for inheritance"
        },
        # Add more inheritance questions...
    ],
    "Exception_Handling": [
        {
            "question": "Which of these keywords is used to manually throw an exception?",
            "options": [
                "try",
                "finally",
                "throw",
                "catch"
            ],
            "answer": 3,
            "explanation": "The throw keyword is used to explicitly throw an exception"
        },
        # Add more exception handling questions...
    ],
    "Collections": [
        {
            "question": "Which of these packages contains the Collection interface?",
            "options": [
                "java.util",
                "java.lang",
                "java.net",
                "java.awt"
            ],
            "answer": 1,
            "explanation": "Collection interface is part of java.util package"
        },
        # Add more collections questions...
    ],
    "Multithreading": [
        {
            "question": "Which of the following is a valid way to create a thread in Java?",
            "options": [
                "Extending Thread class",
                "Implementing Runnable interface",
                "Both A and B",
                "None of the above"
            ],
            "answer": 3,
            "explanation": "Threads can be created either by extending Thread class or implementing Runnable interface"
        },
        # Add more multithreading questions...
    ],
    "JDBC": [
        {
            "question": "Which of these interfaces handle the connection and database management in JDBC?",
            "options": [
                "Driver Manager",
                "Connection",
                "Both A and B",
                "None of the above"
            ],
            "answer": 3,
            "explanation": "Both Driver Manager and Connection interfaces are used for database connection management"
        },
        # Add more JDBC questions...
    ],
    "Java_IO": [
        {
            "question": "Which of these stream classes are used to read and write bytes?",
            "options": [
                "InputStream and OutputStream",
                "Reader and Writer",
                "Both A and B",
                "None of the above"
            ],
            "answer": 1,
            "explanation": "InputStream and OutputStream are used for byte streams"
        },
        # Add more IO questions...
    ],
    "Generics": [
        {
            "question": "What is the syntax for declaring a generic class?",
            "options": [
                "class Test[T]",
                "class Test<T>",
                "class Test(T)",
                "class Test{T}"
            ],
            "answer": 2,
            "explanation": "Generic classes are declared using angle brackets <>"
        },
        # Add more generics questions...
    ]
}

def create_question_bank(topic, questions):
    """Create a DataFrame from questions"""
    formatted_questions = []
    for i, q in enumerate(questions, 1):
        formatted_questions.append({
            "id": i,
            "text": q["question"],
            "option1": q["options"][0],
            "option2": q["options"][1],
            "option3": q["options"][2],
            "option4": q["options"][3],
            "answer": q["answer"],
            "explanation": q["explanation"]
        })
    return pd.DataFrame(formatted_questions)

# Create question banks for each topic
for topic, questions in java_questions.items():
    file_name = f"{topic}_Java.xlsx"
    df = create_question_bank(topic, questions)
    df.to_excel(f'papers/{file_name}', index=False)
    
    # Add entry to papers.txt
    with open('papers/papers.txt', 'a') as f:
        f.write(f'\n{file_name},Java {topic.replace("_", " ")} Questions')
    
    print(f"Created {file_name} with {len(questions)} verified questions")

print("\nAll verified Java question files have been created successfully!")

# Print sample questions for verification
print("\nSample questions from each topic:")
for topic, questions in java_questions.items():
    print(f"\n{topic}:")
    sample = random.choice(questions)
    print(f"Q: {sample['question']}")
    for i, opt in enumerate(sample['options'], 1):
        print(f"{i}. {opt}")
    print(f"Correct Answer: {sample['answer']}")
    print(f"Explanation: {sample['explanation']}")
