# Personal Finance App

A Streamlit-based web application for managing personal finances. This application provides an intuitive interface for tracking your financial data and managing your personal budget.

## Features

- User-friendly interface
- Personal finance dashboard
- Customizable settings
- Responsive design

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Local Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd personal_finance_streamlit
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:
   ```bash
   streamlit run app.py
   ```

6. Open your browser and navigate to http://localhost:8501

## Docker Installation

1. Build the Docker image:
   ```bash
   docker build -t personal-finance-app .
   ```

2. Run the container:
   ```bash
   docker run -p 8501:8501 personal-finance-app
   ```

3. Access the application at http://localhost:8501

## Usage

1. After launching the application, you'll see the main dashboard.
2. Use the sidebar buttons to:
   - Add new financial entries
   - Customize your preferences
   - Access settings

## License

This project is licensed under the MIT License - see the LICENSE file for details.