from datetime import datetime
from time import sleep
import os
from functools import wraps
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, session, redirect, url_for, flash, abort
import pandas as pd
from dotenv import load_dotenv
from flask import Response
# Load environment variables
load_dotenv(override=True)

# Debug print to verify environment variables are loaded
print("Environment variables loaded:")
print(f"ADMIN_USERNAME: {os.getenv('ADMIN_USERNAME')}")
print(f"ADMIN_PASSWORD: {os.getenv('ADMIN_PASSWORD')}")

app = Flask(__name__, 
    template_folder='templates',
    static_folder='static')
app.secret_key = os.getenv('SECRET_KEY', 'default-dev-key')  # Use environment variable
UPLOAD_FOLDER = "papers"
ALLOWED_EXTENSIONS = {'xlsx', 'xls'}

# Security: Admin credentials (should be moved to env variables in production)
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin123')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_logged_in'):
            flash('Please log in as admin first.')
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function

def handle_file_operation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            flash('Required file not found.')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'An error occurred: {str(e)}')
            return redirect(url_for('index'))
    return wrapper

@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        input_username = request.form.get('username')
        input_password = request.form.get('password')
        
        # Debug print to check environment variables
        print(f"Expected username: {os.getenv('ADMIN_USERNAME')}")
        print(f"Expected password: {os.getenv('ADMIN_PASSWORD')}")
        print(f"Input username: {input_username}")
        print(f"Input password: {input_password}")
        
        if (input_username == os.getenv('ADMIN_USERNAME') and 
            input_password == os.getenv('ADMIN_PASSWORD')):
            session['admin_logged_in'] = True
            flash('Successfully logged in!')
            return redirect(url_for('admin'))
        flash('Invalid credentials')
    return render_template("admin_login.html")

@app.route("/logs", methods=["GET", "POST"])
def logs():
    f = open('logs/logs.txt', 'r')
    return f.read().splitlines()

@app.route("/admin_result", methods=["GET", "POST"])
def admin_result():
    try:
        with open('results/result.txt', 'r') as f:
            content = f.read()
            # Return the content as plain text with formatting preserved
            return Response(content, mimetype='text/plain')
    except FileNotFoundError:
        return {"error": "File not found"}, 404

@app.route("/admin", methods=["GET", "POST"])
@admin_required
def admin():
    if request.method == "POST":
        if 'questions_file' not in request.files:
            flash('No file uploaded')
            return redirect(request.url)
            
        questions_file = request.files["questions_file"]
        if questions_file.filename == '':
            flash('No file selected')
            return redirect(request.url)
            
        if not allowed_file(questions_file.filename):
            flash('Invalid file type. Only Excel files are allowed.')
            return redirect(request.url)
            
        try:
            filename = secure_filename(questions_file.filename)
            questions_file.save(os.path.join(UPLOAD_FOLDER, filename))
            description = request.form.get("description", "").strip()
            
            with open(f"papers/papers.txt", "a+") as file:
                file.write(f"\n{filename},{description}")
                
            flash('File uploaded successfully!')
        except Exception as e:
            flash(f'Error uploading file: {str(e)}')
            
        return redirect(url_for("admin"))

    return render_template("admin.html")

def populate(test_type):
    try:
        excel_path = "papers"
        excel_filename = os.path.join(excel_path, test_type)
        print(f"Loading excel file: {excel_filename}")
        
        if not os.path.exists(excel_filename):
            print(f"Excel file not found: {excel_filename}")
            return []
            
        df = pd.read_excel(excel_filename)
        print(f"Excel loaded successfully. Found {len(df)} questions")
        
        def clean_answer(answer):
            if pd.isna(answer):
                return 1  # Default to first option if no answer
            # Convert to string and clean
            answer_str = str(answer).strip()
            # If multiple answers (comma-separated), take the first one
            if ',' in answer_str:
                answer_str = answer_str.split(',')[0]
            # Remove any non-digit characters
            answer_str = ''.join(c for c in answer_str if c.isdigit())
            # Convert to int, default to 1 if invalid
            try:
                return int(answer_str)
            except (ValueError, TypeError):
                return 1
        
        questions = []
        for i in range(len(df)):
            try:
                question = {}
                # Convert numpy types to Python native types
                question["id"] = int(df.iloc[i]["id"])
                question["text"] = str(df.iloc[i]["text"])
                question["options"] = [
                    str(df.iloc[i]["option1"]),
                    str(df.iloc[i]["option2"]),
                    str(df.iloc[i]["option3"]),
                    str(df.iloc[i]["option4"])
                ]
                question["answer"] = clean_answer(df.iloc[i]["answer"])
                questions.append(question)
            except Exception as e:
                print(f"Error processing question {i+1}: {str(e)}")
                continue
        
        print(f"Processed {len(questions)} questions")
        return questions
    except Exception as e:
        print(f"Error in populate function: {str(e)}")
        raise

