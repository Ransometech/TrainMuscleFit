import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required
from dotenv import load_dotenv
import requests
import time  # Add this line

# Load environment variables from .env file
load_dotenv()
load_dotenv()

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
# Use the absolute path to the database file
db_path = os.path.join(os.path.dirname(__file__), 'fitness.db')
db = SQL(f"sqlite:///{db_path}")

EXERCISE_API_HOST = "exercisedb.p.rapidapi.com"
EXERCISE_API_KEY = os.getenv("EXERCISE_API_KEY")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    return redirect(url_for("home"))


@app.route("/home")
@login_required
def home():
    user_id = session["user_id"]
    # Fetch the user's name from the database
    user = db.execute("SELECT username FROM users WHERE id = ?", user_id)
    # Ensure user is found
    if user:
        user_name = user[0]["username"]
    else:
        user_name = "User"

    return render_template('home.html', user_name=user_name)



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    session.clear()
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username", 403)
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        session["user_id"] = rows[0]["id"]
        flash('Logged in!')
        return redirect("/")
    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear()
    if request.method == "POST":
        # Collect form data
        gender = request.form.get("gender")
        age_range = request.form.get("age_range")
        main_goal = request.form.get("main_goal")
        current_build = request.form.get("current_build")
        goal_body_type = request.form.get("goal_body_type")
        height = request.form.get("height")
        weight = request.form.get("weight")
        goal_weight = request.form.get("goal_weight")
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure form data is valid
        if not username or not password or password != confirmation:
            return render_template("register.html", error="Invalid registration details")

        # Check if username already exists
        check_username = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(check_username) != 0:
            return render_template("register.html", error="Username already exists")

        # Hash the password using pbkdf2:sha256
        hash_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Insert new user into the database
        db.execute(
            "INSERT INTO users (username, hash, gender, age_range, main_goal, current_build, goal_body_type, height, weight, goal_weight) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            username, hash_password, gender, age_range, main_goal, current_build, goal_body_type, height, weight,
            goal_weight
        )

        # Retrieve the new user's ID and log them in
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        session["user_id"] = rows[0]["id"]

        # Flash success message and redirect to home page
        flash('Registered successfully! Enjoy the benefits of consistent workouts.')
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


NUTRITIONIX_APP_ID = os.getenv('NUTRITIONIX_APP_ID')
NUTRITIONIX_API_KEY = os.getenv('NUTRITIONIX_API_KEY')


@app.route("/nutrition", methods=["GET", "POST"])
@login_required
def nutrition():
    if request.method == "POST":
        food_item = request.form.get("food_item")
        if food_item:
            url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
            headers = {
                "x-app-id": NUTRITIONIX_APP_ID,
                "x-app-key": NUTRITIONIX_API_KEY,
                "Content-Type": "application/json"
            }
            data = {
                "query": food_item
            }
            response = requests.post(url, json=data, headers=headers)
            if response.status_code == 200:
                nutrition_data = response.json()
                return render_template("nutrition.html", nutrition_data=nutrition_data)
            else:
                flash("Unable to fetch data")

    return render_template("nutrition.html")


@app.route("/workout")
@login_required
def workout():
    # Get query parameters for search and filters
    search_query = request.args.get('search', '')
    body_part = request.args.get('body_part', '')
    target = request.args.get('target', '')
    equipment = request.args.get('equipment', '')
    offset = int(request.args.get('offset', 0))
    limit = 10  # Default limit

    # Base query
    query = "SELECT * FROM exercises WHERE 1=1"
    params = []

    # Add search and filter conditions
    if search_query:
        query += " AND name LIKE ?"
        params.append(f"%{search_query}%")

    if body_part:
        query += " AND body_part = ?"
        params.append(body_part)

    if target:
        query += " AND target = ?"
        params.append(target)

    if equipment:
        query += " AND equipment = ?"
        params.append(equipment)

    # Add offset and limit for pagination
    query += " LIMIT ? OFFSET ?"
    params.extend([limit, offset])

    # Execute query
    exercises = db.execute(query, *params)

    # Get distinct values for filters
    body_parts = db.execute("SELECT DISTINCT body_part FROM exercises")
    targets = db.execute("SELECT DISTINCT target FROM exercises")
    equipments = db.execute("SELECT DISTINCT equipment FROM exercises")

    # Construct return_url for navigation
    return_url = url_for('workout', search=search_query, body_part=body_part, target=target, equipment=equipment,
                         offset=offset, _external=False)

    return render_template("workout.html", exercises=exercises, body_parts=body_parts, targets=targets,
                           equipments=equipments, return_url=return_url, limit=limit)


