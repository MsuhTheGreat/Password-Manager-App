# **🔐 Password Manager App – Your Personal Digital Vault**
Welcome to your very own secure, encrypted, and user-friendly Password Manager, built entirely in Python with a clean GUI using Tkinter. Whether you're a developer, a student, or someone who values digital safety, this application is designed to keep your credentials safe, accessible, and only in your control.

## **✨ What Makes This Password Manager Special?**
### **🔑 Master Password Lock**
Upon launch, the app prompts you to enter or create a master key. This key is your digital lockpick — no one can view or access your saved data without it.

### **🧊 7-Zip AES-256 Encryption**
Security is at the heart of this project. All your passwords are stored in a .json file and then encrypted using 7-Zip with AES-256. The decrypted file is deleted after every session to ensure data privacy.

### **💻 GUI-Driven Simplicity**
No terminal commands, no config files — just a clean, modern interface built with Tkinter. All features are accessible via buttons, entry fields, and friendly popups.

### **🔐 Password Generator**
Tired of reusing weak passwords? The app can generate random, strong passwords (30 to 40 characters) containing upper/lowercase letters, digits, and symbols. One click, and it's done — and copied to your clipboard too!

### **🔍 Smart Search**
Forgot a password for a site? Just type the website name and hit "Search" — the app fetches the username/email and password instantly and even copies the password to your clipboard.

### **🧾 View All Stored Data**
Easily view all stored login data in a readable format — helpful for managing or auditing your vault.

### **📋 Clipboard Convenience**
Every password you generate or search is automatically copied to the clipboard, ready to paste wherever you need.

### **⚠️ Graceful Error Handling**
From missing files to decryption errors, every critical action is wrapped with clear, user-friendly popup messages.

## **🚀 How Does It Work?**
1. **Initial Setup:**

    - On first run, you’re prompted to create a master key.

    - This master key is used for encryption/decryption via 7-Zip.

    - The app saves all data to a .json file, then encrypts it to Passwords.7z.

2. **Future Launches:**

    - You'll be asked to enter the same master key to decrypt your vault.

    - All operations (viewing, adding, searching) are done on the decrypted JSON.

    - Once the task is complete, the .json is encrypted again and deleted.

## **📁 Project Structure**
```
Password_Manager_App/
│
├── main.py                    # Main application logic
├── seven_zip_path.txt         # Stores the path to your 7-Zip executable
├── Passwords.7z               # Encrypted password data (auto-generated)
├── Passwords.json             # Decrypted version (temporary; auto-deleted)
├── logo.png                   # Main window logo
├── key.png                    # Key image for password creation window
├── opening_key.png            # Lock image for password prompt
```
## **🛠 Requirements**
- Python 3.x

- 7-Zip (must be installed locally)

## **Python Libraries:**
- tkinter (GUI – standard in Python)

- pyperclip (for clipboard handling)

- json (data storage)

- subprocess (running 7-Zip commands)

- os (filesystem operations)

- random (password generator)

- ttk (modern widgets from tkinter)

## **🔧 Setup Guide**
1. **Install 7-Zip**  
If not already installed, download 7-Zip from:
https://www.7-zip.org/download.html

2. **Get the Path to `7z.exe`**  
Usually it's located at:
```
    C:\Program Files\7-Zip\7z.exe
```
3. **Paste the Path in `seven_zip_path.txt`**  
This is how the app knows where 7-Zip lives on your system.

4. **Run the App**
```
    python main.py
```
5. **Create or Enter Master Password**  
Follow the prompts and start managing your digital vault.

## **💡 Future Improvements (Ideas You Can Build On)**
- **🔄 Password Update & Deletion Options**

- **☁️ Cloud Sync (Encrypted) with Google Drive or Dropbox**

- **🔐 Password Strength Meter**

- **🌑 Dark Mode UI Toggle**

- **🔒 Biometric Authentication (Face ID/Fingerprint) Integration**

- **📁 Category-wise Sorting (Social, Banking, Work, etc.)**

- **📋 Export/Import Backup with Encryption**

## **🎓 Why I Built This**
I created this Password Manager to learn practical encryption, build a Tkinter-based app with real value, and explore how everyday users can protect themselves from password fatigue and data breaches — without relying on third-party cloud services.

## **📬 Contact**
Made by MsuhTheGreat  
For suggestions, bugs, or improvements, feel free to open an issue or contribute.