📊 Sales & Customer Analytics with dbt + DuckDB
🚀 Project Overview

This project demonstrates how to build a modern data analytics pipeline using:

dlt
 → extract & load data from public APIs

DuckDB
 → lightweight analytical database

dbt
 → transform and model raw data into analytics-ready datasets

We use the Platzi Fake Store API as our data source, loading entities like:

Users

Products

Categories

and (optionally) generating synthetic orders/carts for analytics practice.

🛠️ Tech Stack

Python + dlt → data ingestion from APIs

DuckDB → local OLAP database (data warehouse-in-a-file)

dbt-duckdb → transformations, staging, marts

VSCode dbt Power User extension → IDE support

GitHub → version control, collaboration