@app.route("/load_more_exercises")
@login_required
def load_more_exercises():
    search_query = request.args.get('search', '')
    body_part = request.args.get('body_part', '')
    target = request.args.get('target', '')
    equipment = request.args.get('equipment', '')
    offset = int(request.args.get('offset', 0))
    limit = 10  # Same as in the workout route

    # Base query
    query = "SELECT * FROM exercises WHERE 1=1"
    params = []

    # Add search and filter conditions
    if search_query:
        query += " AND name LIKE ?"
        params.append(f"%{search_query}%")

    if body_part:
        query += " AND body_part = ?"
        params.append(body_part)

    if target:
        query += " AND target = ?"
        params.append(target)

    if equipment:
        query += " AND equipment = ?"
        params.append(equipment)

    # Add offset and limit for pagination
    query += " LIMIT ? OFFSET ?"
    params.extend([limit, offset])

    # Execute query
    exercises = db.execute(query, *params)

    # Render the exercises part only
    return render_template("partials/exercises_list.html", exercises=exercises)


@app.route("/view_exercise/<string:id>")
@login_required
def view_exercise(id):
    # Fetch the exercise from the database
    exercise = db.execute("SELECT * FROM exercises WHERE id = ?", id)

    if not exercise:
        flash("Exercise not found")
        return redirect(url_for("workout"))

    return_url = request.args.get('return_url', url_for('workout'))
    return render_template("exercise_detail.html", exercise=exercise[0], return_url=return_url)

@app.route("/history")
@login_required
def history():
    """Show history of workouts"""
    user_id = session.get("user_id")
    workouts = db.execute(
        """
        SELECT workout_history.*, exercises.name
        FROM workout_history
        JOIN exercises ON exercises.id = workout_history.exercise_id
        WHERE workout_history.user_id = ?
        ORDER BY workout_history.completed_at DESC LIMIT 30
        """,
        user_id
    )

    workout_days = db.execute("SELECT * FROM workout_day_history WHERE user_id = ? ORDER BY completed_at DESC LIMIT 30", user_id)
    return render_template("history.html", workouts=workouts,workout_days=workout_days)


@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    """Change user password"""
    user_id = session["user_id"]
    if request.method == "POST":
        password = request.form.get("password")
        new_password = request.form.get("new_password")
        confirm_password = request.form.get("confirm_password")
        if not password:
            return apology("must provide password", 403)
        elif not new_password:
            return apology("must provide new password", 403)
        elif not confirm_password:
            return apology("must confirm new password", 403)

        rows = db.execute("SELECT * FROM users WHERE id = ?", user_id)
        if not check_password_hash(rows[0]["hash"], password):
            return apology("invalid password", 403)
        if new_password != confirm_password:
            return apology("passwords do not match", 403)

        new_hash = generate_password_hash(new_password, method='pbkdf2:sha256')
        db.execute("UPDATE users SET hash = ? WHERE id = ?", new_hash, user_id)

        flash('Password changed!')
        return redirect("/")
    else:
        return render_template("change_password.html")


@app.route("/myplan")
@login_required
def myplan():
    user_id = session.get("user_id")
    plans = db.execute("SELECT * FROM programs WHERE user_id = ?", user_id)
    return render_template("myplan.html", plans=plans)


@app.route("/program/<int:days>")
@login_required
def program(days):
    user_id = session.get("user_id")
    return render_template("program.html", days=days)


@app.route("/workout_day/<int:day>")
@login_required
def workout_day(day):
    user_id = session.get("user_id")

    # Get the gender of the user
    user = db.execute("SELECT gender FROM users WHERE id = ?", user_id)
    if not user:
        flash("User not found")
        return redirect(url_for("home"))

    gender = user[0]["gender"]

    # Fetch workouts for the day based on user's gender
    workouts = db.execute('''
            SELECT exercises.*, exercise_genders.order_index FROM exercises
            JOIN exercise_genders ON exercises.id = exercise_genders.exercise_id
            WHERE exercise_genders.day = ? AND exercise_genders.gender = ?
            ORDER BY exercises.body_part, exercise_genders.exercise_id
        ''', day, gender)

    if not workouts:
        flash("No workouts found for the day")
        return redirect(url_for("home"))

    # Assign order_index to each workout and update the database
    for index_order, workout_order in enumerate(workouts):
        db.execute(
            '''
            UPDATE exercise_genders
            SET order_index = ?
            WHERE exercise_id = ? AND gender = ? AND day = ?
            ''',
            index_order, workout_order['id'], gender, day
        )

    #print(db.execute("SELECT * FROM exercise_genders WHERE exercise_genders.day = ? AND exercise_genders.gender = 'male'", day))
    from_plan = request.args.get('from_plan', 'False') == 'True'
    show_timer = from_plan
    total_time = int(time.time() - session.get('general_workout_start_time', time.time())) if show_timer else 0

    return render_template("workout_day.html", day=day, workouts=workouts, show_timer=show_timer, total_time=total_time)


