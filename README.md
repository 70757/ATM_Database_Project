# ATM_Database_Project
ATM Database Management System (Python + MySQL)

## Overview
A simple ATM simulation built using Python and MySQL.
It lets users register, log in, check balance, deposit, withdraw, change PIN, and return card, with all data stored in a database.

## Features

1.Register new users
2.Secure login using card number & PIN
3.View account balance
4.Deposit & withdraw money
5.Change PIN
6.Return card option

## Database Setup
Run these commands in MySQL:
CREATE DATABASE atm;
USE atm;
SELECT * FROM users;
The users table is auto-created by the Python script.

## Setup & Run
1.Install dependency:
pip install mysql-connector-python
2.Update MySQL credentials in atmdm.py
3.Run the program:python atmdm.py

## Technologies Used

Python 3,
MySQL,
mysql-connector-python,
Time Module (for simulation delays)

