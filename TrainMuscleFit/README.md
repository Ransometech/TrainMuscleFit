# TrainMuscleFit

#### Video Demo:  https://youtu.be/RbDf-cVlp0o

#### Description:

TrainMuscleFit is a fitness and nutrition web app designed to help users reach their fitness goals through structured workout plans and nutrition tracking. Users can register, select workout programs, track exercise history, and explore nutritional information for various foods. Built with Flask and SQLite, the app integrates ExerciseDB and Nutritionix APIs to provide extensive data on exercises and nutrition.

### Features

1. **User Registration and Authentication:**
   - **Registration**: Users register with personal details such as gender, age range, main fitness goals, and current body stats. This information helps tailor the experience to their needs.
   - **Authentication**: A secure login system uses `werkzeug.security` to hash passwords, ensuring user data is protected. Users can manage their credentials through a password change feature.

2. **Workout Programs:**
   - **Program Selection**: Users can choose from 3-day, 4-day, or 5-day workout programs.
   - **Workout Management**: Users manage their selected workout plans via the "My Plan" page, where they can see their current program and initiate daily workouts.
   - **Workout Execution**: Once a plan starts, users are directed to the "Workout Day" page to follow exercises scheduled for that day.

3. **Exercise Search and Filter:**
   - **Search Functionality**: Users can search exercises based on name and filter results by body part, target muscle, and equipment. This allows users to find exercises that fit their specific needs.
   - **Pagination**: Exercises are displayed in pages, with a "Load More" option to view additional exercises without overwhelming the user with too much information at once.

4. **Nutrition Tracking:**
   - **Nutritional Information**: Using the Nutritionix API, users can search for foods to get detailed nutritional information. The app displays data such as calories, macronutrients, and other nutritional facts.
   - **Food Search**: Users enter food names, and the app retrieves nutritional data to help them make informed dietary choices.

5. **Exercise History:**
   - **Workout Tracking**: Users view their exercise history, including completed workouts and workout days. This feature helps users track progress over time.
   - **Detailed Logs**: The app maintains detailed logs of workouts, allowing users to revisit past exercises and times.

6. **User Interface:**
   - **Responsive Design**: The app is designed to be responsive, ensuring a consistent experience across devices.
   - **Navigation**: Simple navigation with clearly labeled buttons allows users to easily access features like workouts, nutrition, and history.

### File Overview

- **`app.py`**: The main Flask application file. It handles routing, session management, database interactions, and integrates APIs for workouts and nutrition. This file contains routes for user registration, login, workouts, nutrition tracking, and more.

- **HTML Templates**: These files use Jinja2 for dynamic content rendering:
  - **`apology.html`**: Displays error messages to the user.
  - **`change-password.html`**: Interface for users to change their passwords.
  - **`exercise_detail.html`**: Shows detailed information about a specific exercise.
  - **`exercises.html`**: Lists available exercises based on search and filters.
  - **`history.html`**: Displays a history of the user's completed workouts.
  - **`index.html`**: The main entry point that redirects users based on their status.
  - **`home.html`**: Greets users upon login and displays available workout programs.
  - **`layout.html`**: Base layout for the app, including navigation and structure.
  - **`login.html`**: Login form for returning users.
  - **`myplan.html`**: Displays the user's selected workout program and manages daily workouts.
  - **`nutrition.html`**: Interface for users to search for food and view nutritional data.
  - **`program.html`**: Shows workout programs available to the user.
  - **`register.html`**: Registration form for new users.
  - **`workout.html`**: Interface for searching and filtering exercises.
  - **`workout_history.html`**: Displays a history of workout sessions.
  - **`workout_day.html`**: Shows exercises planned for a specific day.
  - **`workout_execution.html`**: Interface for executing workouts during a session.

- **CSS**: Styles the web pages, ensuring a cohesive design and responsive layout.

- **JavaScript**: Handles dynamic actions like loading more exercises and managing form submissions without full page reloads.

- **Database**: SQLite stores user data, exercise details, and workout history in `fitness.db`.

- **APIs**: The app uses ExerciseDB and Nutritionix for workout and nutrition data.

### Design Choices

1. **Technology Stack**: Flask was chosen for its simplicity and rapid development capabilities. SQLite was selected for its ease of setup and efficiency for this project.

2. **Security**: Passwords are hashed with `pbkdf2:sha256` to protect user data. Flask-Session is used to manage sessions and maintain user authentication.

3. **User Experience**: The app is designed with a focus on user experience, offering a clean interface and easy navigation. The search and filter features allow users to quickly find relevant exercises.

4. **API Integration**: Using ExerciseDB and Nutritionix enhances the app's functionality by providing comprehensive workout and nutrition data.

### Challenges and Solutions

During development, several challenges were encountered:

- **Deployment to PythonAnywhere**: Initially, deploying the app to PythonAnywhere was challenging. After researching deployment configurations and settings, the issues were resolved.

- **Search and Filter Functionality**: Implementing the search, filter options, and pagination required careful planning and testing to ensure smooth user interaction.

- **Timer Functionality**: Adding the timer feature was particularly challenging due to my limited experience with JavaScript. However, with persistence and learning, I was able to implement it successfully.

- **Load More Functionality**: Managing dynamic content loading required understanding client-side interactions and server-side data handling.

Overall, TrainMuscleFit was a rewarding project that allowed me to develop a comprehensive understanding of web development and API integration while overcoming various technical challenges.
