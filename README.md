# Project Overview 
Employee Asset Management is a custom Odoo 16 module designed to help companies efficiently manage assets issued to employees. It provides HR with the ability to assign, track, and reclaim assets such as laptops, phones, and ID cards.

The module includes full integration with Odoo’s HR system and provides a user-friendly interface for viewing, updating, and managing asset lifecycle events. The system enforces role-based access control, supports workflow states (e.g., assigned, returned, lost), and is structured using best practices in Odoo development.

It covers core components of Odoo’s architecture including models, views, access controls, workflows, and business logic, making it a complete, modular asset management solution.


# Feature Overview
The employee_asset_management module includes the following features:

# Asset Model
- Fields: Name, Asset Type, Serial Number, Purchase Date, Condition, Assigned Employee, Assignment Date, Return Date, State
- Asset Types: Laptop, Phone, ID Card, etc.
- Condition States: New, Good, Needs Repair, Broken
- Workflow States: draft → assigned → returned/lost

 # Access Rights
- HR/Managers: Can assign and reclaim assets
- Employees: Can view only their own assigned assets

# Views
- Tree, Form, and Kanban Views for assets
- Filters: By asset condition and assigned employee
- Smart Buttons: Mark asset as returned or lost

# Business Logic
- Automatically sets asset state to assigned on assignment
- Sets return date and changes state to returned when returned
- Prevents re-assignment of already-assigned assets without a return

# Menu Structure
- Top-level menu: Assets
- Submenu: All Assets
- Submenu: My Assets (filtered by current user)