@app.route("/")
def index():
    filedata = []
    temp = []
    with open('papers/papers.txt', 'r') as f:
        for line in f:
            # filename, desc = line.strip().split(',')
            temp = line.strip().split(',')
            if len(temp) == 2:
                filename = temp[0]
                desc = temp[1]
                filedata.append({'filename': filename, 'desc': desc})
    return render_template("index.html", filedata=filedata)

@app.route("/result", methods=["GET", "POST"])
def result():
    score = 0
    return render_template("result.html", score=score)

def log_test_results(username, test_type, total_correct, total_wrong, total_unanswered, score):
    try:
        current_datetime = datetime.now()
        test_type = test_type.split('.')[0]
        
        with open("logs/logs.txt", "a+") as file:
            file.write(
                f"\n\n\nName: {username}\n"
                f"Test Type: {test_type}\n"
                f"Total Correct: {total_correct}\n"
                f"Total Incorrect: {total_wrong}\n"
                f"Total Unanswered: {total_unanswered}\n"
                f"Final Score: {score}\n"
                f"Date/Time: {current_datetime}"
            )
    except Exception as e:
        app.logger.error(f"Error logging test results: {str(e)}")

@app.route("/test", methods=["GET", "POST"])
@handle_file_operation
def test():
    if request.method == "GET":
        username = request.args.get('username', '').strip()
        test_type = request.args.get('questionpaper', '').strip()
        
        # Validate inputs
        if not username:
            flash('Please enter your name')
            return redirect(url_for('index'))
            
        if not test_type:
            flash('Please select a test paper')
            return redirect(url_for('index'))
            
        try:
            # Verify if the test file exists
            test_path = os.path.join(UPLOAD_FOLDER, test_type)
            if not os.path.exists(test_path):
                flash('Selected test paper not found')
                return redirect(url_for('index'))
                
            session["username"] = username
            session["test_type"] = test_type
            questions = populate(test_type)
            
            if not questions:
                flash('No questions found in the selected test paper')
                return redirect(url_for('index'))
                
            return render_template("test.html", questions=questions)
            
        except Exception as e:
            flash(f'Error loading test: {str(e)}')
            return redirect(url_for('index'))

    if request.method == "POST":
        score = 0
        total_unanswered = 0
        total_correct = 0
        total_wrong = 0
        
        try:
            test_type = session.get("test_type")
            if not test_type:
                raise ValueError("Test type not found in session")
                
            questions = populate(test_type)
            for question in questions:
                if str(question["id"]) in request.form:
                    selected_answer = request.form[str(question["id"])]
                    if selected_answer == str(question["answer"]):
                        total_correct += 1
                    else:
                        total_wrong += 1
                    question["selected_answer"] = int(selected_answer)
                else:
                    question["selected_answer"] = None
                    total_unanswered += 1
                    
            total_questions = len(questions)
            score = total_correct
            print(f"Scores calculated - Correct: {total_correct}, Wrong: {total_wrong}, Unanswered: {total_unanswered}")
            
            # Log results
            log_test_results(
                session.get("username"),
                test_type,
                total_correct,
                total_wrong,
                total_unanswered,
                score
            )
            
            return render_template(
                "result.html",
                score=score,
                questions=questions,
                total_questions=total_questions,
                total_correct=total_correct,
                total_wrong=total_wrong,
                total_unanswered=total_unanswered
            )
            
        except Exception as e:
            flash(f'An error occurred during test submission: {str(e)}')
            return redirect(url_for('index'))

@app.route("/revision", methods=["GET", "POST"])
def revision():
    if request.method == "GET":
        filedata = []
        temp = []
        with open('papers/papers.txt', 'r') as f:
            for line in f:
                # filename, desc = line.strip().split(',')
                temp = line.strip().split(',')
                if len(temp) == 2:
                    filename = temp[0]
                    desc = temp[1]
                    filedata.append({'filename': filename, 'desc': desc})
        return render_template("revisionsearch.html", filedata=filedata)
    if request.method == "POST":
        test_type = request.form['questionpaper']
        print("paer selected: " + test_type)
        questions = populate(test_type)
        return render_template("revision.html", questions=questions)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.route('/start_test', methods=['POST'])
def start_test():
    try:
        username = request.form.get('username')
        test_type = request.form.get('test_type')
        
        print(f"\n=== Starting test for {username} ===")
        print(f"Test type: {test_type}")
        
        # Load questions from Excel
        questions = populate(test_type)
        print(f"Loaded {len(questions)} questions")
        
        # Store in session
        session['username'] = username
        session['test_type'] = test_type
        session['questions'] = questions
        print("Stored in session:", dict(session))
        
        return render_template('test.html', questions=questions)
    except Exception as e:
        print(f"Error starting test: {str(e)}")
        import traceback
        print(traceback.format_exc())
        flash('Error starting test. Please try again.')
        return redirect(url_for('index'))

