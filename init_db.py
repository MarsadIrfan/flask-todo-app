from app import app, db

# Create an application context
with app.app_context():
    # Create the database and tables
    db.create_all()
