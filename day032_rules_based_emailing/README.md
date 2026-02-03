# Automated Email & Date Practice Project

This project is part of a **Python bootcamp** and focuses on practicing:
- Dates and time logic
- File handling
- Email automation
- CSV / JSON data management

The project sends **Monday motivational emails** and **automated birthday emails**.

---

## Project Goals

- Learn how to send emails using SMTP
- Practice working with dates (`datetime`)
- Read and write CSV and JSON files
- Use regular expressions for text replacement
- Keep the project simple and readable

---

## Quote Attribution

Motivational quotes used in this project were borrowed from:

https://gist.github.com/robatron/a66acc0eed3835119817

Quotes are used **for learning and practice purposes only**.

---

## File Structure

```
project/
│ main.py
│
├─ letter_templates/
│   ├─ letter_1.txt
│   ├─ letter_2.txt
│   └─ letter_3.txt
│
├─ misc/
│   ├─ birthdays.csv
│   ├─ login.json
│   └─ quotes.txt
```

> Files ending in `.Zone.Identifier` are ignored.

---

## Features

### Monday Motivation Email
- Runs only on Mondays
- Picks a random quote from `quotes.txt`
- Sends email using SMTP credentials from `login.json`

### Birthday Automation
- Stores birthdays in `birthdays.csv`
- Supports add / update / remove operations
- Detects birthdays matching today’s date
- Generates letters from templates
- Sends personalized birthday emails

---

## How It Works

### Core Functions

- `get_filepath()` → finds files in the project
- `is_monday()` → checks if today is Monday
- `email_monday_quote()` → sends Monday email
- `manage_birthdate()` → manages CSV records
- `get_today_birthday()` → checks today’s birthdays
- `generate_birthday_letter()` → fills templates
- `email_birthday_letters()` → sends birthday emails

---

## Requirements

```
python3
pandas
```

Uses Python standard library modules:
- os
- json
- datetime
- smtplib
- random
- re

---

## Run

```
python main.py
```

---

## Notes

- Built for learning, not production
- Emphasis on clarity over abstraction
- Designed to be refactored as skills improve
