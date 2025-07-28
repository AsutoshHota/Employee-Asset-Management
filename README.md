# Project Overview 
Employee Asset Management is a custom Odoo 16 module designed to help companies efficiently manage assets issued to employees. It provides HR with the ability to assign, track, and reclaim assets such as laptops, phones, and ID cards.

The module includes full integration with Odoo’s HR system and provides a user-friendly interface for viewing, updating, and managing asset lifecycle events. The system enforces role-based access control, supports workflow states (e.g., assigned, returned, lost), and is structured using best practices in Odoo development.

It covers core components of Odoo’s architecture including models, views, access controls, workflows, and business logic, making it a complete, modular asset management solution.

# Feature Overview
The module provides a clean interface for managing company-issued assets assigned to employees:

 Asset Model with:

Name, Type, Serial Number, Condition, Purchase Date

Assigned Employee, Assignment Date, Return Date, Status (draft, assigned, returned, lost)

 Access Control:

HR/Manager can assign and reclaim assets

Employees can view only their own assigned assets

 Views:

Tree, Form, and Kanban views

Filters for Asset Condition and Assigned Employee

Smart buttons to mark an asset as Returned or Lost

 Menus:

Main menu: Assets

Submenus: All Assets, My Assets

 Business Workflow:

Auto-set state and assignment date on asset assignment

Update return date and state on return

Prevent double assignment without return
