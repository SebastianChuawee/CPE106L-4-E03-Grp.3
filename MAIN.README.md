# CPE106L-4-E03-Grp.3
# Login UI Instructions & Explanation

Welcome to the User Login Application! This guide will help you understand and use the Login-UI effectively.

---

## What is the Login-UI?

The Login-UI is the first screen you see when you launch the app. It allows users to securely enter their credentials (username/email and password) to access the application's features.

---

## Step-by-Step Instructions

### 1. Launch the App

- Double-click on the application's executable or run the following command in your terminal:
  ```bash
  python main.py
  ```

### 2. Understanding the Login Window

The Login Window typically includes:
- **Username or Email Field:** Where you enter your registered username or email.
- **Password Field:** Where you enter your password. Characters will typically appear as dots or asterisks for security.
- **Login Button:** Click this to submit your credentials.
- **Show/Hide Password Option:** (If available) Click the eye icon to show/hide your password text.
- **Forgot Password Link:** If you’ve forgotten your password, click this to recover or reset it.
- **Register/Sign Up Button:** (If available) For new users to create an account.

### 3. Logging In

1. **Enter your username or email:**  
   Click inside the field labeled "Username" or "Email" and type your registered information.
2. **Enter your password:**  
   Click the "Password" field and type your password. If you want to see what you’re typing, use the show/hide password option.
3. **Submit your credentials:**  
   Click the “Login” button or press Enter.
4. **Successful Login:**  
   You will be directed to the main app dashboard or home screen.
5. **Failed Login:**  
   If the credentials are incorrect, you will see an error message (e.g., "Invalid username or password"). Double-check your information and try again.

### 4. Password Assistance

- Click "Forgot Password?" to start the recovery process. Follow the prompts, which usually involve verifying your email and setting a new password.

### 5. Registering a New Account

- If you don’t have an account, click “Sign Up” or “Register.” Fill in the required information and follow the prompts to create your account.

---

## Security Tips

- Never share your password with others.
- Use a strong password (mix of letters, numbers, and symbols).
- Always log out after using the app on shared devices.

---

## Troubleshooting

- **App won’t open:** Ensure Python is installed and you’re in the correct directory.
- **Can’t log in:** Make sure Caps Lock is off and credentials are correct. Use the "Forgot Password" option if needed.
- **UI elements not displaying:** Ensure all required dependencies are installed.

---

## Developer Explanation (How it works under the hood)

- **Input Validation:** The UI checks if both fields are filled before submission.
- **Credential Check:** Submitted credentials are compared against a secure user database (could be local or cloud-based).
- **Feedback:** The UI provides immediate feedback (success or error message).
- **Session Handling:** After successful login, the app creates a session for the user, granting access to further features.
- **Security:** Passwords are never displayed in plain text and are handled securely.

---

If you need further assistance, please refer to the [Help Section] or contact support.