@app.route('/submit_test', methods=['POST'])
def submit_test():
    print("\n=== Starting submit_test function ===")
    print("Request method:", request.method)
    print("Form data:", dict(request.form))
    print("\nSession data:")
    print("All session data:", dict(session))
    
    try:
        print("\nProcessing form data...")
        answers = {}
        for key, value in request.form.items():
            if key.isdigit():
                answers[int(key)] = int(value)
        print(f"Processed answers: {answers}")
        
        print("\nGetting session data...")
        questions = session.get('questions', [])
        username = session.get('username', 'Anonymous')
        test_type = session.get('test_type', 'Unknown')
        
        print(f"Username from session: {username}")
        print(f"Test type from session: {test_type}")
        print(f"Number of questions from session: {len(questions)}")
        
        if not questions:
            print("WARNING: No questions found in session! Attempting to reload...")
            # Try to reload questions
            if test_type != 'Unknown':
                questions = populate(test_type)
                print(f"Reloaded {len(questions)} questions")
        
        if questions:
            print("First question sample:", questions[0])
        else:
            print("WARNING: Still no questions after reload attempt!")
        
        print("\nCalculating scores...")
        total_correct = 0
        total_wrong = 0
        total_unanswered = 0
        
        if not questions:
            print("ERROR: No questions to grade!")
            flash('Error: No questions found. Please try starting the test again.')
            return redirect(url_for('index'))
            
        # Process answers
        for q in questions:
            print(f"\nProcessing question {q['id']}:")
            selected_answer = answers.get(q['id'])
            print(f"Selected answer: {selected_answer}")
            print(f"Correct answer: {q['answer']}")
            
            q['selected_answer'] = selected_answer
            if selected_answer is None:
                total_unanswered += 1
                print("Status: Unanswered")
            elif selected_answer == q['answer']:
                total_correct += 1
                print("Status: Correct")
            else:
                total_wrong += 1
                print("Status: Incorrect")
        
        score = total_correct
        print(f"\nFinal scores:")
        print(f"Total correct: {total_correct}")
        print(f"Total wrong: {total_wrong}")
        print(f"Total unanswered: {total_unanswered}")
        print(f"Final score: {score}")
        
        # Save result to file
        print("\n=== Starting to save results ===")
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            result_file = os.path.join(base_dir, 'results', 'result.txt')
            
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            result_entry = f"\n{'='*50}\n"
            result_entry += f"Date: {timestamp}\n"
            result_entry += f"Username: {username}\n"
            result_entry += f"Test Type: {test_type}\n"
            result_entry += f"Total Questions: {len(questions)}\n"
            result_entry += f"Correct Answers: {total_correct}\n"
            result_entry += f"Incorrect Answers: {total_wrong}\n"
            result_entry += f"Unanswered Questions: {total_unanswered}\n"
            result_entry += f"Final Score: {score}/{len(questions)}\n"
            result_entry += f"{'='*50}\n"
            
            with open(result_file, 'a', encoding='utf-8') as f:
                f.write(result_entry)
            
            print("=== Result saved successfully ===\n")
            
        except Exception as e:
            print(f"\nERROR saving result: {str(e)}")
            import traceback
            print(traceback.format_exc())
        
        return render_template('result.html',
                             questions=questions,
                             total_correct=total_correct,
                             total_wrong=total_wrong,
                             total_unanswered=total_unanswered,
                             score=score,
                             total_questions=len(questions))
                             
    except Exception as e:
        print(f"\nERROR in submit_test: {str(e)}")
        import traceback
        print(traceback.format_exc())
        raise

@app.route('/view_results')
def view_results():
    if not session.get('admin_logged_in'):
        flash('Please log in as admin first.')
        return redirect(url_for('admin_login'))
        
    try:
        # Get path to results file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        result_file = os.path.join(base_dir, 'results', 'result.txt')
        
        # Check if file exists
        if not os.path.exists(result_file):
            return render_template('view_results.html', results=[], error="No results found.")
            
        # Read results from file
        with open(result_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Split content into individual results
        result_blocks = content.strip().split('='*50)
        results = []
        
        for block in result_blocks:
            if not block.strip():
                continue
                
            # Parse each result block
            lines = block.strip().split('\n')
            result = {}
            
            for line in lines:
                if ':' in line:
                    key, value = line.split(':', 1)
                    result[key.strip()] = value.strip()
                    
            if result:  # Only add if we parsed some data
                results.append(result)
                
        # Sort results by date in reverse order (newest first)
        results.sort(key=lambda x: x.get('Date', ''), reverse=True)
        
        return render_template('view_results.html', results=results)
        
    except Exception as e:
        print(f"Error reading results: {str(e)}")
        import traceback
        print(traceback.format_exc())
        return render_template('view_results.html', results=[], error=str(e))

if __name__ == "__main__":
    # Ensure required directories exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs('logs', exist_ok=True)
    
    # Create papers.txt if it doesn't exist
    if not os.path.exists('papers/papers.txt'):
        open('papers/papers.txt', 'a').close()
        
    app.run(debug=False)  # Set debug=False in production
