# Basic-Student-Management-System-API
 Using Python,Flask,DB,HTML,CSS,SQLite


<!-- Project 1: Basic Student Management System API

Project Description

Create a simple RESTful API using Flask (Python) to manage basic student information. The API should provide endpoints for CRUD operations (Create, read, update, delete) on student records.

What is Expected from the Student

Implement the API using Flask (Python).

Ensure the API can:

Add a new student record.

Retrieve a list of all students.

Update an existing student record.

Delete a student record.

Use SQLite for data persistence. -->

python -m venv myenv


.\myenv\Scripts\Activate.ps1


pip install flask


>>> from create_database import init_db
>>> init_db()
>>> exit()


1. SQLite Viewer Extension (Optional):

While SQLite databases can be managed directly from Python code using the sqlite3 module, a visual SQLite viewer extension for your code editor can enhance the experience.
Popular options include:
VS Code: The "SQLite" extension by Pranay Prakash (https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite)
PyCharm: Built-in support for SQLite database browsing
Other editors: Search for extensions in your editor's marketplace.
2. Creating a Virtual Environment (Recommended):

Using a virtual environment isolates project dependencies from your system-wide Python installation, preventing conflicts.

Here's how to create a virtual environment using venv (Python 3.3+):

Bash
python -m venv .venv  # Replace ".venv" with your desired virtual environment name
Use code with caution.
content_copy
Activate the environment on different operating systems:

Windows:

Bash
.venv\Scripts\activate.ps1
Use code with caution.
content_copy
macOS/Linux:

Bash
source .venv/bin/activate
Use code with caution.
content_copy
3. Installing Flask (Within the Virtual Environment):

Once the virtual environment is active, install Flask using pip:

Bash
pip install Flask
Use code with caution.
content_copy
4. Creating the create_database.py Script:

Create a new Python file named create_database.py and add the following code to connect to or create an SQLite database, define a table schema, and execute the CREATE TABLE statement:

Python
import sqlite3

# Database path (replace with your desired path)
db_path = 'my_database.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create a table if it doesn't exist
table_schema = """
CREATE TABLE IF NOT EXISTS my_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    # Add more columns as needed
)
"""

cursor.execute(table_schema)
conn.commit()  # Commit changes to the database

conn.close()
Use code with caution.
content_copy
Replace 'my_database.db' with the desired location and name for your database file.
Modify the table_schema string to define your table structure, including column names, data types, and constraints.
5. Running the Script:

Navigate to the directory containing create_database.py in your terminal.

Execute the script:

Bash

python create_database.py


6. Optional: Flask Application (Not Required for Database Creation)

If you're planning to use Flask in a separate project, you can create a Flask application to interact with the database. This is a different process beyond the scope of creating a database, but here's a basic example structure:

Python
 run == ( python -m flask run )
