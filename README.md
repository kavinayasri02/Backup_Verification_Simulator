# 🛡Backup Verification Simulator

## Overview

The Enterprise Backup Verification System is a Python-based application designed to verify the integrity and consistency of backup files. The system compares original data files with backup files and provides a visual dashboard for monitoring backup verification activities.

This project demonstrates how organizations can ensure that their backup data remains reliable and recoverable in case of system failures, data corruption, or accidental data loss.

---

## Problem Statement

Many organizations create backups regularly but often fail to verify whether the backups are valid and usable.

Common challenges include:

* Corrupted backup files
* Incomplete backup processes
* Data inconsistencies
* Lack of monitoring dashboards
* Manual verification effort

This project provides an automated solution to address these challenges.

---

## Objectives

* Automate backup verification.
* Compare original and backup files.
* Detect mismatches and integrity issues.
* Provide a user-friendly dashboard.
* Generate verification results instantly.
* Improve backup monitoring efficiency.

---

## Features

### Dashboard

* System health monitoring
* Verification progress tracking
* Backup statistics overview
* Real-time status updates

### Backup Verification

* Upload Original File
* Upload Backup File
* Compare backup integrity
* Detect mismatches automatically

### Analytics

* Total Backups
* Verified Backups
* Failed Backups
* Success Rate
* Storage Utilization

### Alert Center

* Verification alerts
* Backup failure notifications
* System monitoring logs

### User Interface

* Dark Theme Dashboard
* Enterprise Style Layout
* Sidebar Navigation
* Interactive Components

---

## Technology Stack

### Frontend

* CustomTkinter

### Backend

* Python

### Libraries

* customtkinter
* os
* datetime
* tkinter

---

## Project Structure

```text
backup_verification/
│
├── main.py
├── ui.py
├── README.md
├── requirements.txt
│
├── agent/
│   ├── __init__.py
│   ├── backup_agent.py
│   ├── backup.py
│   └── validator.py
│
├── llm/
│   ├── __init__.py
│   └── narrator.py
│
├── data/
│   └── backups/
│
└── prompts/
```

## Module Description

### main.py

Entry point of the application.

Responsibilities:

* Launch application
* Initialize verification process
* Connect UI with backend

### ui.py

Graphical User Interface.

Responsibilities:

* Dashboard
* Upload Files
* Analytics View
* Alerts View
* Verification Results

### backup.py

Handles backup file operations.

Responsibilities:

* Read backup files
* Manage backup repository
* Process uploaded files

### validator.py

Performs validation logic.

Responsibilities:

* Compare files
* Detect mismatches
* Verify backup integrity

### backup_agent.py

Controls verification workflow.

Responsibilities:

* Coordinate modules
* Execute verification cycle
* Generate system responses

### narrator.py

Provides result summaries.

Responsibilities:

* Generate verification messages
* Produce human-readable output

---

## Workflow

```text
Upload Original File
          │
          ▼
Upload Backup File
          │
          ▼
Start Verification
          │
          ▼
Compare Files
          │
          ▼
Generate Result
          │
          ▼
Update Dashboard
          │
          ▼
Display Alerts & Analytics
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/jemimoses/Backup_Verification.git
```

### Move Into Project Folder

```bash
cd Backup_Verification
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## Sample Verification Process

### Successful Verification

Original File:

```
backup1.zip
```

Backup File:

```
backup1.zip
```

Result:

```
MATCHED
```

### Failed Verification

Original File:

```
backup1.zip
```

Backup File:

```
backup2.zip
```

Result:

```
MISMATCH FOUND
```

---

## Future Enhancements

* SHA-256 Hash Verification
* Real-Time Monitoring
* Cloud Backup Support
* Database Backup Validation
* Email Notifications
* PDF Report Generation
* Backup Scheduling
* AI-Based Anomaly Detection
* Multi-User Access Control

---

## Real World Applications

* Banking Systems
* Healthcare Records
* Enterprise Data Centers
* Cloud Infrastructure
* Educational Institutions
* Government Data Repositories

---

## Team Contribution

This project was developed as an academic project to demonstrate enterprise backup monitoring and verification concepts using Python and CustomTkinter.

## Demo video link
Link 1 - https://kavinayasri02.github.io/Demo-video/
Link 2 - https://drive.google.com/drive/folders/1HlbK_JxQc2SFkYAU1dKZog-eJESWLV2D?usp=sharing
---
## Application Link
https://backup-verification-simulator-1.onrender.com/


## Conclusion

The Enterprise Backup Verification System provides a simple yet effective solution for validating backup integrity. The application reduces manual effort, improves reliability, and offers a professional dashboard for monitoring backup verification activities.
