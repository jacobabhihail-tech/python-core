# Expense Tracker — Day 27

## 📅 Day 27: Debugging & Logging

### What I Learned Today

1. **Debug Mode (`DEBUG`)**
   - When `DEBUG=True`, Django shows detailed error pages in the browser.
   - Useful for development to find errors quickly.
   - Never leave it `True` in production environments.

2. **Debug Output**
   - Using `print()` is simple but temporary.
   - `logging` is structured, persistent, and configurable.
   - Debug logs can show:
     - Files loaded by Django
     - API requests/responses
     - Errors and warnings

3. **Logging Basics**
   - Imported with `import logging` and configured in `settings.py`.
   - Levels of logging:
     - `logger.debug()` → detailed info for debugging
     - `logger.info()` → general information, like user actions
     - `logger.warning()` → potential issues
     - `logger.error()` → actual errors
     - `logger.critical()` → critical failures

4. **Example Usage in Views**
```python
import logging

logger = logging.getLogger(__name__)

def home(request):
    logger.debug("Home page accessed")
    logger.info(f"User {request.user} viewed the home page")
    return render(request, 'expenses/home.html')