@app.route("/exercise/<string:id>/<int:day>")
@login_required
def exercise(id, day):
    exercise = db.execute("SELECT * FROM exercises WHERE id = ?", id)
    if len(exercise) == 0:
        flash("Exercise not found")
        return redirect(url_for("home"))

    # Fetch from_plan parameter from request args
    from_plan = request.args.get('from_plan', 'False') == 'True'

    return render_template("exercise_detail.html", exercise=exercise[0], day=day, from_plan=from_plan)


@app.route("/select_program/<int:days>", methods=["POST"])
@login_required
def select_program(days):
    user_id = session.get("user_id")
    existing_program = db.execute("SELECT * FROM programs WHERE user_id = ?", user_id)
    if existing_program:
        db.execute("UPDATE programs SET days = ? WHERE user_id = ?", days, user_id)
    else:
        db.execute("INSERT INTO programs (user_id, days) VALUES (?, ?)", user_id, days)
    session['selected_program'] = days  # Store the selected program in the session
    flash('Program selected!')
    return redirect(url_for("myplan"))


@app.route("/start_program_day/<int:day>", methods=["POST"])
@login_required
def start_program_day(day):
    user_id = session.get("user_id")
    if 'workout_start_time' not in session:
        session['workout_start_time'] = time.time()
        session['general_workout_start_time'] = time.time()
    session['current_day'] = day  # Store the current day in the session
    session['current_program'] = session.get('selected_program', 1)  # Store the current program in the session
    return redirect(url_for("workout_day", day=day, from_plan=True))


@app.route("/start_workout/<string:exercise_id>/<int:day>")
@login_required
def start_workout(exercise_id, day):
    user_id = session.get("user_id")
    exercise = db.execute("SELECT * FROM exercises WHERE id = ?", exercise_id)
    if not exercise:
        flash("Exercise not found")
        return redirect(url_for("workout_day", day=day, from_plan=True))
    if 'workout_start_time' not in session:
        session['workout_start_time'] = time.time()
    total_time = int(time.time() - session.get('general_workout_start_time', time.time()))
    return render_template("workout_execution.html", workout=exercise[0], day=day, total_time=total_time)


@app.route("/complete_workout/<string:exercise_id>", methods=["POST"])
@login_required
def complete_workout(exercise_id):
    user_id = session.get("user_id")
    total_time = request.form.get('total_time', 0, type=int)
    session['total_time'] = total_time  # Save total time to session
    user = db.execute("SELECT gender FROM users WHERE id = ?", user_id)
    if not user:
        flash("User not found")
        return redirect(url_for("home"))

    gender = user[0]["gender"]
    current_exercise = db.execute(
        "SELECT exercise_genders.* FROM exercise_genders WHERE exercise_id = ? AND gender = ?",
        exercise_id, gender)[0]
    day = current_exercise['day']
    print("day", day)

    db.execute(
        "INSERT INTO workout_history (user_id, exercise_id, day, total_workout_time, completed_at) VALUES (?, ?, ?, ?, datetime('now'))",
        user_id, exercise_id, day, total_time or 0)  # Ensure total_time is not None

    # Fetch the next exercise based on day and current exercise order
    next_exercise = db.execute(
        """
        SELECT *
        FROM exercise_genders
        WHERE day = ? AND gender = ?
        AND order_index = (
            SELECT order_index + 1
            FROM exercise_genders
            WHERE exercise_id = ? AND day = ? AND gender = ?
        )
        LIMIT 1
        """,
        day, gender, exercise_id, day, gender
    )

    if next_exercise:
        return redirect(url_for("start_workout", exercise_id=next_exercise[0]['exercise_id'], day=day))
    else:
        flash('All exercises for the day completed! You can end the workout or continue with other exercises.')
        return redirect(url_for("workout_day", day=day, from_plan=True))
    print(next_exercise)


@app.route("/end_all_workout", methods=["POST"])
@login_required
def end_all_workout():
    total_time = int(request.form.get('total_time', 0))
    user_id = session.get("user_id")
    current_day = session.get('current_day', 1)
    current_program = session.get('current_program', 1)
    session.pop('workout_start_time', None)
    session.pop('general_workout_start_time', None)
    session.pop('total_time', None)  # Reset the total time
    db.execute(
        "INSERT INTO workout_day_history (user_id, day, program, total_workout_time, completed_at) VALUES (?, ?, ?, ?, datetime('now'))",
        user_id, current_day, current_program, total_time)
    flash(f'All workouts ended! Total workout time: {total_time // 60} minutes and {total_time % 60} seconds.')
    return redirect(url_for("myplan"))


if __name__ == '__main__':
    app.run(debug=True)
