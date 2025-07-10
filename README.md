# Passwrod_Strength_Checker

## Description
The Password Strength Checker is a Python GUI application that analyzes the strength of passwords in real-time. It evaluates passwords based on multiple security criteria and provides detailed feedback to help users create stronger passwords.

### Key Features:
- **Real-time analysis**: Checks password strength as you type
- **Comprehensive evaluation**: Tests against 10+ security criteria
- **Common password detection**: Checks against rockyou.txt wordlist (with fallback)
- **Detailed feedback**: Explains exactly what makes a password strong/weak
- **Password generator**: Creates secure random passwords with one click
- **Visual indicators**: Color-coded strength ratings and feedback

The tool helps users understand password security best practices and create credentials that are resistant to brute force and dictionary attacks.

## Usage

### Requirements
- Python 3.x
- Tkinter (usually included with Python)
  ```bash
  pip3 install -r requirements.txt
  ```
### Running the Application
1. Simply run the script:
   ```bash
   python Password_Strength_Checker.py
   ```

2. The GUI window will appear with these components:
   - Password entry field (hidden by default)
   - Show password checkbox
   - Strength indicator (color-coded)
   - Detailed feedback panel
   - "Generate Strong Password" button

### How to Use
1. **Enter a password** in the text field
   - Strength analysis updates automatically as you type
   - Check "Show password" to view what you're typing

2. **Review the feedback**:
   - Green checkmarks (✓) indicate satisfied requirements
   - Red X's (✗) show areas needing improvement
   - Warnings appear for common/weak passwords

3. **Generate a strong password**:
   - Click the "Generate Strong Password" button
   - A 16-character secure password will be created
   - The password is automatically copied to your clipboard

### Password Evaluation Criteria
The tool checks for:
- Minimum length (8+ characters recommended, 12+ ideal)
- Uppercase and lowercase letters
- Numbers and special characters
- Common passwords/patterns (like "123" or "password")
- Keyboard sequences (like "qwerty")
- Pure numeric or alphabetic passwords

### Advanced Features
- **rockyou.txt integration**: For comprehensive common password checking
  - Place rockyou.txt in the script directory or standard locations
  - Falls back to a small built-in list if not found
- **Copy to clipboard**: Generated passwords are ready to paste
- **Responsive UI**: Updates instantly as you type

## Security Notes
- All processing happens locally - no passwords are transmitted
- The password generator creates cryptographically random passwords
- For maximum security, always use unique passwords for different services

This tool is designed for personal and educational use to promote better password hygiene and security awareness.
**OUTPUT**


  <img width="627" height="665" alt="Image" src="https://github.com/user-attachments/assets/9c120efa-e768-4a48-a850-18d68b77a697" />      



