import pandas as pd
import random

def get_question_data(topic, subtopic):
    questions_data = {
        "Basic Concepts": {
            "JVM": {
                "question": "What is the primary function of JVM in Java?",
                "options": [
                    "To compile Java source code into bytecode",
                    "To execute Java bytecode and provide runtime environment",
                    "To debug Java applications",
                    "To create Java documentation"
                ],
                "answer": 2
            },
            "Platform Independence": {
                "question": "Why is Java called platform independent?",
                "options": [
                    "It can only run on Windows",
                    "It requires specific hardware",
                    "Java bytecode can run on any platform with JVM",
                    "It's written in machine code"
                ],
                "answer": 3
            }
        },
        "OOP Concepts": {
            "Inheritance": {
                "question": "Which statement best describes inheritance in Java?",
                "options": [
                    "A mechanism to create multiple objects",
                    "A way to reuse code and establish relationships between classes",
                    "A method to compile code faster",
                    "A tool for debugging"
                ],
                "answer": 2
            },
            "Polymorphism": {
                "question": "What is polymorphism in Java?",
                "options": [
                    "Having multiple main methods",
                    "The ability of an object to take multiple forms",
                    "Creating multiple classes",
                    "Having multiple constructors"
                ],
                "answer": 2
            }
        },
        "Data Types & Variables": {
            "Primitive Types": {
                "question": "Which of these is not a primitive data type in Java?",
                "options": [
                    "byte",
                    "String",
                    "int",
                    "boolean"
                ],
                "answer": 2
            },
            "Type Casting": {
                "question": "What is automatic type conversion in Java?",
                "options": [
                    "Converting a smaller data type to a larger one automatically",
                    "Converting a larger data type to a smaller one",
                    "Converting any type to String",
                    "Converting String to int"
                ],
                "answer": 1
            }
        },
        "Control Flow": {
            "switch": {
                "question": "Which of these can't be used as a case value in switch statement?",
                "options": [
                    "Character literal",
                    "Integer literal",
                    "Boolean value",
                    "String literal (Java 7+)"
                ],
                "answer": 3
            },
            "try-catch": {
                "question": "What is the purpose of try-catch block?",
                "options": [
                    "To define a class",
                    "To handle exceptions and errors",
                    "To create objects",
                    "To implement interfaces"
                ],
                "answer": 2
            }
        },
        "Collections": {
            "ArrayList": {
                "question": "Which of these best describes ArrayList in Java?",
                "options": [
                    "A fixed-size array",
                    "A resizable array implementation of List interface",
                    "A linked list implementation",
                    "A thread-safe collection"
                ],
                "answer": 2
            },
            "HashMap": {
                "question": "What is the key characteristic of HashMap?",
                "options": [
                    "Maintains insertion order",
                    "Stores only strings",
                    "Stores key-value pairs",
                    "Is synchronized"
                ],
                "answer": 3
            }
        }
    }
    
    # If specific question exists, return it
    if topic in questions_data and subtopic in questions_data[topic]:
        return questions_data[topic][subtopic]
    
    # Otherwise, generate a generic question
    generic_questions = {
        "Basic Concepts": {
            "question": f"Which statement is true about {subtopic} in Java?",
            "options": [
                f"It is used for memory management in {subtopic}",
                f"It provides platform independence through {subtopic}",
                f"It helps in code organization using {subtopic}",
                f"It optimizes performance using {subtopic}"
            ]
        },
        "OOP Concepts": {
            "question": f"How does {subtopic} contribute to Object-Oriented Programming?",
            "options": [
                f"It enables code reusability through {subtopic}",
                f"It provides data hiding using {subtopic}",
                f"It implements runtime polymorphism via {subtopic}",
                f"It supports multiple inheritance with {subtopic}"
            ]
        },
        "Data Types & Variables": {
            "question": f"What is the main purpose of {subtopic} in Java?",
            "options": [
                f"To store primitive data types using {subtopic}",
                f"To manage memory allocation for {subtopic}",
                f"To perform type conversion with {subtopic}",
                f"To handle complex data structures using {subtopic}"
            ]
        },
        "Control Flow": {
            "question": f"How does {subtopic} affect program execution?",
            "options": [
                f"It controls program flow using {subtopic}",
                f"It handles exceptions through {subtopic}",
                f"It manages loops with {subtopic}",
                f"It implements conditional logic via {subtopic}"
            ]
        },
        "Collections": {
            "question": f"What is the primary use of {subtopic} in Collections framework?",
            "options": [
                f"To store and manage data using {subtopic}",
                f"To provide thread-safe operations with {subtopic}",
                f"To implement sorting algorithms through {subtopic}",
                f"To handle data structures efficiently using {subtopic}"
            ]
        }
    }
    
    template = generic_questions.get(topic, generic_questions["Basic Concepts"])
    return {
        "question": template["question"],
        "options": template["options"],
        "answer": random.randint(1, 4)
    }

def generate_java_questions(start_id=1):
    topics = [
        ("Basic Concepts", [
            "JVM", "JRE", "JDK", "Platform Independence",
            "Bytecode", "Class Loading", "Access Modifiers", "Package Declaration",
            "Import Statements", "Garbage Collection"
        ]),
        ("OOP Concepts", [
            "Inheritance", "Polymorphism", "Encapsulation", "Abstraction",
            "Interface", "Abstract Class", "Method Overriding", "Method Overloading",
            "Constructor", "this keyword"
        ]),
        ("Data Types & Variables", [
            "Primitive Types", "Reference Types", "Type Casting", "Arrays",
            "String", "StringBuilder", "Variable Scope", "Final Keyword",
            "Static Variables", "Instance Variables"
        ]),
        ("Control Flow", [
            "if-else", "switch", "for loop", "while loop", "do-while",
            "break", "continue", "return", "try-catch", "throw"
        ]),
        ("Collections", [
            "ArrayList", "LinkedList", "HashMap", "HashSet", "TreeMap",
            "TreeSet", "Queue", "Stack", "Vector", "Collections Class"
        ])
    ]
    
    questions = []
    for i in range(100):
        topic, subtopics = random.choice(topics)
        subtopic = random.choice(subtopics)
        
        question_data = get_question_data(topic, subtopic)
        
        question = {
            "id": start_id + i,
            "text": question_data["question"],
            "option1": question_data["options"][0],
            "option2": question_data["options"][1],
            "option3": question_data["options"][2],
            "option4": question_data["options"][3],
            "answer": question_data["answer"]
        }
        questions.append(question)
    
    return questions

# Create 20 different question banks
for file_num in range(1, 21):
    # Generate questions
    questions = generate_java_questions(start_id=1)
    
    # Convert to DataFrame
    df = pd.DataFrame(questions)
    
    # Format file name with leading zero
    file_name = f'Java_{file_num:02d}.xlsx'
    
    # Save to Excel file
    df.to_excel(f'papers/{file_name}', index=False)
    
    # Add entry to papers.txt
    with open('papers/papers.txt', 'a') as f:
        f.write(f'\n{file_name},Java Programming Set {file_num:02d}')
    
    print(f"Created {file_name}")

print("\nAll Java question files have been created successfully!")
