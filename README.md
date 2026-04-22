# Shopping Data Engineering Project

An end-to-end data engineering project built with **Python**, **PostgreSQL**, **dbt**, **Airflow**, and **Docker**.

This project demonstrates a complete data pipeline, starting from raw CSV ingestion, continuing through data transformation, and ending with orchestration using Airflow.

---

## Project Overview

The goal of this project is to build a simple but complete data engineering workflow using a shopping trends dataset.

The pipeline performs the following steps:

1. Load a CSV dataset into a PostgreSQL **raw** table using Python.
2. Transform the raw data into a clean **staging** layer using dbt.
3. Build **mart** models for analytics and dashboard-ready outputs.
4. Orchestrate the pipeline with Airflow running in Docker.

This project is designed as a beginner-friendly but practical implementation of a modern data stack.

---

## Tech Stack

- **Python** for ingestion
- **PostgreSQL** for data storage
- **dbt** for transformation
- **Airflow** for orchestration
- **Docker** for containerized services
- **DBeaver** for database inspection and validation

---

## Dataset

This project uses a shopping trends dataset containing customer and transaction-related attributes such as:

- age
- gender
- item purchased
- category
- purchase amount
- location
- season
- color
- size
- payment method
- shipping type
- previous purchases
- review rating
- subscription status
- discount applied
- promo code used
- frequency of purchases

---

## Pipeline Architecture

```text
CSV File
   ↓
Python Ingestion Script
   ↓
PostgreSQL Raw Layer
   ↓
dbt Staging Model
   ↓
dbt Mart Models
   ↓
Airflow Orchestration

---
## Data Layers

1. Raw Layer

The raw layer stores the ingested CSV data in PostgreSQL with minimal transformation.

Main raw table: raw2.customer_shopping_trends

2. Staging Layer

The staging layer standardizes the raw data by:

cleaning column names
casting data types
normalizing text values
preparing data for downstream transformations

Main staging model: analytics2.stg_customer_shopping_trends

3. Mart Layer

The mart layer provides analytics-ready outputs for reporting and dashboard use.

Main mart models:

analytics2.mart_sales_by_category
analytics2.mart_sales_by_location

--
## Airflow Orchestration

The pipeline is orchestrated using Airflow with the DAG:

shopping_pipeline

Main tasks:

load_raw
run_dbt

The DAG is currently configured with:

schedule = None

This means the pipeline is triggered manually for development and testing purposes.
It can be easily changed to a scheduled DAG later.

--
## Main Components
### Python Ingestion Script

The Python script:

reads the CSV file
connects to PostgreSQL
creates the raw schema if needed
refreshes the raw table contents

File: scripts/load_csv_to_db.py

### dbt Models

dbt is used to create:

a staging model for cleaning and standardization
mart models for analytical outputs

Location: dbt/shopping_dbt/

### Airflow

Airflow is used to orchestrate the pipeline so that:

raw ingestion runs first
dbt transformation runs second

Location: airflow/dags/shopping_pipeline.py

### PostgreSQL

PostgreSQL is used as the main data warehouse/storage layer for:

raw tables
staging views/tables
mart views/tables

Location: postgres/docker-compose.yml

--
## Pipeline Execution Flow

The pipeline is executed in the following order:

### Step 1: Raw Ingestion

The ingestion script reads the CSV file and loads it into:

raw2.customer_shopping_trends

### Step 2: dbt Staging Transformation

dbt reads from the raw table and creates:

analytics2.stg_customer_shopping_trends

### Step 3: dbt Mart Transformation

dbt creates analytical outputs such as:

analytics2.mart_sales_by_category
analytics2.mart_sales_by_location

### Step 4: Airflow Orchestration

Airflow coordinates the order of execution using the DAG:

shopping_pipeline

--
## Outputs

The pipeline produces the following outputs:

### Raw Output
raw2.customer_shopping_trends
### Staging Output
analytics2.stg_customer_shopping_trends
### Mart Outputs
analytics2.mart_sales_by_category
analytics2.mart_sales_by_location

--
## Screenshots
### Airflow DAG Run
<img width="1600" height="825" alt="image" src="https://github.com/user-attachments/assets/25ad87b3-9dc8-472a-8317-8c738c7608b6" />

<img width="1600" height="903" alt="image" src="https://github.com/user-attachments/assets/71543864-c9e6-4283-87d8-d020447f2c79" />

### Dbeaver
<img width="392" height="271" alt="image" src="https://github.com/user-attachments/assets/dba0a4c4-dee2-43d6-b392-0bc836a95739" />

<img width="754" height="645" alt="image" src="https://github.com/user-attachments/assets/9456f171-e9dc-4a7a-8b73-361af9c647c4" />

### Visual Studio Code
<img width="1373" height="790" alt="image" src="https://github.com/user-attachments/assets/9d344d9b-6b95-4212-a3db-3eb7d76542cd" />

--
## What I Learned

Through this project, I practiced:

loading CSV data into PostgreSQL
organizing data into raw, staging, and mart layers
writing dbt models for transformation
orchestrating a data pipeline with Airflow
working with Docker-based services
debugging file path, dependency, and container issues
understanding the interaction between host machine, Docker containers, and database services

--
Author

Winona Thea

This project was created as a hands-on practice project to learn and demonstrate end-to-end data engineering concepts
