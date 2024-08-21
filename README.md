# Flask Cafe Management App

This is a simple Flask web application for managing cafes. The application allows users to add cafe details through a form and view a list of cafes with their details. It uses Flask, Flask-WTF for form handling, and Flask-Bootstrap for styling.

## Features

- **Home Page**: Displays a welcome message or main content.
- **Add Cafe**: Form for adding cafe details including name, location, open/close times, coffee quality, WiFi speed, and power availability.
- **Cafes List**: Displays a list of all cafes added through the form.

## Technologies Used

- **Flask**: Web framework for building the web application.
- **Flask-WTF**: Simplifies form handling and validation.
- **Flask-Bootstrap**: Integrates Bootstrap with Flask for styling.
- **CSV**: Used for storing and retrieving cafe data.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**:
    ```bash
    python app.py
    ```

5. **Navigate to**:
    Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- **Home Page**: Access the home page at `http://127.0.0.1:5000/`.
- **Add Cafe**: Go to `http://127.0.0.1:5000/add` to add a new cafe.
- **Cafes List**: View the list of cafes at `http://127.0.0.1:5000/cafes`.

## Code Overview

### `app.py`

- **Imports**: Necessary modules including Flask, Flask-WTF, and CSV.
- **Form Validation**: Custom validator `validate_https` ensures URL starts with `https://`.
- **Routes**:
  - **Home (`/`)**: Renders the home page.
  - **Add Cafe (`/add`)**: Handles form submission and CSV writing. Redirects to the cafes list page.
  - **Cafes (`/cafes`)**: Reads cafe data from CSV and renders it in a list format.

### Form Fields

- **Cafe Name**: Required field for the cafe's name.
- **Location**: Required field for the cafe's location, must start with `https://`.
- **Open**: Required field for opening time.
- **Close**: Required field for closing time.
- **Coffee Quality**: Select field with choices representing coffee quality.
- **WiFi Speed**: Select field with choices representing WiFi speed.
- **Power Availability**: Select field with choices representing power availability.

## Requirements

- **Flask**: ^2.0.0
- **Flask-WTF**: ^1.0.0
- **Flask-Bootstrap**: ^5.0.0

Create a `requirements.txt` file with the following content:

Flask==2.0.0
Flask-WTF==1.0.0
Flask-Bootstrap==5.0.0

markdown


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **Saurav Bista**: [GitHub](https://github.com/your-username)
