import os
from cs50 import SQL
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Ensure the database file exists
db = SQL("sqlite:///fitness.db")

# Drop existing tables if they exist
db.execute("DROP TABLE IF EXISTS workout_history")
db.execute("DROP TABLE IF EXISTS workout_day_history")
db.execute("DROP TABLE IF EXISTS exercise_genders")
db.execute("DROP TABLE IF EXISTS exercises")
db.execute("DROP TABLE IF EXISTS workouts")
db.execute("DROP TABLE IF EXISTS nutrition")
db.execute("DROP TABLE IF EXISTS programs")
# Create the users table
db.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        hash TEXT NOT NULL,
        gender TEXT,
        age_range TEXT,
        main_goal TEXT,
        current_build TEXT,
        goal_body_type TEXT,
        height NUMERIC,
        weight NUMERIC,
        goal_weight NUMERIC
    );
''')

# Create the workouts table
db.execute('''
    CREATE TABLE IF NOT EXISTS workouts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        date TEXT,
        workout TEXT,
        duration INTEGER,
        calories_burned INTEGER,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    );
''')

# Create the nutrition table
db.execute('''
    CREATE TABLE IF NOT EXISTS nutrition (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        date TEXT,
        food_item TEXT,
        calories INTEGER,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    );
''')

# RapidAPI credentials
EXERCISE_API_HOST = "exercisedb.p.rapidapi.com"
EXERCISE_API_KEY = os.getenv("EXERCISE_API_KEY")

# Connect to the SQLite database
db = SQL("sqlite:///fitness.db")

# Create the exercises table with appropriate fields
# Create the exercises table
db.execute('''
CREATE TABLE IF NOT EXISTS exercises (
    id TEXT PRIMARY KEY,
    name TEXT,
    body_part TEXT,
    equipment TEXT,
    target TEXT,
    secondary_muscles TEXT,
    instructions TEXT,
    gif_path TEXT,
    day INTEGER
)
''')

# Create the exercise_genders table
db.execute('''
    CREATE TABLE IF NOT EXISTS exercise_genders (
        exercise_id TEXT,
        gender TEXT,
        day INTEGER,
        order_index INTEGER,
        FOREIGN KEY (exercise_id) REFERENCES exercises(id),
        PRIMARY KEY (exercise_id, gender, day)
    );
