# 🗺️ Google Maps Playwright Python Automation Framework

A modern UI test automation framework designed to validate critical search functionality on Google Maps. Built with a modern, high-performance Python and Playwright stack utilizing the Page Object Model (POM) pattern.

---

## 🛠️ Tech Stack & Architecture

* **Language:** Python 3.12+
* **Automation Engine:** Playwright 
* **Test Runner:** Pytest
* **Reporting:** Allure Report Engine
* **Design Pattern:** Page Object Model (POM) for decoupled, maintainable locators and actions.

---

## 🚀 Key Features

* **Data-Driven Geographic Testing:** Supports dynamic location testing by injecting latitude and longitude coordinates directly into URL parameters. This bypasses fragile browser hardware geolocation permissions, ensuring deterministic, cloud-safe execution across any CI/CD pipeline.
* **Robust Core Framework:** Zero explicit, flaky hardcoded pauses; leverages Playwright's native auto-waiting mechanisms and locator assertions.
* **Scalable Reporting:** Full integration with Allure to capture granular test steps, execution times, and comprehensive suite status.
* **Environment Isolated:** Clean workspace dependencies managed entirely within a local virtual environment (.venv).
* **Cross-Browser Capable:** Engineered to run seamlessly across Chromium, Firefox, and WebKit (Safari).

---

## 📋 Prerequisites & Installation

Ensure you have Python 3.12+ installed on your system.

### 1. Clone the Repository

    git clone https://github.com/markeskritt/google-maps-playwright-python-automation.git
    cd google-maps-playwright-python-automation

### 2. Set up the Virtual Environment & Dependencies

    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt

### 3. Install Playwright Browsers

    playwright install

---

## 🏃 Running the Tests

To run the full end-to-end suite with live browser rendering:

    pytest --headed --slowmo=500

## 📋 Test Suite Overview

The suite currently consists of two distinct functional testing strategies to validate location-based behaviors on live production maps:

* **`test_search_without_coordinates`**
  * **Strategy:** Relies on the host machine's network IP location to establish a baseline.
  * **Behavior:** Automatically searches for a restaurant relative to the user's local region.
  
* **`test_search_with_coordinates`**
  * **Strategy:** Data-driven execution utilizing direct URL parameter injection.
  * **Behavior:** Bypasses browser hardware locks to explicitly search Midtown Toronto using target coordinates:
    * `latitude = 43.7067`
    * `longitude = -79.3984`
  * **Advantage:** Enables completely deterministic, cloud-safe execution across any remote CI/CD environment.

### Core Verification Criteria
Both test variations strictly assert the following structural layers before passing:
1. Dynamic page title resolution.
2. Visibility and interactive state of the core search execution elements.
3. Successful rendering of location-specific results components.

---

## 📊 Generating Allure Reports

To execute tests and capture data for reporting: 

    pytest --headed --slowmo=500 --alluredir=allure-results

To serve and view the interactive HTML Allure Report locally: 

    allure serve allure-results

*(Press Ctrl + C in your terminal to stop serving the report).*

---

## 🌐 Cross-Browser Testing

This framework utilizes Playwright's native multi-engine architecture. Tests run in a highly isolated environment using pristine browser engines, completely separated from local browser histories, profiles, or cached data pollution.

By default, executing pytest runs the test suite on the Chromium engine in headless (hidden) mode.

### Running Different Browser Types

You can target specific browser rendering engines natively via the command line using the --browser flag. Supported engines are chromium, firefox, and webkit.

    # Run on Firefox (Gecko Engine)
    pytest --browser firefox --headed

    # Run on WebKit (Apple Safari Engine)
    pytest --browser webkit --headed

    # Run on Chromium (Default Engine)
    pytest --browser chromium --headed

### Useful Execution Flags

Combine these native flags to fine-tune your local debugging sessions:
* --headed: Disables the default headless mode and pops open the browser UI window.
* --slowmo=<ms>: Introduces a hard delay (in milliseconds) between every automation action (e.g., --slowmo=500), making it easier to visually track execution steps.
* --alluredir=allure-results: Captures framework data and automatically attaches screenshots to the report on failure.

---

## 🛠️ Tools & Frameworks Used (And Why)

* **Python & Pytest:** Python offers a highly readable, expressive syntax that reduces boilerplate code in test scripts. Pytest was selected as the test runner for its powerful fixture model, native test discovery, and seamless execution scalability.
* **Playwright:** Chosen over legacy solutions like Selenium due to its modern architecture. Playwright communicates directly with browser developer tools protocols, enabling built-in auto-waiting, faster execution speeds, and bulletproof stability with near-zero flaky tests.
* **Allure Report:** Integrated to provide clear, human-readable execution dashboards, historical trends, and automatic failure screenshot attachments, which are essential for triage in continuous integration (CI) environments.

---

## 📁 Test Structure Overview

The project strictly follows the Page Object Model (POM) design pattern to isolate UI selectors from core test logic:

    ├── .venv/                      # Isolated virtual environment
    ├── allure-results/             # Raw XML/JSON test artifacts for reporting
    ├── google_maps_page.py         # Page Object Model (POM) holding locators & UI interactions
    ├── test_google_maps.py         # Core test suites and functional assertions
    ├── conftest.py                 # Global Pytest fixtures and Allure screenshot hooks
    ├── requirements.txt            # Project dependencies
    └── README.md                   # Project documentation

---

## 🧠 Assumptions & Limitations

* **OS Environment:** 
* **OS Environment:** The current activation scripts provided in this documentation assume a local Windows environment (`.venv\Scripts\activate`). Mac/Linux users will need to run `source .venv/bin/activate`.

---

## 🚀 Future Improvements 

If this framework was to be scaled into an enterprise-level regression suite, the following enhancements could be prioritised:

1. **CI/CD Integration:** Wrap the suite inside a GitHub Actions workflow to run headlessly on every pull request, automatically publishing the Allure Report pages to GitHub Pages.
2. **Parallel Execution:** Integrate `pytest-xdist` to run tests concurrently across multiple workers, dramatically cutting down suite execution time as the test count scales.
3. **API Validation Layer:** Introduce an asynchronous HTTP client (like HTTPX) to validate backend network responses alongside the UI layout states for true end-to-end coverage.
4. **Visual Regression Testing:** Implement pixel-by-pixel visual assertions using Playwright's native screenshot comparisons to catch subtle CSS alignment or rendering bugs that text-based locators miss.