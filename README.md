# Shopping Data Engineering Project

This is an end-to-end data engineering project built using Python, PostgreSQL, dbt, Airflow, and Docker.

## Overview
The pipeline takes a shopping trends CSV dataset, loads it into a PostgreSQL raw table, transforms it into staging and mart layers using dbt, and orchestrates the workflow using Airflow.

## Tech Stack
- Python
- PostgreSQL
- dbt
- Airflow
- Docker

## Pipeline Flow
1. Load CSV into PostgreSQL raw layer
2. Transform raw data into staging layer using dbt
3. Build mart outputs for analytics
4. Run the pipeline with Airflow

## Project Structure
- `scripts/` → Python ingestion script
- `dbt/` → dbt project
- `airflow/` → Airflow DAG and Docker setup
- `postgres/` → PostgreSQL Docker setup
- `docs/` → optional screenshots or supporting docs

## Main Outputs
- `raw2.customer_shopping_trends`
- `analytics2.stg_customer_shopping_trends`
- `analytics2.mart_sales_by_category`
- `analytics2.mart_sales_by_location`

## Notes
This repository does not include secrets such as real passwords or local environment-specific files.
