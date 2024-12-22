# Restaurant Kitchen Manager

Welcome to the **Restaurant Kitchen Manager**! This Django-based web application allows restaurant managers to efficiently manage their kitchen operations, including handling dishes, dish types, and cooks. Streamline your kitchen management processes with an intuitive and user-friendly interface.

## 📌 Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Demo

Experience the Restaurant Kitchen Manager in action! Visit the live website:

🔗 [Restaurant Kitchen Manager](https://restaurant-kitchen-manager.onrender.com)

Use the following credentials to log in as a test user:

- **Login URL:** `https://restaurant-kitchen-manager.onrender.com/accounts/login/`
- **Username:** `user`
- **Password:** `user`

## Features

- **User Authentication**
  - Register as a cook.
  - Secure login and logout functionalities.
- **Dish Management**
  - Create, view, update, and delete dishes.
  - Assign multiple cooks to a dish.
- **Dish Type Management**
  - Organize dishes by types (e.g., Soup, Cake, Pasta).
- **Cook Management**
  - View detailed information about each cook, including their experience and assigned dishes.
- **Search and Filtering**
  - Search for dishes by name.
  - Filter dishes by dish type.
- **Responsive Design**
  - Built with Bootstrap for a seamless experience across devices.

## Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/zaietsmo/restaurant-manager.git
cd restaurant-manager
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **macOS and Linux:**

  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory of the project and add the necessary environment variables. Here's an example of what the `.env` file might look like:

```env
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

**Note:** Replace `your-secret-key` with a secure secret key. In a production environment, ensure that `DEBUG` is set to `False` and configure `ALLOWED_HOSTS` appropriately.

### 5. Apply Migrations

Create the necessary database tables:

```bash
python manage.py migrate
```

### 6. Load Initial Data (Optional)

If you have a fixture (`dump.json`) with initial data, you can load it using:

```bash
python manage.py loaddata dump.json
```

### 7. Create a Superuser (Optional)

To access the Django admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your superuser account.

### 8. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to access the application.

## Usage

Once the development server is running, navigate to the live site or your local server address. You can perform the following actions:

- **Register as a Cook:** Create a new cook account.
- **Login:** Access the dashboard with your credentials.
- **Manage Dishes:** Add, edit, view, or delete dishes.
- **Manage Dish Types:** Organize dishes by their types.
- **View Cooks:** See information about each cook and their assigned dishes.


## Technologies Used

- **Backend:**
  - [Django](https://www.djangoproject.com/) - Python web framework.
- **Frontend:**
  - [Bootstrap](https://getbootstrap.com/) - CSS framework for responsive design.
- **Database:**
  - [SQLite](https://www.sqlite.org/index.html) (default) or [PostgreSQL](https://www.postgresql.org/) (if configured).
- **Others:**
  - [Gunicorn](https://gunicorn.org/) - WSGI HTTP server for UNIX.
  - [Whitenoise](http://whitenoise.evans.io/en/stable/) - For serving static files.
  - [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) - For enhanced form rendering.
  - [python-dotenv](https://github.com/theskumar/python-dotenv) - For managing environment variables.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. **Fork the Repository**

2. **Create a New Branch**

   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Make Changes and Commit**

   ```bash
   git commit -m "Add some feature"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeatureName
   ```

5. **Open a Pull Request**

Provide a clear description of your changes and the benefits they bring.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or support, feel free to reach out:

- **Email:** mykola.oleksandr.zaiets@gmail.com
- **GitHub:** [zaietsmo](https://github.com/zaietsmo)

---

**Enjoy managing your restaurant kitchen efficiently!**
