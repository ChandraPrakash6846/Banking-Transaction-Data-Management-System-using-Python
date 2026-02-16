# Banking-Transaction-Data-Management-System-using-Python
A Python-based banking transaction data management system designed to securely create accounts, process financial transactions, and maintain persistent structured data. This project demonstrates real-world financial data handling, structured storage, and transaction tracking relevant to Data Analyst and financial analytics workflows.

## Overview
This system simulates core banking operations and generates structured financial data that can be used for analysis, reporting, and financial data processing. It follows modular architecture principles and ensures persistent storage of account and transaction records.
The project demonstrates how financial transaction data is created, stored, managed, and maintained in a structured format.

##Key Features

* Account creation and authentication system

* Deposit and withdrawal transaction processing

* Persistent data storage using JSON

* Transaction history tracking

* Structured financial data generation

* Modular and scalable architecture

* Input validation and error handling

## Tech Stack

* Language: Python 3

* Data Storage: JSON (persistent structured storage)

## Core Concepts:

* Object-Oriented Programming (OOP)

* File Handling

* Data Persistence

* Modular Architecture

* Authentication System

* Financial Data Modeling

## Project Structure
Banking-System/
│
├── Main.py
├── bank.py
├── account.py
├── auth.py
├── storage.py
├── bank_data.json
└── README.md


## File Description:

* Main.py — Controls application flow and user interaction

* bank.py — Handles account creation and management logic

* account.py — Manages account balance and transactions

* auth.py — Handles login authentication

* storage.py — Handles data saving and loading

* bank_data.json — Stores account and transaction data

## System Architecture
User
 │
 ▼
Main.py
 │
 ├── Authentication Layer (auth.py)
 ├── Business Logic Layer (bank.py)
 ├── Account Processing Layer (account.py)
 └── Storage Layer (storage.py)
      │
      ▼
   JSON Database

## Data Model

Each account is stored in structured format:

{
  "account_number": "58644632",
  "account_holder_name": "User",
  "password": "password",
  "balance": 8000.0,
  "transaction_history": [
    {
      "type": "Deposit",
      "amount": 10000.0,
      "balance": 10000.0
    }
  ]
}

## Transaction Processing Flow
User Input
   │
   ▼
Validation
   │
   ▼
Balance Update
   │
   ▼
Transaction Recording
   │
   ▼
Data Storage

## Example Operations

* Create new account

* Login to account

* Deposit money

* Withdraw money

* View transaction history

* Save and load account data

## How to Run the Project
### Step 1: Install Python

* Ensure Python 3 is installed.

* Check version:

* python --version

### Step 2: Clone the Repository
* git clone https://github.com/yourusername/banking-transaction-system.git

### Step 3: Navigate to Project Folder
* cd banking-transaction-system

### Step 4: Run the Application
* python Main.py

## Example Console Interface
### MAIN MENU
1. Create Account
2. Login
3. Exit

###ACCOUNT MENU
1. Deposit
2. Withdraw
3. View Transactions
4. Logout

## Data Analysis Relevance

* This project generates structured financial transaction data that can be used for:

* Transaction analysis

* Financial reporting

* Customer transaction behavior analysis

* Data visualization

* Financial data processing

* Skills Demonstrated

* Python Programming

* Structured Data Handling

* Financial Data Management

* Object-Oriented Programming
  
* Data Persistence

* Modular System Design

* Backend Data Processing

## Future Improvements

* SQL database integration (MySQL/PostgreSQL)

* Password encryption

* Data analysis dashboard

* REST API integration

* Cloud deployment

## Author

Chandra Prakash Choudhary
Data Analyst | Python | SQL | Power BI

Project Status

Active and maintained for portfolio and learning purposes.
