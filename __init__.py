"""
Welcome to the documentation for the CORDS ML Model Management API!

## Introduction

The ML Model Management API is an API (Application Programming Interface) designed to manage and track machine learning artifacts. This API facilitates the storage, retrieval, and management of artifacts generated during the machine learning workflow, particularly those produced by ML Flow. It also manages semantic descriptions of these ML artifacts to enhance understanding and usability.

## Key Functionality

The ML Model Management API provides the following functionality:

1. Manage ML Artifacts:
  * Create new entries for ML artifacts
  * Update existing ML artifact entries
  * Delete ML artifact entries
  * Retrieve and view all ML artifact entries
2. Semantic Management:
  * Add semantic descriptions to artifacts
  * Update semantic descriptions
  * Query artifacts based on semantic descriptions
3. Integration with ML Flow:
  * Automatically track and store artifacts generated by ML Flow
  * Retrieve artifacts linked to specific ML Flow runs

## Key Modules

This project is written using Python 3.10.1.

The project utilizes the following modules:

* **Flask**: A micro-framework for web application development, which includes dependencies such as:
  * **click**: A package for creating command-line interfaces (CLI)
  * **itsdangerous**: A library to cryptographically sign your data and files
  * **Jinja2**: A templating engine for Python
  * **MarkupSafe**: Provides XML/HTML markup safe strings
  * **Werkzeug**: A set of utilities for creating WSGI-compatible web applications
* **APIFairy**: An API framework for Flask that enhances API creation and documentation, including:
  * **Flask-Marshmallow**: Integration of Flask and Marshmallow for object serialization and deserialization
  * **Flask-HTTPAuth**: Provides simple HTTP authentication support
  * **apispec**: Generates API specifications that are compliant with the OpenAPI specification
* **pytest**: A robust framework for testing Python applications

This API is essential for teams involved in machine learning projects, facilitating efficient management and documentation of ML artifacts.
"""
