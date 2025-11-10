# 🔤 NATO Phonetic Alphabet Converter

## 📘 Description
This Python script converts any entered word into its **NATO phonetic alphabet** equivalent.  
For example, typing `hello` returns:  
```
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
```

---

## 🧰 Requirements
Make sure you have:
- **Python 3** installed  
- The **pandas** library:
  ```bash
  pip install pandas
  ```
- A file named **nato_phonetic_alphabet.csv** in the same directory, containing columns:
  ```
  letter,code
  A,Alpha
  B,Bravo
  ...
  Z,Zulu
  ```

---

## ▶️ How to Run
1. Place the following files in one folder:
   ```
   day026_NATO_alphabet_converter/
   ├── main.py
   └── nato_phonetic_alphabet.csv
   ```
2. Run the script:
   ```bash
   python main.py
   ```
3. Enter a word when prompted in the terminal.

---

## 🎯 Usage Example
```
Enter word: hello
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']

Enter another word: WORD
['Whiskey', 'Oscar', 'Romeo', 'Delta']
```

To quit, type:
```
exit
```

---

## ⚠️ Notes
- Words must contain only **letters** (no numbers or empty input).  
- If you type an invalid word, an error message will appear:
  ```
  Error: Word must be entered.
  ```
