# Hospital OPD System - Basic Understanding

## Overview
This is a comprehensive Hospital Outpatient Department (OPD) Management System built in Python. It manages patient queues, bed allocation, and hospital statistics using efficient data structures and algorithms.

## What This System Does

### ✅ Core Features

1. **Add Patients to OPD Queue**
   - Patients are added with their name and medical condition
   - Automatic validation ensures data integrity
   - Each patient gets a unique 8-character ID

2. **Smart Priority-Based Queue**
   - Uses Python's `heapq` for efficient priority queue management
   - Priority levels:
     - **ICU** (Priority 1) - Highest priority
     - **Maternity** (Priority 2)
     - **Pediatrics** (Priority 3)
     - **General** (Priority 4) - Lowest priority
   - Higher priority patients are always processed first

3. **Intelligent Bed Allocation**
   - **ICU patients** → Only ICU beds
   - **General patients** → General beds OR ICU beds (if general full)
   - **Maternity patients** → Maternity beds only
   - **Pediatrics patients** → Pediatrics beds only
   - Total: 5 General + 3 ICU + 2 Maternity + 2 Pediatrics = 12 beds

4. **Process Next Patient**
   - Checks if a suitable bed is available
   - If bed available → Patient is admitted immediately
   - If no bed → Patient is moved to waiting list
   - Tracks wait time in seconds

5. **Discharge Patients**
   - Frees up beds when patients are discharged
   - Automatically admits waiting patients if beds become available
   - Updates discharge statistics

6. **Auto-Admit from Waiting List**
   - When a bed is freed, the system automatically checks the waiting list
   - Eligible patients are admitted without manual intervention
   - Maintains queue fairness

7. **Real-Time Statistics**
   - Total patients admitted
   - Total patients discharged
   - Current occupancy rate (%)
   - Waiting list count

8. **Status Display**
   - View all beds and their availability
   - See which patient occupies each bed
   - Monitor hospital capacity

## How to Use

### Running the Program
```bash
python hospital_system.py
```

### Menu Options
1. **Add Patient** - Register a new patient with name and condition
2. **Process Next Patient** - Admit the next patient from queue if bed available
3. **Discharge Patient** - Release a patient and free their bed
4. **Show Bed Status** - View all beds and occupancy
5. **Show Statistics** - View hospital performance metrics
6. **Show Admitted Patients** - List all currently admitted patients
7. **Exit** - Close the system

## Example Workflow

```
1. Add Patient: John Doe (ICU)
2. Add Patient: Jane Smith (General)
3. Add Patient: Bob Wilson (Maternity)

Process Next Patient:
   - John (ICU) is admitted to ICU1 (highest priority)
   
Process Next Patient:
   - Jane (General) is admitted to G1
   
Discharge Patient:
   - John is discharged from ICU1
   - ICU1 becomes available
   
Process Next Patient:
   - Bob (Maternity) is admitted to M1

Show Statistics:
   - Total Admitted: 3
   - Total Discharged: 1
   - Occupancy Rate: 25%
   - Waiting List: 0
```

## Key Data Structures

### Patient Class
- **id**: Unique 8-character identifier
- **name**: Patient name
- **condition**: Medical condition (icu/maternity/pediatrics/general)
- **arrival_time**: Timestamp of registration

### Bed Class
- **bed_id**: Unique bed identifier (G1, ICU1, M1, P1, etc.)
- **bed_type**: Type of bed (general/icu/maternity/pediatrics)
- **occupied_by**: Reference to occupying patient (or None if available)

### HospitalSystem Class
- **opd_queue**: Priority queue using heapq
- **waiting_list**: List of patients without available beds
- **beds**: List of all hospital beds
- **admitted_patients**: Dictionary of current admitted patients
- **Statistics**: Track total admitted, discharged, and occupancy

## Technical Highlights

- **Efficient Priority Queue**: O(log n) insertion and removal using heapq
- **Optimal Bed Matching**: Finds suitable beds in O(n) time
- **Automatic Waiting List Processing**: Reduces manual intervention
- **UUID Generation**: Ensures unique patient IDs
- **Real-Time Metrics**: Instant occupancy and performance tracking

## Benefits

✅ Reduces patient wait times
✅ Optimizes bed utilization
✅ Prioritizes critical cases
✅ Easy to track and manage
✅ Scalable and maintainable code
