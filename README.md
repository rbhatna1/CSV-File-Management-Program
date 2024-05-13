# CSV-File-Management-Program

## Overview
This Python program provides functions for managing CSV files that store student information. Users can write data to CSV files, read data from CSV files, and perform various analyses and manipulations on the data.

## Functions

### `write()`
- **Description**: Writes student data to the CSV file `Students.csv`. If the file does not exist, it creates the file and writes the headers.
- **Prompts**:
  - Roll number
  - Name

### `reading()`
- **Description**: Reads and prints the contents of the CSV file `Students.csv`.

### `check()`
- **Description**: Checks if the file `student.csv` exists.

### `func()`
- **Description**: Counts and returns the number of rows in the CSV file `Students.csv` where the first column value is "hr" or "manager".

### `count()`
- **Description**: Counts the number of students in the CSV file `student.csv` based on their streams (Science, Commerce, Humanities).

### `Marksbetween()`
- **Description**: Reads and prints the rows from the CSV file `people.csv` where the third column value is a digit between 85 and 95.

### `Student()`
- **Description**: Writes student course data to the CSV file `StudCourse.csv`.
- **Prompts**:
  - Roll number
  - Name
  - Course

### `SetSub()`
- **Description**: Returns a string of subjects based on the course input.
- **Returns**:
  - 'Phy-Che-Mat' for Science
  - 'Acc-Bus-Eco' for Commerce
  - 'His-Pol-Web' for Humanities

### `READ()`
- **Description**: Reads and prints the contents of the CSV file `StudCourse.csv`.

### `Humanities()`
- **Description**: Reads and prints the rows from the CSV file `people.csv` where the second column value is "humanities".

### `Altrecords()`
- **Description**: Reads and prints every alternate record from the CSV file `StudCourse.csv`.

### `Grade()`
- **Description**: Reads the marks from the CSV file `people.csv` and prints the corresponding grade based on the mark range.

## How to Run the Program

1. Ensure the required CSV files are present in the same directory as the script.
2. Run the script.
3. Call the desired functions to perform specific operations on the CSV files.

## Example Usage

```python
write()
reading()
check()
count = func()
print(count)
count()
Marksbetween()
Student()
READ()
Humanities()
Altrecords()
Grade()
