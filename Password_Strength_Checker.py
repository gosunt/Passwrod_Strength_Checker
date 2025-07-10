import tkinter as tk
from tkinter import ttk, messagebox
import re
import random
import string
import os
from pathlib import Path

class PasswordStrengthChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Analyzer")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        
        # Load the rockyou.txt file
        self.common_passwords = self.load_common_passwords()
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('Red.TLabel', foreground='red', font=('Arial', 10, 'bold'))
        self.style.configure('Green.TLabel', foreground='green', font=('Arial', 10, 'bold'))
        self.style.configure('Yellow.TLabel', foreground='orange', font=('Arial', 10, 'bold'))
        
        self.create_widgets()
    
    def load_common_passwords(self):
        """Load common passwords from rockyou.txt file"""
        common_passwords = set()
        try:
            # Try to find rockyou.txt in common locations
            possible_paths = [
                'rockyou.txt',
                '/usr/share/wordlists/rockyou.txt',
                '/usr/share/dict/rockyou.txt',
                str(Path.home() / 'rockyou.txt')
            ]
            
            found_path = None
            for path in possible_paths:
                if os.path.exists(path):
                    found_path = path
                    break
            
            if found_path:
                with open(found_path, 'r', encoding='latin-1') as f:
                    for line in f:
                        common_passwords.add(line.strip())
                return common_passwords
            else:
                messagebox.showwarning(
                    "Warning", 
                    "rockyou.txt not found. Common password checking will be limited.\n"
                    "Please place rockyou.txt in the same directory as this script."
                )
                return set(['password', '123456', 'qwerty', 'abc123', 'letmein'])  # minimal fallback
        except Exception as e:
            messagebox.showerror("Error", f"Could not load rockyou.txt: {str(e)}")
            return set()
    
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="Password Strength Analyzer", font=('Arial', 14, 'bold'))
        title_label.pack(pady=(0, 15))
        
        # Password entry frame
        entry_frame = ttk.Frame(main_frame)
        entry_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(entry_frame, text="Enter Password:").pack(side=tk.LEFT)
        
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(entry_frame, textvariable=self.password_var, show="*", width=30)
        self.password_entry.pack(side=tk.LEFT, padx=(5, 0))
        self.password_entry.bind('<KeyRelease>', self.check_password_strength)
        
        # Show password checkbox
        self.show_password_var = tk.IntVar()
        show_password_cb = ttk.Checkbutton(main_frame, text="Show password", 
                                          variable=self.show_password_var,
                                          command=self.toggle_password_visibility)
        show_password_cb.pack(anchor=tk.W, pady=(0, 10))
        
        # Strength indicator frame
        strength_frame = ttk.Frame(main_frame)
        strength_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(strength_frame, text="Strength:").pack(side=tk.LEFT)
        
        self.strength_label = ttk.Label(strength_frame, text="", font=('Arial', 10, 'bold'))
        self.strength_label.pack(side=tk.LEFT, padx=(5, 0))
        
        # Common password warning
        self.common_password_warning = ttk.Label(main_frame, text="", style='Red.TLabel')
        self.common_password_warning.pack(fill=tk.X, pady=(0, 10))
        
        # Feedback frame
        feedback_frame = ttk.LabelFrame(main_frame, text="Feedback", padding=10)
        feedback_frame.pack(fill=tk.BOTH, expand=True)
        
        self.feedback_text = tk.Text(feedback_frame, height=8, wrap=tk.WORD, padx=5, pady=5)
        self.feedback_text.pack(fill=tk.BOTH, expand=True)
        
        # Generate strong password button
        generate_btn = ttk.Button(main_frame, text="Generate Strong Password", command=self.generate_strong_password)
        generate_btn.pack(pady=(10, 0))
    
    def toggle_password_visibility(self):
        if self.show_password_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")
    
    def check_password_strength(self, event=None):
        password = self.password_var.get()
        
        if not password:
            self.strength_label.config(text="", style='TLabel')
            self.feedback_text.delete(1.0, tk.END)
            self.common_password_warning.config(text="")
            return
        
        # Reset common password warning
        self.common_password_warning.config(text="")
        
        # Calculate strength score
        score = 0
        feedback = []
        
        # Check if password is in common passwords list
        if password.lower() in self.common_passwords:
            score -= 3
            feedback.append("✗ Password found in common passwords list (very weak)")
            self.common_password_warning.config(
                text="WARNING: This password was found in a list of commonly hacked passwords!",
                style='Red.TLabel'
            )
        
        # Length check
        if len(password) >= 12:
            score += 3
            feedback.append("✓ Good password length (12+ characters)")
        elif len(password) >= 8:
            score += 2
            feedback.append("✓ Moderate password length (8+ characters)")
        else:
            feedback.append("✗ Password is too short (minimum 8 characters recommended)")
        
        # Uppercase letters
        if re.search(r'[A-Z]', password):
            score += 1
            feedback.append("✓ Contains uppercase letters")
        else:
            feedback.append("✗ Add uppercase letters")
        
        # Lowercase letters
        if re.search(r'[a-z]', password):
            score += 1
            feedback.append("✓ Contains lowercase letters")
        else:
            feedback.append("✗ Add lowercase letters")
        
        # Numbers
        if re.search(r'[0-9]', password):
            score += 1
            feedback.append("✓ Contains numbers")
        else:
            feedback.append("✗ Add numbers")
        
        # Special characters
        if re.search(r'[^A-Za-z0-9]', password):
            score += 2
            feedback.append("✓ Contains special characters")
        else:
            feedback.append("✗ Add special characters (!@#$%^&*, etc.)")
        
        # Common patterns (weak patterns)
        weak_patterns = [
            (r'123', "Avoid simple sequences like '123'"),
            (r'abc', "Avoid simple sequences like 'abc'"),
            (r'qwerty', "Avoid keyboard patterns like 'qwerty'"),
            (r'password', "Avoid common words like 'password'"),
            (r'^\d+$', "Avoid numbers only"),
            (r'^[A-Za-z]+$', "Avoid letters only")
        ]
        
        for pattern, message in weak_patterns:
            if re.search(pattern, password, re.IGNORECASE):
                score -= 1
                if message not in feedback:
                    feedback.append(f"✗ {message}")
        
        # Determine strength level
        if score >= 7:
            strength = "Very Strong"
            style = "Green.TLabel"
        elif score >= 5:
            strength = "Strong"
            style = "Green.TLabel"
        elif score >= 3:
            strength = "Moderate"
            style = "Yellow.TLabel"
        else:
            strength = "Weak"
            style = "Red.TLabel"
        
        self.strength_label.config(text=strength, style=style)
        
        # Update feedback
        self.feedback_text.delete(1.0, tk.END)
        self.feedback_text.insert(tk.END, "\n".join(feedback))
        
        # Color code feedback
        for i, line in enumerate(feedback, 1):
            if line.startswith("✓"):
                self.feedback_text.tag_add("good", f"{i}.0", f"{i}.end")
                self.feedback_text.tag_config("good", foreground="green")
            elif line.startswith("✗"):
                self.feedback_text.tag_add("bad", f"{i}.0", f"{i}.end")
                self.feedback_text.tag_config("bad", foreground="red")
    
    def generate_strong_password(self):
        # Generate a random strong password
        length = 16
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        # Ensure we have at least one of each character type
        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(symbols)
        ]
        
        # Fill the rest with random choices
        all_chars = lowercase + uppercase + digits + symbols
        password.extend(random.choice(all_chars) for _ in range(length - 4))
        
        # Shuffle the password
        random.shuffle(password)
        strong_password = ''.join(password)
        
        # Show the password in a messagebox
        messagebox.showinfo("Strong Password Suggestion", 
                          f"Here's a strong password suggestion:\n\n{strong_password}\n\n"
                          "Copy this to your clipboard and use it if you like it.")
        
        # Optional: copy to clipboard
        self.root.clipboard_clear()
        self.root.clipboard_append(strong_password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordStrengthChecker(root)
    root.mainloop()
