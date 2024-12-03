import os
import sqlite3
from sqlalchemy import text

def apply_sqlite_migrations(engine, model_base, migrations_dir):
    """Apply SQLite migrations to database"""
    try:
        # Create migrations directory if needed
        if not os.path.exists(migrations_dir):
            os.makedirs(migrations_dir)
        
        # Get database connection
        with engine.connect() as conn:
            # Create migrations table using SQLAlchemy text()
            migrations_table = text('''
                CREATE TABLE IF NOT EXISTS migrations (
                    id INTEGER PRIMARY KEY, 
                    name TEXT, 
                    applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.execute(migrations_table)
            conn.commit()
            
            # Create initial schema
            model_base.metadata.create_all(engine)
            
    except Exception as e:
        print(f"Error during migration: {str(e)}")
        raise