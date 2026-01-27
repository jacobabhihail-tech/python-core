# Day 25: Environment Variables & Settings Best Practices

## Tasks Completed

1. **Moved secret keys to `.env` file**
   - `SECRET_KEY` is no longer hardcoded in `settings.py`.
   - Uses `python-decouple` to read secrets safely.

2. **Configured `DEBUG` using environment variables**
   - Allows turning debug on/off without changing code.
   - Prevents accidental debug mode in production.

3. **Database settings moved to environment variables**
   - Can switch between SQLite, PostgreSQL, or other databases easily.
   - Keeps credentials secure.

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install python-decouple