''')

# Fetch exercises from RapidAPI
url = "https://exercisedb.p.rapidapi.com/exercises"
headers = {
    'x-rapidapi-key': EXERCISE_API_KEY,
    'x-rapidapi-host': EXERCISE_API_HOST
}
params = {
    'limit': 0  # This will remove the limit and fetch all available data
}

response = requests.get(url, headers=headers, params=params)

# Exercise plans for males
exercise_push = ['barbell bench press', 'dumbbell incline bench press', 'cable standing up straight crossovers',
                 'barbell standing wide military press', 'dumbbell lateral raise', 'barbell lying triceps extension '
                                                                                   'skull crusher', 'cable triceps '
                                                                                                    'pushdown (v-bar)']
exercise_pull = ['cable straight back seated row', 'cable bar lateral pulldown', 'barbell bent over row',
                 'hyperextension', 'ez-barbell standing wide grip biceps curl', 'dumbbell seated hammer curl']
exercise_leg_core = ['barbell full squat (back pov)', 'dumbbell single leg split squat', 'barbell straight leg deadlift', 'sled 45в° leg press',
                     'lever leg extension', 'lever lying two-one leg curl',
                     'dumbbell standing calf raise', 'weighted front plank', 'cross body crunch']
exercise_full_body = ['barbell incline bench press', 'chest dip (on dip-pull-up cage)', 'pull-up',
                      'barbell reverse grip bent over row',
                      'dumbbell seated shoulder press', 'dumbbell reverse fly', 'barbell romanian deadlift',
                      'dumbbell biceps curl', 'cable overhead triceps extension (rope attachment)',
                      'hanging straight leg raise']
exercise_lower_body = ['barbell clean-grip front squat', 'dumbbell goblet squat', 'sled 45в° leg press (back pov)',
                       'barbell one leg squat', 'lever seated leg curl', 'sled calf press on leg press',
                       'otis up']

# Exercise plans for females
exercise_lower_body_female = ['barbell full squat (back pov)', 'barbell lying lifting (on hip)', 'sled 45в° leg press','cable hip adduction', 'dumbbell single leg split squat','lever seated hip abduction']
exercise_upper_body_female = ['assisted pull-up','lever shoulder press v. 3', 'dumbbell reverse grip row (female)','cable bar lateral pulldown', 'dumbbell lateral raise','barbell biceps curl (with arm blaster)', 'cable triceps pushdown (v-bar)']
exercise_lower_core_female = ['barbell deadlift','dumbbell lunge','dumbbell goblet squat','dumbbell romanian deadlift','lever seated leg curl', 'cable standing hip extension','dumbbell standing calf raise', 'hip raise (bent knee)','russian twist']
exercise_core_cardio_female = ['air bike', 'twisted leg raise (female)', 'incline twisting sit-up', 'bodyweight incline side plank','bridge - mountain climber (cross body)','astride jumps (male)','run (equipment)']
exercise_full_body_female = ['barbell glute bridge','barbell sumo deadlift', 'cable pull through (with rope)', 'dumbbell single leg deadlift','band bent-over hip extension','lever hip extension v. 2','lever seated hip adduction','3/4 sit-up']

if response.status_code == 200:
    exercise_data = response.json()

    # Insert data into the exercises table
    for exercise in exercise_data:
        exercise_name = exercise.get('name', '')
        exercise_id = exercise.get('id', '')

        # Check if exercise is already in the table
        existing_exercise = db.execute("SELECT * FROM exercises WHERE id = ?", exercise_id)
        if not existing_exercise:
            db.execute('''
            INSERT INTO exercises (id, name, body_part, equipment, target, secondary_muscles, instructions, gif_path)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', exercise_id,
                       exercise_name,
                       exercise.get('bodyPart', ''),
                       exercise.get('equipment', ''),
                       exercise.get('target', ''),
                       ', '.join(exercise.get('secondaryMuscles', [])),  # Join list into a comma-separated string
                       ' '.join(exercise.get('instructions', [])),  # Join list into a space-separated string
                       exercise.get('gifUrl', '')
                       )

        # Insert into exercise_genders table based on gender and day
        if exercise_name in exercise_push:
            db.execute('INSERT OR IGNORE INTO exercise_genders (exercise_id, gender, day) VALUES (?, ?, ?)',
                       exercise_id, 'male', 1)
        if exercise_name in exercise_pull:
            db.execute('INSERT OR IGNORE INTO exercise_genders (exercise_id, gender, day) VALUES (?, ?, ?)',
                       exercise_id, 'male', 2)
        if exercise_name in exercise_leg_core:
            db.execute('INSERT OR IGNORE INTO exercise_genders (exercise_id, gender, day) VALUES (?, ?, ?)',
                       exercise_id, 'male', 3)
        if exercise_name in exercise_full_body:
            db.execute('INSERT OR IGNORE INTO exercise_genders (exercise_id, gender, day) VALUES (?, ?, ?)',
                       exercise_id, 'male', 4)
        if exercise_name in exercise_lower_body:
            db.execute('INSERT OR IGNORE INTO exercise_genders (exercise_id, gender, day) VALUES (?, ?, ?)',
                       exercise_id, 'male', 5)

        if exercise_name in exercise_lower_body_female:
            db.execute('INSERT OR IGNORE INTO exercise_genders (exercise_id, gender, day) VALUES (?, ?, ?)',
                       exercise_id, 'female', 1)
        if exercise_name in exercise_upper_body_female:
            db.execute('INSERT OR IGNORE INTO exercise_genders (exercise_id, gender, day) VALUES (?, ?, ?)',
                       exercise_id, 'female', 2)
        if exercise_name in exercise_lower_core_female:
            db.execute('INSERT OR IGNORE INTO exercise_genders (exercise_id, gender, day) VALUES (?, ?, ?)',
                       exercise_id, 'female', 3)
        if exercise_name in exercise_core_cardio_female:
            db.execute('INSERT OR IGNORE INTO exercise_genders (exercise_id, gender, day) VALUES (?, ?, ?)',
                       exercise_id, 'female', 4)
        if exercise_name in exercise_full_body_female:
            db.execute('INSERT OR IGNORE INTO exercise_genders (exercise_id, gender, day) VALUES (?, ?, ?)',
                       exercise_id, 'female', 5)

else:
    print(f"Error fetching exercises: {response.status_code} {response.text}")


# Execute each statement separately
db.execute('CREATE INDEX idx_exercises_name ON exercises(name);')
db.execute('CREATE INDEX idx_exercises_body_part ON exercises(body_part);')
db.execute('CREATE INDEX idx_exercises_target ON exercises(target);')
db.execute('CREATE INDEX idx_exercises_equipment ON exercises(equipment);')
db.execute('CREATE INDEX idx_exercises_secondary_muscles ON exercises(secondary_muscles);')

# Create the programs table
db.execute('''
    CREATE TABLE IF NOT EXISTS programs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE,
        days INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id)
    );
''')

# Create the updated workout_history table
db.execute('''
    CREATE TABLE IF NOT EXISTS workout_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        exercise_id TEXT,
        day INTEGER,
        total_workout_time INTEGER,
        completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(exercise_id) REFERENCES exercises(id)
    );
''')

# Create the workout_day_history table
db.execute('''
    CREATE TABLE IF NOT EXISTS workout_day_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        day INTEGER,
        program INTEGER,
        total_workout_time INTEGER,
        completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    );
''')
