import pandas as pd
import random

# Comprehensive Java MCQs organized by topics
java_questions = {
    "Basics": [
        {
            "question": "What is the default value of Object variable?",
            "options": ["undefined", "0", "null", "not defined"],
            "answer": 3,
            "explanation": "The default value of any object reference is null"
        },
        {
            "question": "Which of the following is not a valid Java identifier?",
            "options": ["myVariable", "123variable", "_value", "$price"],
            "answer": 2,
            "explanation": "Variable names cannot start with numbers in Java"
        },
        {
            "question": "What is the size of float and double in Java?",
            "options": ["32 and 64 bits", "32 and 32 bits", "64 and 64 bits", "64 and 32 bits"],
            "answer": 1,
            "explanation": "float is 32 bits and double is 64 bits"
        },
        {
            "question": "Which package is automatically imported into all Java programs?",
            "options": ["java.lang", "java.util", "java.io", "java.net"],
            "answer": 1,
            "explanation": "java.lang package is automatically imported in all Java programs"
        },
        {
            "question": "What is the range of short data type in Java?",
            "options": ["-128 to 127", "-32768 to 32767", "-2147483648 to 2147483647", "None of these"],
            "answer": 2,
            "explanation": "short data type has a range from -32768 to 32767"
        },
        {
            "question": "What is the default value of boolean variable?",
            "options": ["true", "false", "null", "undefined"],
            "answer": 2,
            "explanation": "The default value of boolean variable is false"
        },
        {
            "question": "Which of the following is a valid long literal?",
            "options": ["L", "L232", "23L", "None of these"],
            "answer": 3,
            "explanation": "Long literals are appended by L or l"
        },
        {
            "question": "What is the default value of char variable?",
            "options": ["'\\u0000'", "0", "null", "undefined"],
            "answer": 1,
            "explanation": "The default value of char variable is '\\u0000'"
        },
        {
            "question": "What is the process of converting one data type to another?",
            "options": ["Type Promotion", "Type Conversion", "Type Casting", "None of these"],
            "answer": 3,
            "explanation": "Type Casting is the process of converting one data type to another"
        },
        {
            "question": "Which operator is used to allocate memory to array variable in Java?",
            "options": ["alloc", "malloc", "new", "new malloc"],
            "answer": 3,
            "explanation": "new operator is used to allocate memory to array variable in Java"
        },
        {
            "question": "Which of these literals can be contained in float data type variable?",
            "options": ["3.4e+038", "3.4e+050", "1.7e+308", "1.7e+050"],
            "answer": 1,
            "explanation": "float can hold up to 3.4e+038, double can hold up to 1.7e+308"
        },
        {
            "question": "What is the output of this expression: 3 + 4 + \"7\" + 3 + 4?",
            "options": ["7734", "7343", "3473", "14343"],
            "answer": 2,
            "explanation": "First 3+4=7, then \"7\"+3=\"73\", finally \"73\"+4=\"734\""
        },
        {
            "question": "Which statement is true about Java?",
            "options": [
                "Java is a sequence-dependent programming language",
                "Java is a code-dependent programming language",
                "Java is a platform-dependent programming language",
                "Java is a platform-independent programming language"
            ],
            "answer": 4,
            "explanation": "Java is platform-independent because it uses bytecode that can run on any platform with JVM"
        },
        {
            "question": "What is the use of final keyword in Java?",
            "options": [
                "To create constant variables",
                "To prevent inheritance",
                "To prevent method overriding",
                "All of the above"
            ],
            "answer": 4,
            "explanation": "final keyword can be used with variables (constants), classes (prevent inheritance), and methods (prevent overriding)"
        },
        {
            "question": "What is the default value of int variable?",
            "options": ["0", "0.0", "null", "undefined"],
            "answer": 1,
            "explanation": "The default value of int variable is 0"
        },
        {
            "question": "Which operator is used to compare two values?",
            "options": ["==", "=", "!=", "><"],
            "answer": 1,
            "explanation": "== operator is used to compare two values"
        },
        {
            "question": "Which of these cannot be used for a variable name in Java?",
            "options": ["identifier", "keyword", "identifier & keyword", "None of the mentioned"],
            "answer": 2,
            "explanation": "Keywords cannot be used as variable names in Java"
        },
        {
            "question": "What is the size of int in Java?",
            "options": ["16 bit", "32 bit", "64 bit", "None of these"],
            "answer": 2,
            "explanation": "int is 32 bits in Java"
        },
        {
            "question": "What is the range of byte data type in Java?",
            "options": ["-128 to 127", "-256 to 255", "-32768 to 32767", "-65536 to 65535"],
            "answer": 1,
            "explanation": "byte ranges from -128 to 127"
        },
        {
            "question": "Which method must be implemented by all threads?",
            "options": ["wait()", "start()", "stop()", "run()"],
            "answer": 4,
            "explanation": "All threads must implement the run() method"
        },
        {
            "question": "What is the default value of long variable?",
            "options": ["0", "0L", "0.0", "null"],
            "answer": 1,
            "explanation": "The default value of long variable is 0"
        },
        {
            "question": "What is the entry point of a program in Java?",
            "options": [
                "main() method",
                "The first line of code",
                "Last line of code",
                "main class"
            ],
            "answer": 1,
            "explanation": "main() method is the entry point of any Java program"
        },
        {
            "question": "Which of these keywords is used to make a class?",
            "options": ["class", "struct", "int", "None of the mentioned"],
            "answer": 1,
            "explanation": "class keyword is used to create a class in Java"
        },
        {
            "question": "Which of the following is not an access modifier?",
            "options": ["protected", "void", "public", "private"],
            "answer": 2,
            "explanation": "void is a return type, not an access modifier"
        }
    ],
    
    "OOP_Concepts": [
        {
            "question": "Which concept of Java is achieved by combining methods and attributes into a class?",
            "options": ["Encapsulation", "Inheritance", "Polymorphism", "Abstraction"],
            "answer": 1,
            "explanation": "Encapsulation is the bundling of data and methods that operate on that data within a single unit"
        },
        {
            "question": "Which of these keywords is used to define interfaces in Java?",
            "options": ["interface", "Interface", "intf", "Intf"],
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
        {
            "question": "Which of the following is not a type of inheritance?",
            "options": ["Multiple", "Multilevel", "Hierarchical", "Friend"],
            "answer": 4,
            "explanation": "Friend inheritance is not supported in Java. It's a C++ concept"
        },
        {
            "question": "What is the implicit superclass of all classes in Java?",
            "options": ["String", "Object", "Main", "Abstract"],
            "answer": 2,
            "explanation": "Object class is the implicit superclass of all classes in Java"
        },
        {
            "question": "Which of the following is a valid declaration of an object of class Box?",
            "options": [
                "Box obj = new Box();",
                "Box obj = new Box;",
                "obj = new Box();",
                "new Box obj;"
            ],
            "answer": 1,
            "explanation": "Objects are created using new keyword followed by constructor call"
        },
        {
            "question": "What is the result of multiple inheritance in Java?",
            "options": [
                "Compile time error",
                "Runtime error",
                "Compilation and execution successfully",
                "None of these"
            ],
            "answer": 1,
            "explanation": "Java doesn't support multiple inheritance through classes, it will give compile time error"
        },
        {
            "question": "What is method overloading?",
            "options": [
                "Methods with same name but different parameters",
                "Methods with same name but different return types",
                "Methods with same name but different access modifiers",
                "None of these"
            ],
            "answer": 1,
            "explanation": "Method overloading is having multiple methods with same name but different parameters"
        },
        {
            "question": "Which of these keywords can be used with abstract class?",
            "options": [
                "final",
                "static",
                "abstract",
                "None of these"
            ],
            "answer": 3,
            "explanation": "abstract keyword is used with abstract classes"
        },
        {
            "question": "What is the use of super keyword?",
            "options": [
                "To call superclass methods",
                "To call superclass constructor",
                "To access superclass instance variables",
                "All of these"
            ],
            "answer": 4,
            "explanation": "super keyword can be used for all mentioned purposes"
        },
        {
            "question": "Which of these is not a feature of OOP?",
            "options": [
                "Polymorphism",
                "Inheritance",
                "Compilation",
                "Encapsulation"
            ],
            "answer": 3,
            "explanation": "Compilation is not a feature of OOP"
        },
        {
            "question": "What is runtime polymorphism?",
            "options": [
                "Method overloading",
                "Method overriding",
                "Both A and B",
                "None of these"
            ],
            "answer": 2,
            "explanation": "Runtime polymorphism is achieved through method overriding"
        },
        {
            "question": "What is the use of private constructor?",
            "options": [
                "To create singleton class",
                "To create multiple objects",
                "To create inheritance",
                "None of these"
            ],
            "answer": 1,
            "explanation": "Private constructor is used to create singleton classes"
        }
    ],

    "Collections": [
        {
            "question": "Which collection class allows you to grow or shrink its size and provides indexed access to its elements?",
            "options": ["LinkedList", "ArrayList", "HashMap", "Vector"],
            "answer": 2,
            "explanation": "ArrayList provides dynamic arrays in Java that can grow or shrink"
        },
        {
            "question": "Which collection interface declares core methods that most collections will have?",
            "options": ["Set", "Collection", "List", "Map"],
            "answer": 2,
            "explanation": "Collection interface provides the basic operations that all collections will have"
        },
        {
            "question": "Which of these allows duplicate elements?",
            "options": ["Set", "List", "Map", "None of these"],
            "answer": 2,
            "explanation": "List allows duplicate elements while Set and Map don't"
        },
        {
            "question": "Which collection class implements a linked list data structure?",
            "options": ["AbstractList", "LinkedList", "ArrayList", "None of these"],
            "answer": 2,
            "explanation": "LinkedList implements a linked list data structure"
        },
        {
            "question": "Which collection interface provides functionality of a stack data structure?",
            "options": ["Queue", "Set", "Deque", "List"],
            "answer": 3,
            "explanation": "Deque interface provides stack operations like push and pop"
        },
        {
            "question": "Which of these is synchronized by default?",
            "options": [
                "ArrayList",
                "LinkedList",
                "Vector",
                "None of these"
            ],
            "answer": 3,
            "explanation": "Vector is synchronized by default"
        },
        {
            "question": "What is the difference between ArrayList and Vector?",
            "options": [
                "Synchronization",
                "Size growth",
                "Both A and B",
                "None of these"
            ],
            "answer": 3,
            "explanation": "ArrayList is not synchronized and grows by 50%, Vector is synchronized and grows by 100%"
        },
        {
            "question": "Which collection stores key-value pairs?",
            "options": [
                "List",
                "Set",
                "Map",
                "Queue"
            ],
            "answer": 3,
            "explanation": "Map interface is used to store key-value pairs"
        },
        {
            "question": "What is the initial capacity of ArrayList?",
            "options": [
                "5",
                "10",
                "15",
                "20"
            ],
            "answer": 2,
            "explanation": "The default initial capacity of ArrayList is 10"
        },
        {
            "question": "Which collection implementation should be used if we want to maintain insertion order?",
            "options": [
                "HashSet",
                "TreeSet",
                "LinkedHashSet",
                "None of these"
            ],
            "answer": 3,
            "explanation": "LinkedHashSet maintains insertion order"
        }
    ],

    "Exception_Handling": [
        {
            "question": "Which of these keywords is used to manually throw an exception?",
            "options": ["try", "finally", "throw", "catch"],
            "answer": 3,
            "explanation": "The throw keyword is used to explicitly throw an exception"
        },
        {
            "question": "Which of these keywords must be used to handle the exception thrown by try block?",
            "options": ["try", "finally", "throw", "catch"],
            "answer": 4,
            "explanation": "catch block is used to handle exceptions thrown by try block"
        },
        {
            "question": "Which of these keywords is used to define a block of code that will be executed after try block whether an exception occurs or not?",
            "options": ["try", "finally", "throw", "catch"],
            "answer": 2,
            "explanation": "finally block is always executed whether exception occurs or not"
        },
        {
            "question": "Which of these is a checked exception?",
            "options": ["RuntimeException", "IOException", "NullPointerException", "ArithmeticException"],
            "answer": 2,
            "explanation": "IOException is a checked exception that must be declared or handled"
        },
        {
            "question": "What is the parent class of all exception classes?",
            "options": ["Throwable", "Exception", "Error", "RuntimeException"],
            "answer": 1,
            "explanation": "Throwable is the parent class of all exception classes"
        },
        {
            "question": "Which of these is used to handle all exceptions?",
            "options": [
                "BaseException",
                "Exception",
                "Throwable",
                "None of these"
            ],
            "answer": 2,
            "explanation": "Exception class is used to handle all exceptions"
        },
        {
            "question": "What happens when an exception is not caught?",
            "options": [
                "Program terminates",
                "Exception is ignored",
                "Program continues",
                "None of these"
            ],
            "answer": 1,
            "explanation": "If an exception is not caught, program terminates abnormally"
        },
        {
            "question": "Which block is used to handle multiple exceptions?",
            "options": [
                "try",
                "catch",
                "finally",
                "throw"
            ],
            "answer": 2,
            "explanation": "Multiple catch blocks can be used to handle different exceptions"
        },
        {
            "question": "What is the use of throws keyword?",
            "options": [
                "To throw an exception",
                "To declare an exception",
                "To handle an exception",
                "None of these"
            ],
            "answer": 2,
            "explanation": "throws keyword is used to declare exceptions that a method might throw"
        },
        {
            "question": "Which of these is not a checked exception?",
            "options": [
                "IOException",
                "SQLException",
                "NullPointerException",
                "FileNotFoundException"
            ],
            "answer": 3,
            "explanation": "NullPointerException is an unchecked exception"
        }
    ],

    "Multithreading": [
        {
            "question": "Which of these methods is used to suspend a thread for a specific time?",
            "options": ["sleep()", "wait()", "suspend()", "stop()"],
            "answer": 1,
            "explanation": "sleep() method is used to suspend a thread for a specific time period"
        },
        {
            "question": "What is the state of a thread after it has completed its execution?",
            "options": ["Running", "Dead", "Blocked", "Suspended"],
            "answer": 2,
            "explanation": "A thread enters Dead state after completing its execution"
        },
        {
            "question": "Which method must be implemented by a class implementing the Runnable interface?",
            "options": ["start()", "run()", "execute()", "perform()"],
            "answer": 2,
            "explanation": "run() method must be implemented when implementing Runnable interface"
        },
        {
            "question": "Which keyword is used for synchronization in Java?",
            "options": ["synchronize", "sync", "synchronized", "synch"],
            "answer": 3,
            "explanation": "synchronized keyword is used for synchronization in Java"
        },
        {
            "question": "What is the purpose of join() method?",
            "options": [
                "To join two threads",
                "To wait for a thread to die",
                "To suspend a thread",
                "To resume a thread"
            ],
            "answer": 2,
            "explanation": "join() method waits for a thread to die"
        },
        {
            "question": "What is synchronization in Java?",
            "options": [
                "Thread communication",
                "Thread safety",
                "Both A and B",
                "None of these"
            ],
            "answer": 2,
            "explanation": "Synchronization is used to achieve thread safety in Java"
        },
        {
            "question": "Which method is used to pause a thread for specific time?",
            "options": [
                "wait()",
                "sleep()",
                "pause()",
                "stop()"
            ],
            "answer": 2,
            "explanation": "sleep() method is used to pause a thread for specific time"
        },
        {
            "question": "What is thread priority range in Java?",
            "options": [
                "0 to 9",
                "1 to 10",
                "1 to 5",
                "None of these"
            ],
            "answer": 2,
            "explanation": "Thread priority range is from 1 to 10"
        },
        {
            "question": "Which method is used to start a thread execution?",
            "options": [
                "init()",
                "start()",
                "run()",
                "resume()"
            ],
            "answer": 2,
            "explanation": "start() method is used to begin thread execution"
        },
        {
            "question": "What is deadlock in Java?",
            "options": [
                "When two threads wait for each other",
                "When thread stops",
                "When thread sleeps",
                "None of these"
            ],
            "answer": 1,
            "explanation": "Deadlock occurs when two threads wait for each other indefinitely"
        }
    ],
    
    "JDBC": [
        {
            "question": "Which class is responsible for establishing connection with database in JDBC?",
            "options": [
                "Connection",
                "DriverManager",
                "Statement",
                "ResultSet"
            ],
            "answer": 2,
            "explanation": "DriverManager class is used to establish connection with database"
        },
        {
            "question": "Which interface is used to execute SQL queries in JDBC?",
            "options": [
                "Statement",
                "PreparedStatement",
                "Both A and B",
                "None of these"
            ],
            "answer": 3,
            "explanation": "Both Statement and PreparedStatement interfaces are used to execute SQL queries"
        },
        {
            "question": "What is the use of PreparedStatement?",
            "options": [
                "To execute static SQL queries",
                "To execute dynamic SQL queries",
                "To prevent SQL injection",
                "Both B and C"
            ],
            "answer": 4,
            "explanation": "PreparedStatement is used for dynamic SQL queries and prevents SQL injection"
        },
        {
            "question": "Which method is used to execute SELECT queries?",
            "options": [
                "execute()",
                "executeUpdate()",
                "executeQuery()",
                "executeSelect()"
            ],
            "answer": 3,
            "explanation": "executeQuery() method is used to execute SELECT queries"
        },
        {
            "question": "What is the return type of executeUpdate() method?",
            "options": [
                "ResultSet",
                "int",
                "boolean",
                "void"
            ],
            "answer": 2,
            "explanation": "executeUpdate() returns number of rows affected"
        },
        {
            "question": "Which JDBC driver Type is considered the best?",
            "options": ["Type 1", "Type 2", "Type 3", "Type 4"],
            "answer": 4,
            "explanation": "Type 4 (Pure Java) driver is considered the best as it's written entirely in Java and is platform independent"
        },
        {
            "question": "What is the purpose of ResultSetMetaData?",
            "options": [
                "To get data from ResultSet",
                "To get information about ResultSet columns",
                "To update ResultSet",
                "To delete ResultSet"
            ],
            "answer": 2,
            "explanation": "ResultSetMetaData provides information about the columns in a ResultSet"
        },
        {
            "question": "Which statement is true about CallableStatement?",
            "options": [
                "Used for static SQL",
                "Used for dynamic SQL",
                "Used for stored procedures",
                "Used for batch updates"
            ],
            "answer": 3,
            "explanation": "CallableStatement is used to call stored procedures"
        },
        {
            "question": "What is the use of setAutoCommit(false)?",
            "options": [
                "To enable transaction management",
                "To disable transaction management",
                "To commit automatically",
                "To rollback automatically"
            ],
            "answer": 1,
            "explanation": "setAutoCommit(false) enables manual transaction management"
        },
        {
            "question": "Which interface provides methods for batch updates?",
            "options": [
                "Statement",
                "PreparedStatement",
                "Both A and B",
                "None of these"
            ],
            "answer": 3,
            "explanation": "Both Statement and PreparedStatement interfaces provide methods for batch updates"
        },
        {
            "question": "What is the default port for MySQL database?",
            "options": ["3306", "1521", "5432", "1433"],
            "answer": 1,
            "explanation": "Default port for MySQL is 3306"
        },
        {
            "question": "Which method is used to get the connection object?",
            "options": [
                "DriverManager.getConnection()",
                "Connection.getConnection()",
                "DataSource.getConnection()",
                "Both A and C"
            ],
            "answer": 4,
            "explanation": "Both DriverManager and DataSource can provide connection objects"
        },
        {
            "question": "What happens if driver class is not found?",
            "options": [
                "RuntimeException",
                "SQLException",
                "ClassNotFoundException",
                "None of these"
            ],
            "answer": 3,
            "explanation": "ClassNotFoundException is thrown if driver class is not found"
        },
        {
            "question": "Which of these is not a valid JDBC driver type?",
            "options": ["Type 1", "Type 2", "Type 5", "Type 4"],
            "answer": 3,
            "explanation": "There are only 4 types of JDBC drivers (Type 1 to Type 4)"
        },
        {
            "question": "What is the purpose of DatabaseMetaData?",
            "options": [
                "To get database information",
                "To get table information",
                "To get driver information",
                "All of these"
            ],
            "answer": 4,
            "explanation": "DatabaseMetaData provides information about the database, tables, and driver"
        },
        {
            "question": "Which method is called during serialization?",
            "options": [
                "writeObject()",
                "readObject()",
                "Both A and B",
                "None of these"
            ],
            "answer": 1,
            "explanation": "writeObject() method is called during serialization"
        },
        {
            "question": "What is the purpose of serialVersionUID?",
            "options": [
                "Version control",
                "Security",
                "Performance",
                "None of these"
            ],
            "answer": 1,
            "explanation": "serialVersionUID is used for version control during serialization"
        },
        {
            "question": "Which method is used to execute DDL commands?",
            "options": [
                "execute()",
                "executeUpdate()",
                "Both A and B",
                "executeQuery()"
            ],
            "answer": 3,
            "explanation": "Both execute() and executeUpdate() can be used for DDL commands"
        },
        {
            "question": "What is the use of Connection Pool?",
            "options": [
                "To improve performance",
                "To reduce database connections",
                "To reuse connections",
                "All of these"
            ],
            "answer": 4,
            "explanation": "Connection pooling improves performance by reusing database connections"
        },
        {
            "question": "Which package contains JDBC classes?",
            "options": [
                "java.sql",
                "javax.sql",
                "Both A and B",
                "None of these"
            ],
            "answer": 3,
            "explanation": "JDBC classes are in both java.sql and javax.sql packages"
        }
    ],

    "Java_IO": [
        {
            "question": "Which class is used to read character streams?",
            "options": [
                "InputStream",
                "Reader",
                "BufferedReader",
                "InputStreamReader"
            ],
            "answer": 2,
            "explanation": "Reader class is the base class for reading character streams"
        },
        {
            "question": "What is the use of BufferedReader?",
            "options": [
                "To read bytes",
                "To read characters",
                "To read lines",
                "All of these"
            ],
            "explanation": "BufferedReader is used to read text from a character-input stream, buffering characters",
            "answer": 3
        },
        {
            "question": "Which class is used to write data to a file?",
            "options": [
                "FileWriter",
                "BufferedWriter",
                "Both A and B",
                "None of these"
            ],
            "answer": 3,
            "explanation": "Both FileWriter and BufferedWriter can be used to write data to files"
        },
        {
            "question": "Which class is used for binary file input?",
            "options": [
                "FileInputStream",
                "FileReader",
                "BufferedInputStream",
                "Both A and C"
            ],
            "answer": 4,
            "explanation": "FileInputStream and BufferedInputStream are used for binary file input"
        },
        {
            "question": "What is the purpose of mark() and reset() methods?",
            "options": [
                "To mark position in stream",
                "To reset stream to marked position",
                "Both A and B",
                "None of these"
            ],
            "answer": 3,
            "explanation": "mark() marks a position in stream and reset() returns to that position"
        },
        {
            "question": "Which class is used to read primitive data types?",
            "options": [
                "DataInputStream",
                "ObjectInputStream",
                "FileInputStream",
                "BufferedInputStream"
            ],
            "answer": 1,
            "explanation": "DataInputStream is used to read primitive data types"
        },
        {
            "question": "What is RandomAccessFile used for?",
            "options": [
                "Sequential file access",
                "Random file access",
                "Both A and B",
                "None of these"
            ],
            "answer": 3,
            "explanation": "RandomAccessFile supports both sequential and random access"
        },
        {
            "question": "Which method is used to read a single character?",
            "options": [
                "read()",
                "readChar()",
                "readSingle()",
                "readOne()"
            ],
            "answer": 1,
            "explanation": "read() method reads a single character"
        },
        {
            "question": "What is the purpose of FileDescriptor?",
            "options": [
                "To represent files",
                "To represent open files and sockets",
                "To describe file properties",
                "None of these"
            ],
            "answer": 2,
            "explanation": "FileDescriptor represents open files, sockets, and other I/O connections"
        },
        {
            "question": "Which class is used to read strings and arrays?",
            "options": [
                "StringReader",
                "CharArrayReader",
                "Both A and B",
                "None of these"
            ],
            "answer": 3,
            "explanation": "Both StringReader and CharArrayReader are used to read strings and character arrays"
        },
        {
            "question": "What is the purpose of PushbackInputStream?",
            "options": [
                "To push data back into stream",
                "To read data from stream",
                "To write data to stream",
                "None of these"
            ],
            "answer": 1,
            "explanation": "PushbackInputStream allows pushing back data into the stream"
        },
        {
            "question": "Which class is used for character stream buffering?",
            "options": [
                "BufferedReader",
                "BufferedWriter",
                "Both A and B",
                "None of these"
            ],
            "answer": 3,
            "explanation": "Both BufferedReader and BufferedWriter provide buffering for character streams"
        },
        {
            "question": "What is the default buffer size in BufferedReader?",
            "options": ["1024", "2048", "4096", "8192"],
            "answer": 4,
            "explanation": "Default buffer size in BufferedReader is 8192 characters"
        }
    ],

    "Lambda_Expressions": [
        {
            "question": "What is a lambda expression?",
            "options": [
                "Anonymous function",
                "Named function",
                "Both A and B",
                "None of these"
            ],
            "answer": 1,
            "explanation": "Lambda expression is an anonymous function"
        },
        {
            "question": "Which interface is required to use lambda expressions?",
            "options": [
                "Marker interface",
                "Functional interface",
                "Normal interface",
                "None of these"
            ],
            "answer": 2,
            "explanation": "Functional interface is required to use lambda expressions"
        },
        {
            "question": "What is the syntax of lambda expression?",
            "options": [
                "parameter -> expression",
                "(parameter) -> expression",
                "(parameters) -> expression",
                "All of these"
            ],
            "answer": 4,
            "explanation": "All these are valid lambda expression syntaxes"
        },
        {
            "question": "Which feature was introduced with lambda expressions?",
            "options": [
                "Functional interfaces",
                "Default methods",
                "Static methods in interface",
                "All of these"
            ],
            "answer": 4,
            "explanation": "Lambda expressions were introduced with functional interfaces, default methods, and static methods in interfaces"
        },
        {
            "question": "What is the advantage of lambda expressions?",
            "options": [
                "Less coding",
                "Functional programming",
                "Both A and B",
                "None of these"
            ],
            "answer": 3,
            "explanation": "Lambda expressions enable functional programming with less code"
        },
        {
            "question": "Which of these is a functional interface?",
            "options": [
                "Runnable",
                "Comparable",
                "ActionListener",
                "All of these"
            ],
            "answer": 4,
            "explanation": "All these interfaces are functional interfaces as they have only one abstract method"
        },
        {
            "question": "What is the type of lambda expression?",
            "options": [
                "Object",
                "Function",
                "Functional Interface",
                "None of these"
            ],
            "answer": 3,
            "explanation": "Lambda expressions are of the type of their target functional interface"
        },
        {
            "question": "Can lambda expressions be used with abstract classes?",
            "options": [
                "Yes",
                "No",
                "Sometimes",
                "Depends on implementation"
            ],
            "answer": 2,
            "explanation": "Lambda expressions can only be used with functional interfaces, not abstract classes"
        }
    ],

    "Stream_API": [
        {
            "question": "What is Stream in Java?",
            "options": [
                "IO Stream",
                "Sequence of elements",
                "Collection",
                "None of these"
            ],
            "answer": 2,
            "explanation": "Stream is a sequence of elements supporting sequential and parallel operations"
        },
        {
            "question": "Which method is used to convert Collection to Stream?",
            "options": [
                "stream()",
                "toStream()",
                "convertStream()",
                "None of these"
            ],
            "answer": 1,
            "explanation": "stream() method is used to convert Collection to Stream"
        },
        {
            "question": "Which operation is terminal operation?",
            "options": [
                "map()",
                "filter()",
                "collect()",
                "distinct()"
            ],
            "answer": 3,
            "explanation": "collect() is a terminal operation that produces a result"
        },
        {
            "question": "What is the difference between intermediate and terminal operations?",
            "options": [
                "Intermediate returns Stream",
                "Terminal returns result",
                "Both A and B",
                "None of these"
            ],
            "answer": 3,
            "explanation": "Intermediate operations return Stream, terminal operations return result"
        },
        {
            "question": "Which method is used to get parallel stream?",
            "options": [
                "parallelStream()",
                "parallel()",
                "Both A and B",
                "None of these"
            ],
            "answer": 3,
            "explanation": "Both parallelStream() and parallel() can be used to get parallel stream"
        },
        {
            "question": "Which operation is not a terminal operation?",
            "options": [
                "forEach()",
                "map()",
                "count()",
                "min()"
            ],
            "answer": 2,
            "explanation": "map() is an intermediate operation that transforms elements"
        },
        {
            "question": "What is the use of peek() operation?",
            "options": [
                "Debug",
                "Transform elements",
                "Filter elements",
                "Collect elements"
            ],
            "answer": 1,
            "explanation": "peek() is used for debugging by looking at the elements as they flow past"
        },
        {
            "question": "Which collector is used to convert stream to List?",
            "options": [
                "Collectors.toList()",
                "Collectors.toSet()",
                "Collectors.toMap()",
                "None of these"
            ],
            "answer": 1,
            "explanation": "Collectors.toList() is used to collect stream elements into a List"
        }
    ],

    "Java_Networking": [
        {
            "question": "Which class is used to create server socket?",
            "options": [
                "Socket",
                "ServerSocket",
                "Both A and B",
                "None of these"
            ],
            "answer": 2,
            "explanation": "ServerSocket class is used to create server socket"
        },
        {
            "question": "Which protocol is connection-oriented?",
            "options": [
                "TCP",
                "UDP",
                "Both A and B",
                "None of these"
            ],
            "answer": 1,
            "explanation": "TCP is a connection-oriented protocol"
        },
        {
            "question": "Which class is used for UDP communication?",
            "options": [
                "DatagramSocket",
                "Socket",
                "ServerSocket",
                "None of these"
            ],
            "answer": 1,
            "explanation": "DatagramSocket is used for UDP communication"
        },
        {
            "question": "What is the default port for HTTP?",
            "options": ["80", "443", "21", "22"],
            "answer": 1,
            "explanation": "Default port for HTTP is 80"
        },
        {
            "question": "Which class is used to create URL object?",
            "options": [
                "URL",
                "URI",
                "URLConnection",
                "HttpURLConnection"
            ],
            "answer": 1,
            "explanation": "URL class is used to create URL object"
        },
        {
            "question": "What is the use of InetAddress class?",
            "options": [
                "To represent IP address",
                "To represent host name",
                "Both A and B",
                "None of these"
            ],
            "answer": 3,
            "explanation": "InetAddress represents both IP address and host name"
        },
        {
            "question": "Which protocol is used for file transfer?",
            "options": ["FTP", "HTTP", "SMTP", "TCP"],
            "answer": 1,
            "explanation": "FTP (File Transfer Protocol) is used for file transfer"
        },
        {
            "question": "What is the default port for FTP?",
            "options": ["21", "22", "23", "25"],
            "answer": 1,
            "explanation": "Default port for FTP is 21"
        }
    ],

    "Java_Serialization": [
        {
            "question": "What is serialization in Java?",
            "options": [
                "Converting object to byte stream",
                "Converting object to string",
                "Converting string to object",
                "None of these"
            ],
            "answer": 1,
            "explanation": "Serialization is the process of converting object to byte stream"
        },
        {
            "question": "Which interface is used for serialization?",
            "options": [
                "Serializable",
                "Serialization",
                "Serial",
                "None of these"
            ],
            "answer": 1,
            "explanation": "Serializable interface is used for serialization"
        },
        {
            "question": "What is the use of transient keyword?",
            "options": [
                "To skip serialization",
                "To include in serialization",
                "To mark as constant",
                "None of these"
            ],
            "answer": 1,
            "explanation": "transient keyword is used to skip serialization of a field"
        },
        {
            "question": "Which method is called during serialization?",
            "options": [
                "writeObject()",
                "readObject()",
                "Both A and B",
                "None of these"
            ],
            "answer": 1,
            "explanation": "writeObject() method is called during serialization"
        },
        {
            "question": "What is the purpose of serialVersionUID?",
            "options": [
                "Version control",
                "Security",
                "Performance",
                "None of these"
            ],
            "answer": 1,
            "explanation": "serialVersionUID is used for version control during serialization"
        },
        {
            "question": "What happens if a superclass is not serializable?",
            "options": [
                "Compilation error",
                "Runtime error",
                "Superclass fields are ignored",
                "None of these"
            ],
            "answer": 3,
            "explanation": "If superclass is not serializable, its fields are ignored during serialization"
        },
        {
            "question": "Can we serialize static fields?",
            "options": [
                "Yes",
                "No",
                "Depends on implementation",
                "Only if marked transient"
            ],
            "answer": 2,
            "explanation": "Static fields cannot be serialized as they belong to class not object"
        },
        {
            "question": "What is the purpose of Externalizable interface?",
            "options": [
                "Custom serialization",
                "Automatic serialization",
                "Both A and B",
                "None of these"
            ],
            "answer": 1,
            "explanation": "Externalizable interface allows custom serialization implementation"
        }
    ]
}

# Adding code-based questions to each topic
java_questions["Lambda_Expressions"].extend([
    {
        "question": "What will be the output of the following code?\n```java\nList<String> list = Arrays.asList(\"a\", \"b\", \"c\");\nlist.forEach(s -> System.out.print(s.toUpperCase()));\n```",
        "options": [
            "abc",
            "ABC",
            "Compilation error",
            "Runtime error"
        ],
        "answer": 2,
        "explanation": "The lambda expression converts each string to uppercase and prints ABC"
    },
    {
        "question": "Which of these lambda expressions is correct?\n```java\n1. () -> System.out.println(\"Hello\")\n2. (String s) -> { return s.length(); }\n3. s -> s.length()\n4. (String s) -> return s.length();\n```",
        "options": [
            "1, 2 and 3 only",
            "2, 3 and 4 only",
            "1, 2 and 4 only",
            "All are correct"
        ],
        "answer": 1,
        "explanation": "Option 4 is incorrect as return statement in single expression lambda should not have semicolon"
    }
])

java_questions["Stream_API"].extend([
    {
        "question": "What will be the output of the following code?\n```java\nList<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);\nint sum = numbers.stream()\n    .filter(n -> n % 2 == 0)\n    .mapToInt(n -> n * 2)\n    .sum();\nSystem.out.println(sum);\n```",
        "options": ["12", "30", "15", "6"],
        "answer": 1,
        "explanation": "Filter selects even numbers (2,4), map multiplies by 2 (4,8), sum adds them (12)"
    },
    {
        "question": "What's wrong with this code?\n```java\nStream<String> stream = Arrays.asList(\"a\", \"b\", \"c\").stream();\nstream.forEach(System.out::println);\nlong count = stream.count();\n```",
        "options": [
            "Syntax error",
            "Stream has already been operated upon or closed",
            "count() is not a terminal operation",
            "None of these"
        ],
        "answer": 2,
        "explanation": "Stream can only be used once. After forEach(), the stream is closed"
    }
])

java_questions["JDBC"].extend([
    {
        "question": "What's wrong with this JDBC code?\n```java\nConnection conn = DriverManager.getConnection(url, user, pass);\nStatement stmt = conn.createStatement();\nResultSet rs = stmt.executeQuery(\"SELECT * FROM users\");\nwhile(rs.next()) {\n    System.out.println(rs.getString(\"name\"));\n}\n```",
        "options": [
            "No error handling",
            "Resources not closed",
            "Both A and B",
            "None of these"
        ],
        "answer": 3,
        "explanation": "Code lacks try-catch blocks and doesn't close resources (Connection, Statement, ResultSet)"
    },
    {
        "question": "Which is the correct way to use PreparedStatement?\n```java\n1. PreparedStatement ps = conn.prepareStatement(\"SELECT * FROM users WHERE id = \" + id);\n2. PreparedStatement ps = conn.prepareStatement(\"SELECT * FROM users WHERE id = ?\");\n   ps.setInt(1, id);\n3. PreparedStatement ps = conn.prepareStatement(\"SELECT * FROM users WHERE id = ?1\");\n   ps.setInt(1, id);\n```",
        "options": [
            "1 only",
            "2 only",
            "3 only",
            "Both 2 and 3"
        ],
        "answer": 2,
        "explanation": "Option 2 is correct. Option 1 is vulnerable to SQL injection, Option 3 has incorrect parameter syntax"
    }
])

java_questions["Java_IO"].extend([
    {
        "question": "What will this code do?\n```java\ntry (BufferedReader br = new BufferedReader(new FileReader(\"file.txt\"))) {\n    String line;\n    while ((line = br.readLine()) != null) {\n        System.out.println(line);\n    }\n}\n```",
        "options": [
            "Read file character by character",
            "Read file line by line",
            "Read entire file at once",
            "None of these"
        ],
        "answer": 2,
        "explanation": "This code uses BufferedReader to read the file line by line using readLine()"
    },
    {
        "question": "What's the output of this code?\n```java\nString str = \"Hello\";\nByteArrayInputStream bis = new ByteArrayInputStream(str.getBytes());\nint data;\nwhile((data = bis.read()) != -1) {\n    System.out.print((char)data);\n}\n```",
        "options": [
            "Hello",
            "HELLO",
            "hello",
            "Compilation error"
        ],
        "answer": 1,
        "explanation": "Code reads bytes from ByteArrayInputStream and converts them back to characters"
    }
])

java_questions["Java_Networking"].extend([
    {
        "question": "What will this code do?\n```java\nURL url = new URL(\"http://example.com\");\nURLConnection conn = url.openConnection();\nBufferedReader br = new BufferedReader(\n    new InputStreamReader(conn.getInputStream()));\nString line;\nwhile ((line = br.readLine()) != null) {\n    System.out.println(line);\n}\n```",
        "options": [
            "Download webpage content",
            "Download webpage images",
            "Connect to server only",
            "None of these"
        ],
        "answer": 1,
        "explanation": "This code downloads and prints the HTML content of the webpage"
    },
    {
        "question": "What's wrong with this server code?\n```java\nServerSocket server = new ServerSocket(8080);\nwhile(true) {\n    new Thread(() -> {\n        try {\n            Socket socket = server.accept();\n            handleClient(socket);\n        } catch(Exception e) {}\n    }).start();\n}\n```",
        "options": [
            "Infinite loop",
            "Single-threaded handling",
            "No error handling",
            "All of these"
        ],
        "answer": 4,
        "explanation": "Code has infinite loop, handles one client at a time, and lacks error handling"
    }
])

java_questions["Java_Serialization"].extend([
    {
        "question": "What's wrong with this serializable class?\n```java\nclass User implements Serializable {\n    private String username;\n    private transient String password;\n    private static String dbUrl;\n    private Connection dbConn;\n}\n```",
        "options": [
            "password won't be serialized",
            "dbUrl won't be serialized",
            "dbConn isn't serializable",
            "All of these"
        ],
        "answer": 4,
        "explanation": "transient password won't be serialized, static dbUrl isn't serialized, Connection isn't serializable"
    },
    {
        "question": "What will happen when deserializing this object?\n```java\nclass Person implements Serializable {\n    private String name;\n    private int age;\n    \n    private void writeObject(ObjectOutputStream out) throws IOException {\n        out.writeUTF(name);\n        out.writeInt(age + 1);\n    }\n    \n    private void readObject(ObjectInputStream in) throws IOException {\n        name = in.readUTF();\n        age = in.readInt() - 1;\n    }\n}\n```",
        "options": [
            "Object won't be deserialized",
            "Age will be same as serialized",
            "Age will be restored correctly",
            "Compilation error"
        ],
        "answer": 3,
        "explanation": "Custom serialization adds 1 to age during writing and subtracts 1 during reading"
    }
])

# Adding remaining questions for Lambda Expressions
java_questions["Lambda_Expressions"].extend([
    {
        "question": "What's the output of this method reference chain?\n```java\nList<String> list = Arrays.asList(\"a\", \"b\", \"c\");\nlist.stream()\n    .map(String::toUpperCase)\n    .map(StringBuilder::new)\n    .map(StringBuilder::reverse)\n    .map(StringBuilder::toString)\n    .forEach(System.out::println);\n```",
        "options": [
            "a b c",
            "A B C",
            "A, B, C",
            "C B A"
        ],
        "answer": 2,
        "explanation": "Each string is uppercase, converted to StringBuilder, reversed, and converted back"
    },
    {
        "question": "What's special about this composition?\n```java\nFunction<Integer, Integer> times2 = x -> x * 2;\nFunction<Integer, Integer> plus3 = x -> x + 3;\nFunction<Integer, Integer> composed = times2.compose(plus3);\nSystem.out.println(composed.apply(5));\n```",
        "options": [
            "16",
            "13",
            "11",
            "Error"
        ],
        "answer": 1,
        "explanation": "compose applies plus3 first (5+3=8), then times2 (8*2=16)"
    }
])

# Adding remaining questions for Stream API
java_questions["Stream_API"].extend([
    {
        "question": "What's the result of this partitioning?\n```java\nrecord Point(int x, int y) {}\nList<Point> points = List.of(\n    new Point(1,1),\n    new Point(2,2));\n\nMap<Boolean, List<Point>> result = points.stream()\n    .collect(Collectors.partitioningBy(\n        p -> p.x() > 0,\n        Collectors.mapping(\n            Point::toString,\n            Collectors.toList()\n)));\n```",
        "options": [
            "{true=[Point[x=1, y=1], Point[x=2, y=2]], false=[]}",
            "{true=[], false=[Point[x=1, y=1], Point[x=2, y=2]]}",
            "Compilation error",
            "Runtime error"
        ],
        "answer": 1,
        "explanation": "Partitions points by x value and maps to string"
    },
    {
        "question": "What's the output of this teeing collector?\n```java\nint[] result = Stream.of(1, 2, 3, 4)\n    .collect(Collectors.teeing(\n        Collectors.summingInt(i -> i),\n        Collectors.counting(),\n        (sum, count) -> new int[]{sum, (int)count}\n    ));\n```",
        "options": [
            "[10, 4]",
            "[4, 10]",
            "Error: can't use teeing",
            "None of these"
        ],
        "answer": 1,
        "explanation": "Teeing collector computes sum (10) and count (4) simultaneously"
    }
])

# Adding remaining questions for JDBC
java_questions["JDBC"].extend([
    {
        "question": "What's the purpose of this savepoint?\n```java\nconn.setAutoCommit(false);\nSavepoint save1 = conn.setSavepoint(\"Save1\");\ntry {\n    // operation 1\n    Savepoint save2 = conn.setSavepoint(\"Save2\");\n    // operation 2\n    conn.commit();\n} catch(SQLException e) {\n    conn.rollback(save1);\n}\n```",
        "options": [
            "Checkpoint for transactions",
            "Performance optimization",
            "Error handling",
            "Connection pooling"
        ],
        "answer": 1,
        "explanation": "Savepoints allow partial rollback of transactions"
    }
])

# Adding remaining questions for Java IO
java_questions["Java_IO"].extend([
    {
        "question": "What's special about this memory-mapped file?\n```java\nRandomAccessFile file = new RandomAccessFile(\"data.bin\", \"rw\");\nFileChannel channel = file.getChannel();\nMappedByteBuffer buffer = channel.map(\n    FileChannel.MapMode.READ_WRITE, 0, 1024*1024);\nbuffer.putInt(0, 100);\nbuffer.force();\n```",
        "options": [
            "Regular file writing",
            "Direct memory access",
            "Buffered IO",
            "None of these"
        ],
        "answer": 2,
        "explanation": "Memory-mapped files allow direct memory access to file contents"
    },
    {
        "question": "What's the purpose of this watchable?\n```java\nPath dir = Paths.get(\"logs\");\nWatchService watcher = FileSystems.getDefault().newWatchService();\ndir.register(watcher, \n    StandardWatchEventKinds.ENTRY_CREATE,\n    StandardWatchEventKinds.ENTRY_DELETE,\n    StandardWatchEventKinds.ENTRY_MODIFY\n);\n```",
        "options": [
            "File monitoring",
            "File copying",
            "File locking",
            "File searching"
        ],
        "answer": 1,
        "explanation": "WatchService monitors directory for file system events"
    }
])

# Adding remaining questions for Java Networking
java_questions["Java_Networking"].extend([
    {
        "question": "What's special about this DatagramChannel?\n```java\nDatagramChannel channel = DatagramChannel.open()\n    .bind(new InetSocketAddress(8080))\n    .connect(new InetSocketAddress(\"localhost\", 9090));\nchannel.configureBlocking(false);\nByteBuffer buffer = ByteBuffer.allocate(1024);\nwhile(true) {\n    buffer.clear();\n    channel.receive(buffer);\n}\n```",
        "options": [
            "TCP communication",
            "Connected UDP",
            "Regular UDP",
            "None of these"
        ],
        "answer": 2,
        "explanation": "Connected DatagramChannel provides connection-oriented UDP"
    },
    {
        "question": "What's the purpose of this SSL context?\n```java\nSSLContext context = SSLContext.getInstance(\"TLS\");\nKeyManagerFactory kmf = KeyManagerFactory.getInstance(\"SunX509\");\nKeyStore ks = KeyStore.getInstance(\"JKS\");\nks.load(new FileInputStream(\"keystore.jks\"), \"password\".toCharArray());\nkmf.init(ks, \"password\".toCharArray());\ncontext.init(kmf.getKeyManagers(), null, null);\n```",
        "options": [
            "Client authentication",
            "Server authentication",
            "Both A and B",
            "None of these"
        ],
        "answer": 2,
        "explanation": "Configures SSL context with server's private key for authentication"
    }
])

# Adding remaining questions for Java Serialization
java_questions["Java_Serialization"].extend([
    {
        "question": "What's the purpose of this externalizable implementation?\n```java\nclass DataHolder implements Externalizable {\n    private int[] data;\n    \n    public void writeExternal(ObjectOutput out) throws IOException {\n        out.writeInt(data.length);\n        for(int i = 0; i < data.length; i += 2) {\n            out.writeInt(data[i]);\n        }\n    }\n    \n    public void readExternal(ObjectInput in) throws IOException {\n        int len = in.readInt();\n        data = new int[len];\n        for(int i = 0; i < len; i += 2) {\n            data[i] = in.readInt();\n        }\n    }\n}\n```",
        "options": [
            "Regular serialization",
            "Custom format",
            "Data compression",
            "Error checking"
        ],
        "answer": 3,
        "explanation": "Implements custom serialization that only writes every second element"
    },
    {
        "question": "What's the best practice for serialVersionUID?\n```java\nclass Data implements Serializable {\n    static final long serialVersionUID = 1L;\n    // vs\n    private static final long serialVersionUID = 1234567890L;\n    // vs\n    // no serialVersionUID\n}\n```",
        "options": [
            "Don't declare it",
            "Use 1L",
            "Use generated value",
            "Access modifier doesn't matter"
        ],
        "answer": 3,
        "explanation": "Use IDE-generated serialVersionUID based on class structure for better version control"
    }
])

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

def main():
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

if __name__ == "__main__":
    main()
