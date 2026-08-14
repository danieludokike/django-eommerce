# 🛒 Full-Stack Django E-Commerce Platform

A complete, production-ready E-Commerce application built with Python and Django. This project covers essential web development concepts including relational database design, session-based shopping cart management, user authentication, model forms, custom template tags, and the Django Admin panel.

---

## 📸 Core Features

- **Product & Category Catalog:** Dynamic routing by category slug, search, and stock tracking.
- **Session-Based Shopping Cart:** Guest users can add, remove, and manage cart items without logging in.
- **Order Processing & Checkout:** Complete order creation flow with shipping details and line-item snapshots.
- **User Authentication:** Registration, Login, and Logout functionality.
- **Django Admin Management:** Pre-configured admin dashboard with inline order tracking and automated slug generation.
- **Responsive UI:** Built with Bootstrap 5 for clean mobile and desktop experience.

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.10+
- **Framework:** Django 5.x
- **Database:** SQLite (Default / Development)
- **Image Processing:** Pillow
- **Frontend Framework:** Bootstrap 5 (via CDN)

---

## 🚀 Quickstart & Installation Guide

Follow these steps to set up the project on your local machine after cloning.

### 1. Clone the Repository
```bash
git clone https://github.com/danieludokike/django-eommerce.git
cd django-ecommerce
```

### 2. Set Up Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django pillow
```

### 4. Run Database Migrations
Apply the initial schema to create the database tables:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Admin)
Create an admin account to access the dashboard and add categories/products:
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your web browser.

---

## 🗂️ Project Architecture

```text
django_ecommerce/
│
├── store_config/           # Root Configuration Directory
│   ├── settings.py         # App settings, media paths, installed apps
│   ├── urls.py             # Main routing & media file handling
│   └── wsgi.py
│
├── store/                  # Main E-Commerce Application
│   ├── admin.py            # Admin UI configuration & Inlines
│   ├── cart.py             # Session-based cart object logic
│   ├── forms.py            # Checkout and User Registration forms
│   ├── models.py           # Category, Product, Order, OrderItem, ShippingAddress
│   ├── urls.py             # App-specific URL routes
│   ├── views.py            # Storefront, Cart, Checkout, Auth views
│   └── templates/          # HTML Templates
│       ├── registration/   # Login & Register templates
│       └── store/          # Storefront, Product Detail, Cart, Checkout
│
├── media/                  # Product image uploads directory
├── db.sqlite3              # Database file
└── manage.py               # Django CLI management tool
```

---

## 🎯 Post-Class Challenges (Student Tryouts)

Now that you have cloned and set up the project, test and strengthen your Django skills by attempting these progressive extension challenges!

### 🌟 Level 1: Beginner Enhancements
1. **Product Search Bar:**
   - Add a search input field in the navbar (`base.html`).
   - Create a view in `views.py` that filters products using `Product.objects.filter(name__icontains=query)`.
2. **Stock Auto-Deduction:**
   - Modify the `checkout` view so that when an order is successfully placed, the stock quantity (`product.stock`) automatically decreases by the ordered amount.
3. **Product Price Formatting:**
   - Add a custom Django template filter or method on the `Product` model to display prices with formatted currency symbols and comma separators (e.g., `$1,250.00`).

### 🚀 Level 2: Intermediate Features
4. **Order History Page for Authenticated Users:**
   - Create a new view `user_orders` protected with `@login_required`.
   - Render a template showing all past orders for `request.user` with order status and total cost.
5. **Quantity Controls in Cart:**
   - Add `+` and `-` buttons in `cart_detail.html` allowing users to increment or decrement product quantities directly inside the cart table.
6. **Product Review & Rating System:**
   - Create a `Review` model (`product`, `user`, `rating` (1-5), `comment`, `created_at`).
   - Add a review submission form on `product_detail.html` and display the average rating score.

### 🔥 Level 3: Advanced Challenges
7. **Discount / Coupon Code System:**
   - Build a `Coupon` model with code, discount percentage, active status, and expiry date.
   - Allow users to enter a coupon code during checkout and apply the percentage discount to the cart total price.
8. **Payment Gateway Integration (Paystack / Stripe):**
   - Replace the instant mock checkout with live payment processing using Paystack or Stripe webhooks before marking `order.paid = True`.

---

## 📝 License
This project is open-source and intended for educational and mentoring purposes.