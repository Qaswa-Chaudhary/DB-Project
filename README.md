# Hotel Management System – Overview
The Hotel Management System is a console-based application developed using Python that facilitates seamless interaction between Employees and Guests with the hotel's core services. The application adheres to the Model-View-Controller (MVC) architectural pattern, which ensures a clear separation of concerns between data, logic, and presentation. This makes the system more maintainable, scalable, and easier to test or extend.

At the backend, the system is powered by the hotel_db database, developed in MySQL, which is responsible for managing all operational data. This includes:

Guest information

Room inventory and availability

Bookings

Payments

Service usage

Employee details
## 📂 Project Structure (MVC)
- `models/` → Database schema and data models
- `controllers/` → Business logic and processing
- `views/` → CLI output and user interaction
- `config/` → MySQL DB connection setup

## ✅ Features
### For Employees:
- View Booking Details
- View Payment History
- Check Guest Services

### For Guests:
- View Used Services
- Check Payment History

## 🧰 Tools & Technologies
- Python
- MySQL Workbench
- Lucidchart (ERD Design)
- dotenv

## 📊 SQL Features
- **DDL**: Tables, Views, Stored Procedures
- **DML**: Insert, Select, Procedure Calls
- **Views**: `GuestBookingDetails`, `PaymentHistory`, `UsedService`
- **Procedures**: `AddGuests()`, `AddPayment()`
