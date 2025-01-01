import pandas as pd
import random

# Detailed questions for each topic
topic_questions = {
    "Inheritance": [
        {
            "question": "What type of inheritance is not supported in Java?",
            "options": [
                "Single inheritance",
                "Multiple inheritance through classes",
                "Multilevel inheritance",
                "Hierarchical inheritance"
            ],
            "answer": 2
        },
        {
            "question": "Which keyword is used to inherit a class in Java?",
            "options": [
                "extends",
                "implements",
                "inherits",
                "using"
            ],
            "answer": 1
        },
        {
            "question": "What is the superclass of all classes in Java?",
            "options": [
                "String",
                "Main",
                "Object",
                "Class"
            ],
            "answer": 3
        }
    ],
    "Polymorphism": [
        {
            "question": "Which type of polymorphism is achieved through method overloading?",
            "options": [
                "Runtime polymorphism",
                "Compile-time polymorphism",
                "Multiple polymorphism",
                "Dynamic polymorphism"
            ],
            "answer": 2
        },
        {
            "question": "What is necessary for runtime polymorphism in Java?",
            "options": [
                "Method overloading",
                "Method overriding",
                "Multiple inheritance",
                "Interface implementation"
            ],
            "answer": 2
        }
    ],
    "Encapsulation": [
        {
            "question": "Which access modifier provides the highest level of encapsulation?",
            "options": [
                "public",
                "protected",
                "private",
                "default"
            ],
            "answer": 3
        },
        {
            "question": "What is the main purpose of encapsulation?",
            "options": [
                "To increase code complexity",
                "To hide implementation details and protect data",
                "To improve code performance",
                "To reduce memory usage"
            ],
            "answer": 2
        }
    ],
    "Abstraction": [
        {
            "question": "Which keyword is used to declare an abstract class?",
            "options": [
                "abstract",
                "virtual",
                "static",
                "final"
            ],
            "answer": 1
        },
        {
            "question": "Can an abstract class have a constructor?",
            "options": [
                "Yes, and it can be called directly",
                "Yes, but it can only be called by subclasses",
                "No, abstract classes cannot have constructors",
                "Only if the class has no abstract methods"
            ],
            "answer": 2
        }
    ],
    "Exception_Handling": [
        {
            "question": "Which of these is not a checked exception?",
            "options": [
                "IOException",
                "SQLException",
                "NullPointerException",
                "ClassNotFoundException"
            ],
            "answer": 3
        },
        {
            "question": "What is the order of catch blocks in exception handling?",
            "options": [
                "Most specific to most general",
                "Most general to most specific",
                "Order doesn't matter",
                "Alphabetical order"
            ],
            "answer": 1
        }
    ],
    "Multithreading": [
        {
            "question": "Which method is used to start a thread's execution?",
            "options": [
                "run()",
                "start()",
                "execute()",
                "begin()"
            ],
            "answer": 2
        },
        {
            "question": "What is thread synchronization?",
            "options": [
                "Creating multiple threads",
                "Killing a thread",
                "Preventing thread interference",
                "Making threads run faster"
            ],
            "answer": 3
        }
    ],
    "Collections": [
        {
            "question": "Which collection type should be used for storing unique elements?",
            "options": [
                "ArrayList",
                "LinkedList",
                "HashSet",
                "Vector"
            ],
            "answer": 3
        },
        {
            "question": "Which collection is synchronized by default?",
            "options": [
                "ArrayList",
                "LinkedList",
                "HashSet",
                "Vector"
            ],
            "answer": 4
        }
    ],
    "String_Handling": [
        {
            "question": "Which class is immutable in Java?",
            "options": [
                "String",
                "StringBuilder",
                "StringBuffer",
                "StringTokenizer"
            ],
            "answer": 1
        },
        {
            "question": "Which is more efficient for string concatenation in a loop?",
            "options": [
                "String",
                "StringBuilder",
                "StringBuffer",
                "char[]"
            ],
            "answer": 2
        }
    ],
    "JDBC": [
        {
            "question": "Which interface is used to execute SQL queries in JDBC?",
            "options": [
                "Connection",
                "Statement",
                "ResultSet",
                "DriverManager"
            ],
            "answer": 2
        },
        {
            "question": "What is the first step in JDBC connection?",
            "options": [
                "Creating Statement object",
                "Loading and registering driver",
                "Creating Connection object",
                "Executing queries"
            ],
            "answer": 2
        }
    ],
    "Serialization": [
        {
            "question": "Which interface is used to make a class serializable?",
            "options": [
                "Serializable",
                "Serialization",
                "Serial",
                "ObjectStream"
            ],
            "answer": 1
        },
        {
            "question": "What keyword is used to prevent a variable from being serialized?",
            "options": [
                "static",
                "transient",
                "volatile",
                "final"
            ],
            "answer": 2
        }
    ]
}

def generate_generic_questions(topic, count):
    """Generate generic questions for a topic when we need more questions"""
    generic_templates = [
        f"Which feature of {topic} is most important for object-oriented design?",
        f"How does {topic} contribute to code reusability?",
        f"What is a common use case for {topic} in Java applications?",
        f"Which best practice should be followed when using {topic}?",
        f"What is a potential problem when implementing {topic} incorrectly?"
    ]
    
    generic_options = [
        [f"Feature A of {topic}", f"Feature B of {topic}", f"Feature C of {topic}", f"Feature D of {topic}"],
        [f"Approach 1 for {topic}", f"Approach 2 for {topic}", f"Approach 3 for {topic}", f"Approach 4 for {topic}"],
        [f"Implementation 1 of {topic}", f"Implementation 2 of {topic}", f"Implementation 3 of {topic}", f"Implementation 4 of {topic}"],
        [f"Best practice 1 for {topic}", f"Best practice 2 for {topic}", f"Best practice 3 for {topic}", f"Best practice 4 for {topic}"]
    ]
    
    questions = []
    for i in range(count):
        template = random.choice(generic_templates)
        options = random.choice(generic_options)
        questions.append({
            "question": template,
            "options": options,
            "answer": random.randint(1, 4)
        })
    return questions

def create_topic_question_bank(topic, questions_needed=50):
    """Create a question bank for a specific topic"""
    # Get predefined questions
    predefined = topic_questions.get(topic, [])
    
    # Generate additional questions if needed
    if len(predefined) < questions_needed:
        additional = generate_generic_questions(topic, questions_needed - len(predefined))
        all_questions = predefined + additional
    else:
        all_questions = predefined[:questions_needed]
    
    # Format questions for DataFrame
    formatted_questions = []
    for i, q in enumerate(all_questions, 1):
        formatted_questions.append({
            "id": i,
            "text": q["question"],
            "option1": q["options"][0],
            "option2": q["options"][1],
            "option3": q["options"][2],
            "option4": q["options"][3],
            "answer": q["answer"]
        })
    
    return pd.DataFrame(formatted_questions)

# List of topics to create question banks for
topics = [
    "Inheritance", "Polymorphism", "Encapsulation", "Abstraction",
    "Exception_Handling", "Multithreading", "Collections", 
    "String_Handling", "JDBC", "Serialization"
]

# Create question bank for each topic
for topic in topics:
    file_name = f"{topic}_Java.xlsx"
    df = create_topic_question_bank(topic)
    df.to_excel(f'papers/{file_name}', index=False)
    
    # Add entry to papers.txt
    with open('papers/papers.txt', 'a') as f:
        f.write(f'\n{file_name},Java {topic.replace("_", " ")} Questions')
    
    print(f"Created {file_name}")

print("\nAll topic-specific Java question files have been created successfully!")
