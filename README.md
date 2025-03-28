# Bruteforce Python Code #
A collection of hands-on Python scripts focused on cybersecurity tasks, automation, and problem-solving—ranging from brute-force simulations to vulnerability analysis and file handling. Built to showcase technical skills, creativity, and real-world applicability.


# Brute-Force Ransomware Decryption Script 🔐

This project demonstrates how to use Python to perform a brute-force attack on a password-protected zip file. The simulation mimics a cybersecurity task to recover encrypted files without paying a ransom.

## 💡 Overview

This script:
- Reads a list of common passwords from a wordlist (`rockyou.txt`)
- Attempts to decrypt a zip file (`enc.zip`) using each password
- Extracts the contents upon successful password match

## 📁 Files Included

- `bruteforce_ransomware.py`: Main script for brute-forcing the encrypted zip.
- `rockyou.txt`: Sample wordlist (not included here for size constraints).
- `enc.zip`: Example encrypted archive (not included here).
- `ImportantFile.pdf`: Final output file generated from a decrypted `.docx`.

## 🚀 Usage

1. Place the following files in the same directory:
   - `bruteforce_ransomware.py`
   - `enc.zip`
   - `rockyou.txt`

2. Run the script using Python 3:
   ```bash
   python bruteforce_ransomware.py
3. If the correct password is found in the wordlist, the zip will be extracted into a decrypted/ directory.

4. Inside the extracted files, you'll find ImportantFile.docx.

5. To convert this file to PDF, use a script or tool that loads the Word document and writes it to PDF. In this case, Python libraries like python-docx and fpdf were used to generate ImportantFile.pdf.

## 🛠 Dependencies

Python 3.x

No external libraries needed for the brute-force script

Optional (for DOCX to PDF conversion):

- python-docx
- fpdf

## ⚠️ Disclaimer
# This script is for educational purposes only. Always ensure you have permission to test systems and files. Unauthorized access or cracking of password-protected files is illegal and unethical. 

## 🧠 Why This Is Important
Ransomware attacks are one of the most common and devastating threats in cybersecurity. Learning how to ethically test and recover encrypted data strengthens your ability to:

Understand the mechanics of file encryption and password protection.

Develop scripts for incident response and forensic analysis.

Build a proactive mindset when facing real-world cyber threats.

## 🎯 Why This Matters for Cybersecurity Analysts
Cybersecurity analysts are often on the front lines of responding to security incidents, including ransomware attacks. Being able to:

Simulate attack scenarios and potential recoveries,

Think critically under pressure,

Investigate encrypted or suspicious files,

And automate parts of the analysis or recovery process using scripting,

...are all crucial skills. This project reinforces practical, analytical, and scripting abilities that align closely with real-world tasks an analyst may encounter during incident response, threat hunting, or forensic investigations. 
