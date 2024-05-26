# User Model Project

This project demonstrates the creation of a SQLAlchemy model named `User` for a database table named `users`. The model includes the following attributes:
- `id`: the integer primary key
- `email`: a non-nullable string
- `hashed_password`: a non-nullable string
- `session_id`: a nullable string
- `reset_token`: a nullable string

## Files

- `user.py`: Contains the definition of the `User` model.
- `main.py`: Demonstrates the usage of the `User` model by printing the table name and column details.

## Requirements

- Python 3.7
- SQLAlchemy 1.3.x
- pycodestyle 2.5

## Usage

Make sure all files are executable. You can run the `main.py` file to see the output.

```sh
chmod +x user.py main.py
./main.py
