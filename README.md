# E2E Automation Framework (Playwright + Behave + Allure)

This project is an **End-to-End (E2E) Automation Test Framework** using:

* **Playwright (Python)** → UI Automation
* **Behave (BDD)** → Behavior Driven Development
* **Allure Report** → Test Reporting

Target website: https://www.saucedemo.com/


# 1. Prerequisites

Make sure you have installed:

* Python 3.8+
* pip
* Git

---

# 2. Installation

## Clone Repository

```
git clone https://github.com/mohammadalfirizzi/automation_saucedemo.git
cd your-repo
```

## Create Virtual Environment

### Windows

```
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```
pip install -r requirements.txt
```

---

## Install Playwright Browsers

```
playwright install
```

---

# 3. Run Automation Test

```
behave
```

---

# 4. Generate Allure Report

## Run test with Allure formatter

```
behave -f allure_behave.formatter:AllureFormatter -o reports/
```

## Open report

You must install the allure report "https://allurereport.org/docs/"
```
allure serve reports/
```

---

# 5. Test Coverage

### Login

* Positive login
* Invalid credentials
* Empty fields
* Locked user

### Product

* View product list
* Sort product
* View product detail

### Cart

* Add item
* Remove item
* View cart

### Checkout

* Complete purchase
* Validation (empty fields)

### Navigation

* Continue shopping
* Back to inventory

### Logout

* Logout successfully

---

# Framework Design

* Page Object Model (POM)
* BDD (Gherkin syntax)
* Reusable steps
* Screenshot on failure
  
---

---
