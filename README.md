# App Usage Tracker

#### Video Demo: https://youtu.be/jmuuQw5QZ2o

#### Description:

App Usage Tracker is a Python-based desktop application designed to help users understand how they spend time on their computer. The project continuously tracks the active window on a Windows system and records how long each application remains in the foreground. By storing this data daily in structured JSON files, the program enables users to analyze their productivity patterns, identify time-consuming applications, and reflect on their usage habits.

This project was built as the final project for CS50’s Introduction to Programming with Python (CS50P) and demonstrates concepts such as file handling, time-based calculations, modular program design, exception handling, and basic testing with pytest.

## How the Project Works

The application consists of three main Python files, each with a clear responsibility.

## tracker.py

This file handles live app usage tracking.

- Uses the win32gui module to detect the currently active window on Windows.
- Tracks time spent on each application using timestamps rather than counters, ensuring accurate results even if execution timing varies.
- Saves usage data every 60 seconds into a JSON file named using the current date (e.g., usage_2025-12-22.json).
- Automatically resets tracking at midnight by creating a new file for the new day.
- Gracefully handles interruptions (such as CTRL+C) to ensure no data is lost.
- Stores all data inside a tracking_data/ directory created automatically if it does not exist.

📌 **Note:** This tracker is Windows-only due to its reliance on win32gui.

## display.py

This file is responsible for reading and processing stored usage data.

- Loads today’s usage data from JSON files.
- Sorts application usage by total time spent.
- Provides helper functions to:
  - Retrieve today’s usage
  - Retrieve the top 5 most-used applications
  - Retrieve usage data for a specific past date
- Handles missing or corrupted JSON files safely.

## project.py

This is the main entry point of the application.

- Presents a user-friendly menu interface.
- Allows users to:
  - Start live tracking
  - View today’s usage summary
  - View top 5 most-used apps
  - View usage data for a specific date
- Converts raw seconds into a readable format (hours minutes seconds).
- Contains the required main() function and additional testable functions as required by CS50P.

## Testing

The file test_project.py contains unit tests written using pytest.

- Tests verify time formatting logic.
- Tests ensure output functions correctly print results using capsys.
- These tests focus on functions defined in project.py, in line with CS50P requirements.

📌 **Important:**  
The tracker should be run at least once before testing so that usage data files are generated.

## Running the Project

Install dependencies:

pip install pywin32

Run the project:

python project.py

Follow the on-screen menu options.

## Optional: Run Tracker Automatically on Windows Startup

To enable automatic tracking when Windows starts:

Create a file named start_tracker.bat with the following content:

@echo off  
python "FULL_PATH_TO_PROJECT_FOLDER\tracker.py"

Place this `.bat` file in:

C:\Users\<YOUR_USERNAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

This step is optional.

## Design Choices & Limitations

- JSON was chosen over a database for simplicity and transparency.
- Time-based tracking using timestamps ensures higher accuracy than counter-based approaches.
- The project focuses on Windows compatibility due to system API limitations.
- A command-line interface was used to keep the project lightweight and aligned with CS50P scope.

## Conclusion

App Usage Tracker demonstrates a practical application of Python for real-world productivity tracking. It combines system interaction, persistent storage, and data visualization through a clean modular design. The project is extensible and could be expanded in the future with features such as GUI support, web dashboards, or browser extensions.
