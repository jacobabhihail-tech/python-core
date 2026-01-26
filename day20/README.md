# 📅 Day 20 – Django Admin Panel & Permissions

## ✅ What was covered

On Day 20, we focused on working with the **Django Admin Panel** and learned how to manage data efficiently from the backend.

---

## 🚀 Features Implemented

### 1️⃣ Django Admin Setup
- Created and used a **superuser**
- Logged into Django Admin (`/admin`)
- Managed app models from the admin panel

### 2️⃣ Admin Model Customization
Customized the `Expense` model using `ExpenseAdmin`:
- `list_display` – show fields in admin table
- `list_filter` – filter records easily
- `search_fields` – search expenses by name
- `ordering` – sort expenses by latest first

```python
ordering = ('-created_at',)
