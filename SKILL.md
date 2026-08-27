---

name: Smart Pharmacy Predictive Analytics Enhancement
description: Enhance an existing AI-powered pharmacy analytics prototype with proactive alerts, a grounded AI query assistant, and actionable inventory insights while preserving the existing architecture and functionality.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Smart Pharmacy Predictive Analytics Enhancement Skill

## Project Context

You are working on an existing project called **Smart Pharmacy Predictive Analytics System**.

This is an AI and Machine Learning-powered healthcare analytics platform designed to improve pharmacy inventory management through predictive analytics and data-driven decision support.

This is an **existing working prototype**. Your responsibility is to understand and enhance it, not rebuild the entire project from scratch.

The repository is the primary source of truth. Before making any changes, inspect the existing:

* Application structure
* Entry points
* Frontend or dashboard framework
* Machine learning models
* Prediction pipeline
* Datasets and available data schema
* Existing pages and modules
* Dependencies
* Current functionality
* README and project documentation

Do not assume that a data field, API, model, or feature exists without verifying it in the repository.

---

# Core Project Purpose

The system aims to help pharmacies make better inventory decisions using:

* Machine learning-based demand forecasting
* Inventory monitoring
* Product-level analytics
* Stock risk identification
* Data visualization
* Predictive insights
* Intelligent decision support

The enhanced product should remain focused on this core objective.

> Transform the existing analytics prototype into a more proactive and intelligent pharmacy decision-support platform.

Do not turn the project into a generic chatbot application or unnecessarily replace the existing architecture.

---

# Primary MVP Features

Implement the following features in priority order.

## 1. Smart Notification and Alert Center

Create a centralized alert and notification system that makes the application proactive.

The system should generate meaningful alerts from actual project data, forecasts, and inventory analytics.

Possible alert types include:

* Critical low-stock alerts
* Predicted future stockout alerts
* Overstock alerts
* Inventory risk alerts
* Significant demand changes
* Other meaningful anomalies supported by the existing data

Only implement expiry-related alerts if the existing dataset genuinely contains sufficient expiry information.

### Required Functionality

* Add a visible notification bell or alert entry point
* Display an unread alert count
* Support alert severity levels:

  * Critical
  * Warning
  * Information
* Allow users to view alert details
* Allow alerts to be marked as read
* Allow alerts to be dismissed where appropriate
* Maintain alert history if practical within the current architecture
* Avoid unnecessary duplicate alerts
* Generate alerts dynamically from real project data

Do not use hardcoded fake alerts as the main implementation.

### Product Goal

The notification system should answer:

> What requires the pharmacy's attention right now?

---

## 2. Grounded AI Pharmacy Query Assistant

Add an AI assistant dedicated to answering user queries and enquiries about the pharmacy's data and analytics.

The assistant is an information and decision-support feature only.

### The Assistant Can Answer Questions Such As

* Which medicines are likely to run out soon?
* What products should be prioritized for restocking?
* Why is a particular medicine considered high risk?
* Which medicines currently have overstock risk?
* What is the predicted demand for a selected medicine?
* Explain this demand forecast.
* Which products show increasing demand?
* Which products show declining demand?
* Summarize the current inventory situation.
* What are the most important inventory risks right now?

### Critical Constraints

The AI assistant must not autonomously:

* Modify inventory data
* Delete records
* Change model configurations
* Execute restocking actions
* Perform destructive or irreversible actions

It should only provide answers, explanations, insights, and recommendations.

### Grounding Requirements

Prioritize actual project data.

The assistant should use available:

* Forecast results
* Inventory metrics
* Product information
* Alerts
* Risk indicators
* Dashboard analytics

Do not hallucinate product statistics, demand values, stock levels, or predictions.

If requested information is unavailable, clearly say that the information is not available in the current project data.

Keep the implementation modular so that any external AI or LLM provider can be replaced later.

---

## 3. AI Insights and Actionable Recommendations

Create a dedicated insights section that converts existing analytics and ML predictions into clear business actions.

The project should not only display charts and predictions. It should help the user understand:

> What happened, why it matters, and what should be done next.

### Possible Insights

Generate insights from real data such as:

* Medicines requiring immediate attention
* Products predicted to face stockout
* High-priority restocking candidates
* Products with overstock risk
* Significant increases in demand
* Significant decreases in demand
* Important inventory anomalies
* Changes in inventory risk

### Every Insight Should Ideally Include

