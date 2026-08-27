# Smart Pharmacy Predictive Analytics — Project Development Skill

## Project Context

You are working on an existing project called **Smart Pharmacy Predictive Analytics System**.

This is an AI and Machine Learning powered healthcare analytics platform designed to improve pharmacy inventory management. The project already contains a working prototype and should be **enhanced, not rebuilt from scratch**.

The existing system includes functionality around:

* Medicine demand forecasting using Machine Learning
* Inventory monitoring and analysis
* Low-stock and overstock identification
* Product intelligence and analytics
* Interactive dashboard and visualizations
* Inventory-related KPIs and insights
* Existing ML workflow and project architecture

The repository connected to this environment is the source of truth. Before making changes, inspect the repository carefully and understand:

1. The existing application structure
2. Current frontend/dashboard framework
3. ML models and prediction pipeline
4. Available datasets and data schema
5. Existing dependencies
6. Existing pages, modules, and functionality

Do not assume data fields or functionality that do not already exist without verifying the code and dataset.

---

## Primary Development Goal

Transform the existing prototype into a more intelligent, proactive, and polished AI-powered product while preserving all currently working functionality.

The project should remain focused on its core purpose:

> **Using predictive analytics and AI to help pharmacies make better inventory decisions, reduce stockouts and wastage, and improve medicine availability.**

Do not unnecessarily convert the project into a generic chatbot application or add unrelated AI features.

---

# MVP Features to Implement

## Feature 1: Smart Notification and Alert Center

Implement a centralized notification and alert system.

The system should generate meaningful alerts based on existing project data and analytics.

Possible alert categories include:

* Critical low-stock alerts
* Predicted future stockout alerts based on demand forecasting
* Overstock alerts
* Inventory risk alerts
* Expiry-related alerts only if expiry data already exists and supports this feature

### Requirements

* Add a visible notification bell or alert entry point
* Display unread notification count
* Support alert severity levels:

  * Critical
  * Warning
  * Information
* Allow users to view alert details
* Allow notifications to be marked as read or dismissed
* Maintain alert history where practical
* Avoid generating duplicate alerts unnecessarily
* Generate alerts dynamically from actual application data rather than hardcoded examples

The notification system should be useful and visually integrated with the existing dashboard.

---

## Feature 2: AI Pharmacy Query Assistant

Implement an AI assistant whose role is strictly limited to **answering user queries and enquiries about pharmacy data and analytics**.

The assistant must not autonomously:

* Modify inventory
* Delete data
* Change model configurations
* Execute restocking actions
* Perform irreversible actions

### Example Queries

The assistant should support questions such as:

* Which medicines are likely to run out soon?
* Why is this medicine marked as high risk?
* What products should be prioritized for restocking?
* Which medicines have overstock risk?
* What is the forecast for a selected medicine?
* Explain the demand trend.
* Which products have declining or increasing demand?
* Summarize the current inventory situation.

### Requirements

* Use actual project data whenever possible
* Ground responses in existing forecasts, inventory metrics, and analytics
* Do not hallucinate medicine statistics or predictions
* Clearly state when requested information is unavailable
* Provide concise and useful responses
* Make the assistant feel integrated into the product rather than being a generic chatbot

If an external LLM/API is required, keep the architecture modular so the provider can be changed later.

---

## Feature 3: AI Insights and Actionable Recommendations

Create an AI-powered insights section that converts analytics and ML predictions into understandable recommendations.

Examples:

* Medicines at immediate stockout risk
* Products predicted to require restocking soon
* Products with overstock risk
* Increasing or declining demand trends
* Inventory priorities
* Important anomalies or changes

### Output Format

Each insight should ideally contain:

* Insight title
* Severity or priority
* Short explanation
* Supporting data or reason
* Recommended action

Example:

**High Priority — Predicted Stockout**

Medicine X is projected to fall below the safe inventory level based on forecasted demand.

**Recommended Action:** Review and prioritize restocking.

Recommendations must be derived from actual project logic and data, not randomly generated text.

---

# Optional Feature

## Forecast vs Actual / Scan Comparison

If the existing data and architecture support it without major disruption, add a comparison capability for:

* Predicted demand versus actual demand
* Previous forecasts versus updated forecasts
* Inventory performance across time periods

This feature should help users understand forecasting accuracy and changes over time.

Do not prioritize this over the three primary MVP features.

---

# UI and Product Requirements

The application should look like one coherent product.

Follow these principles:

* Preserve the existing design language where possible
* Do not redesign working pages unnecessarily
* Avoid excessive animations
* Keep the interface professional and suitable for a healthcare analytics product
* Ensure responsive layouts
* Avoid clutter
* Make critical information easy to identify
* Use consistent components and terminology

Prioritize usability over visual complexity.

---

# Technical Requirements

Before changing the project:

1. Inspect the complete repository
2. Identify the current architecture
3. Identify the application entry point
4. Understand the existing ML pipeline
5. Inspect the dataset schema
6. Check current dependencies

While implementing:

* Reuse existing functions and data pipelines where possible
* Avoid breaking existing functionality
* Avoid hardcoding values that should come from data
* Keep new modules modular
* Add comments where logic is non-obvious
* Handle missing or incomplete data gracefully
* Avoid unnecessary dependencies
* Do not expose API keys or secrets
* Use environment variables for external API credentials if needed

---

# Validation Requirements

After implementation:

1. Run the application
2. Test every existing feature
3. Test every newly added feature
4. Verify that alerts are based on real application data
5. Verify that the AI assistant does not invent unsupported data
6. Check for broken imports and runtime errors
7. Check responsive UI behavior where practical
8. Update README documentation with the new capabilities

---

# Development Philosophy

This is an enhancement of a working prototype.

The priority is:

1. Preserve working functionality
2. Add high-impact MVP features
3. Improve intelligence and decision support
4. Maintain technical reliability
5. Avoid unnecessary feature bloat

Make practical engineering decisions based on the existing repository rather than forcing a completely new architecture.
