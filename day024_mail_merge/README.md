# Mail Merge Project

This Python script automates the process of creating personalized letters for multiple recipients.  
It reads a list of names and a sample letter, replaces the placeholder `[name]` with each recipient’s name, and saves the final letters in a folder.

## How It Works
1. Reads the sample letter from  
   `./Input/Letters/starting_letter.txt`
2. Reads recipient names from  
   `./Input/Names/invited_names.txt`
3. Replaces `[name]` in the sample letter with each name.
4. Saves each personalized letter in a new folder named `ReadyToSend`.

## Folder Structure
```
Input/
 ├── Letters/
 │    └── starting_letter.txt
 └── Names/
      └── invited_names.txt
ReadyToSend/
```

## Run the Script
```bash
python3 main.py
```

Each generated letter will be saved in the `ReadyToSend` folder as a `.txt` file.