* Title
* Priority or severity
* Short explanation
* Supporting reason or relevant data
* Recommended action

### Example Structure

**High Priority — Predicted Stockout**

A product is projected to fall below the safe inventory level based on forecasted demand.

**Why:** Forecasted demand is expected to exceed the available stock threshold.

**Recommended Action:** Review and prioritize restocking.

Do not randomly generate generic recommendations. Insights must be connected to actual project logic and available data.

---

# Optional Feature

## Forecast vs Actual Comparison

Only implement this after the three primary MVP features are stable.

If the existing data supports it naturally, provide a comparison capability for:

* Predicted demand versus actual demand
* Forecast performance over time
* Previous versus updated predictions
* Model prediction accuracy where actual data is available

This feature should improve transparency and trust in the forecasting system.

Do not fabricate historical comparison data.

Do not prioritize this feature over Alerts, AI Assistant, and AI Insights.

---

# Existing Functionality Protection

The project already contains working functionality.

Before modifying the code:

1. Identify all existing features.
2. Understand their dependencies.
3. Reuse existing data pipelines where possible.
4. Avoid unnecessary rewrites.
5. Preserve existing working ML functionality.
6. Preserve useful existing dashboard pages.

After implementing new features, verify that existing functionality still works.

Do not remove features merely to simplify implementation unless there is a genuine technical reason.

---

# UI and Product Design Requirements

The final application should feel like one cohesive product.

Follow these principles:

* Preserve the existing design language where practical.
* Improve rather than unnecessarily redesign working pages.
* Keep the interface clean and professional.
* Avoid excessive animations.
* Avoid clutter.
* Make critical information easy to identify.
* Use consistent terminology.
* Ensure responsive layouts where practical.
* Clearly distinguish critical alerts from normal information.
* Make the AI features useful without overwhelming the dashboard.

The product should look suitable for a modern healthcare analytics and decision-support platform.

---

# Technical Development Rules

Before implementation:

* Inspect the complete repository.
* Understand the existing architecture.
* Identify the application entry point.
* Inspect the dataset schema.
* Understand the ML workflow.
* Review existing dependencies.

During implementation:

* Reuse existing functions and components where possible.
* Keep new features modular.
* Avoid unnecessary dependencies.
* Avoid hardcoding values that should be calculated from data.
* Handle missing or incomplete data gracefully.
* Add comments for non-obvious logic.
* Do not expose API keys or secrets.
* Use environment variables for external credentials.
* Maintain backward compatibility where practical.

---

# Implementation Workflow

Follow this sequence:

## Phase 1 — Inspect

Carefully inspect the entire repository and understand:

* What already works
* How the ML pipeline works
* How data flows through the application
* Which data is available
* Which features already exist

## Phase 2 — Plan

Before making major changes, identify:

* Files likely to require modification
* New modules or components required
* Dependencies needed
* Potential risks to existing functionality

Create a concise implementation plan.

## Phase 3 — Implement

Implement features in this order:

1. Smart Notification and Alert Center
2. Grounded AI Pharmacy Query Assistant
3. AI Insights and Actionable Recommendations
4. Optional Forecast vs Actual Comparison

Do not jump to lower-priority features before the previous features are stable.

## Phase 4 — Test

Test:

* All existing functionality
* Notification generation
* Alert severity and duplicate handling
* AI query responses
* Data grounding
* Insight generation
* Imports and dependencies
* Runtime errors
* UI integration

Fix regressions before considering the work complete.

## Phase 5 — Document

Update the README with:

* New features
* Setup instructions
* Required environment variables
* External AI provider setup if applicable
* How to run the application

---

# Success Criteria

The enhancement is successful when the project clearly evolves from a primarily reactive analytics dashboard into a proactive AI-powered decision-support system.

The final product should allow a user to:

1. See what requires immediate attention through alerts.
2. Ask questions about actual pharmacy data.
3. Understand forecasts and inventory risks.
4. Receive actionable recommendations.
5. Continue using all important existing functionality.

---

# Development Philosophy

Prioritize:

1. Reliability
2. Preservation of existing functionality
3. High-impact MVP features
4. Data-grounded AI
5. Clear decision support
6. Clean implementation

Avoid:

* Feature bloat
* Unnecessary architecture rewrites
* Generic AI features without purpose
* Hardcoded fake analytics
* Hallucinated data
* Autonomous destructive actions

Make practical engineering decisions based on the actual repository and existing project architecture.
