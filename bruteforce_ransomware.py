from zipfile import ZipFile, BadZipFile
import os

def attempt_extract(zip_file_path, password):
    try:
        with ZipFile(zip_file_path) as zf:
            zf.extractall(path="decrypted", pwd=password)
            return True
    except RuntimeError:
        return False
    except BadZipFile:
        print("Bad zip file.")
        return False

def bruteforce_zip(zip_file_path, wordlist_path):
    with open(wordlist_path, 'rb') as f:
        for line in f:
            password = line.strip()
            if attempt_extract(zip_file_path, password):
                print(f"[+] Password found: {password.decode()}")
                return password.decode()
    print("[-] Password not found in list")
    return None

if __name__ == "__main__":
    zip_file_path = "enc.zip"
    wordlist_path = "rockyou.txt"
    print("[+] Starting brute-force attack on encrypted zip...")
    bruteforce_zip(zip_file_path, wordlist_path)
