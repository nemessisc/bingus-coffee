
# bingus-coffee Shop Flask Web App

Welcome to the bingus-coffee Shop! This is a simple Flask-based web application that simulates a coffee shop. Users can log in, receive a personalized greeting, and log out.

## Features

1. **Home Page** (`/` route): Displays a warm welcome message to users visiting the coffee shop.

2. **Login Page** (`/login` route): Provides a form where users can enter their username to log in.

3. **Success Page** (`/success` route): Once logged in, users are greeted with a personalized message and an invitation to enjoy coffee.

4. **Logout** (`/logout` route): Users can log out, which clears their logged-in status and redirects them to the home page.

## Installation

```bash
# Clone this repository
git clone https://github.com/yourusername/coffee-shop-app.git

# Navigate to the project directory
cd coffee-shop-app

# Install Flask (if not already installed)
pip install Flask

# Run the app
python app.py
