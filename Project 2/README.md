# Project 2: Commerce

**Commerce** is a web-based auction platform built with Django. It allows users to list products for sale, place bids on active listings, manage personal watchlists, and browse items by category. The application follows a core auction logic similar to platforms like eBay.

This project was developed as part of the **CS50 Web Programming with Python and JavaScript** course (2020).

---

## Core Features

### User Authentication
- Register new users
- Log in and log out using Django's built-in auth system
- Session-based authentication and CSRF protection

### Listings
- Create auction listings with title, description, starting bid, optional image, and optional category
- Browse all active listings on the homepage
- Each listing has a dedicated detail page

### Bidding System
- Place a bid on any active listing
- Bids must exceed the current highest bid
- Only logged-in users can place bids
- Bidding history is shown in reverse chronological order

### Watchlist
- Add or remove listings from a personal watchlist
- View all watchlisted items in a single page

### Categories
- Assign listings to a predefined category
- Filter active listings by category

### Auction Lifecycle
- Listing owners can close auctions
- Winning bid and bidder are shown after closing
- If no bids were placed, no winner is declared

---

## Technology Stack

- **Backend**: Django 4.x / Python 3.12
- **Frontend**: HTML5, CSS3, Bootstrap 4
- **Database**: SQLite (via Django ORM)
- **Templating**: Django Templates
- **Form Handling**: Django ModelForms

---

## Setup Instructions

To run this project locally:

```bash
# Clone the repository
git clone https://github.com/your-username/commerce.git
cd commerce

# Set up and activate a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Create a superuser for admin access
python manage.py createsuperuser

# Run the development server
python manage.py runserver
