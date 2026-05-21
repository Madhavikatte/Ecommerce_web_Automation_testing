# 🛒 nopCommerce Web Automation Testing Framework

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pytest](https://img.shields.io/badge/Tested%20with-Pytest-yellow?logo=pytest)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green?logo=selenium)
![Framework](https://img.shields.io/badge/Framework-Page%20Object%20Model-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A robust Selenium-Pytest automation framework for end-to-end testing of the [nopCommerce](https://demo.nopcommerce.com/) e-commerce platform, built using the **Page Object Model (POM)** design pattern.

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Test Coverage](#test-coverage)
- [Setup & Installation](#setup--installation)
- [How to Run Tests](#how-to-run-tests)
- [Test Reports](#test-reports)
- [Author](#author)

---

## About the Project

This framework automates functional testing of the nopCommerce e-commerce demo site. It is structured using the **Page Object Model** pattern to ensure clean separation between test logic and UI interaction, making tests easy to maintain and scale.

Key design decisions:
- Page Objects abstract all UI locators and interactions
- Test data is externalized into the `Test_data/` folder (not hardcoded)
- Configurations (browser, base URL) are centralized in `Configurations/`
- HTML reports are auto-generated after every test run

---

## Tech Stack

| Tool | Purpose |
|------|----------|
| Python 3.x | Core language |
| Selenium WebDriver | Browser automation |
| Pytest | Test runner & assertions |
| pytest-html | HTML test report generation |
| Page Object Model | Framework design pattern |

---

## Project Structure

```
Ecommerce_web_Automation_testing/
│
├── Configurations/         # Browser setup, base URL, driver config
├── PageObject/             # Page classes — one per UI page (POM)
├── TestCases/              # Test scripts using page objects
├── conftest.py             # Pytest fixtures and setup/teardown
├── Test_data/              # External test data (credentials, inputs)
├── Utilities/              # Reusable helpers (waits, logger, etc.)          
├── pytest.ini              # Pytest configuration
├── requirements.txt        # Project dependencies
└── README.md
```

---

## Test Coverage

| Module                | Test Scenarios |
|-----------------------|---------------|
| **Login / Logout**    | Valid login, invalid credentials, logout flow |
| **customer Search**   | Search by keyword, filter by category |

---

## Setup & Installation

### Prerequisites
- Python 3.8 or higher
- Google Chrome browser
- ChromeDriver (matching your Chrome version)

### 1. Clone the repository

```bash
git clone https://github.com/Madhavikatte/Ecommerce_web_Automation_testing.git
cd Ecommerce_web_Automation_testing
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## How to Run Tests

### Run all tests with HTML report

```bash
pytest
```

### Run a specific test file

```bash
pytest TestCases/test_login.py --html=Reports/report.html --self-contained-html
```

### Run with verbose output

```bash
pytest TestCases/ -v --html=Reports/report.html --self-contained-html
```

---

## Test Reports

After each run, an HTML report is generated in the `Reports/` folder.

> Note: The `Reports/` directory is excluded from version control (see `.gitignore`). Reports are generated locally on each test run.

---

## Author

**Madhavi Katte**
QA Automation Engineer | Python · Selenium · Pytest · POM

📧 madhavikatte99@gmail.com
🔗 [GitHub Profile](https://github.com/Madhavikatte)
