# Ops Triage Automation

Part 2 submission for the KSEYE Junior Software Developer assessment  
(Option A: Workflow Automation Script).

## Overview
This project provides a small, maintainable Python utility that processes a list of operational requests (“tickets”) stored in a JSON file. It demonstrates basic workflow automation using clear, explainable rules and a simple command-line interface (CLI).

The tool supports:
- Flagging **overdue** tickets based on SLA hours
- Categorising tickets using keyword-based rules
- Filtering and searching tickets by category via the CLI

## Project Structure
```
data/
tickets.json # Example ticket dataset
src/
main.py # CLI entry point
overdue.py # SLA / overdue logic
category.py # Categorisation + filtering logic
```

## How It Works
- Tickets are loaded from `data/tickets.json`
- Overdue tickets are identified using:
  - `created_at` timestamp
  - `sla_hours` threshold
- Ticket messages are categorised using simple keyword rules  
  (e.g. `EMAIL_CHANGE`, `NEW_STARTER_ACCESS`)
- The CLI allows a user to choose between:
  1) Timeline search (overdue tickets)
  2) Category search (including `ALL`)

## Running the Script
From the project root:

```bash
python src/main.py
```

## Design Decisions
Rule-based categorisation was chosen over ML/AI for transparency and maintainability

Logic is split into modules to reduce coupling and improve readability

The script is read-only and does not modify ticket data

## Possible Extensions
Output results to CSV or JSON report files

Add validation rules (missing fields, invalid timestamps)

Add unit tests for categorisation and overdue logic

Replace the CLI with a basic web interface