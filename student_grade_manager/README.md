## # Student Grade Manager

A simple command-line Python application to manage student grades. Add new students, update existing scores, and view all grades in a neat format.

## Features
- Add new students with their scores
- Update scores for existing students
- View all student grades
- Simple menu-driven interface
- Persistent storage in memory during runtime

Follow the on-screen menu:

- **Option 1**: Add or update a student's score
- **Option 2**: Display all student grades
- **Option 3**: Exit the program 

## Code Structure

Class          # Dictionary storing student names and scores
add_student()  # Add/update student score
print_scores() # Display all grades
main loop      # Menu-driven interface

## Installation

1. Clone or download this repository
2. No additional dependencies required (uses only built-in Python libraries)
3. Run `python student_grade_manager.py`

## Initial Students
- Alice: 85
- Bob: 92
- Charlie: 78
- Diana: 88

## Tech Stack
- Python 3.x
- Built-in dict for data storage
- Standard input/output handling

## Future Enhancements
- Save grades to file (JSON/CSV)
- Grade statistics (average, highest, lowest)
- Input validation
- Remove student functionality
- Web interface with Flask
