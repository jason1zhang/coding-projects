# DataEngine

## Overview

DataEngine is a Python project designed to process and analyze data from various sources. It includes functionality for reading data, processing SQL queries, building tables and more.

Originally it is written to hanle the surging volume of user behavior data at certain e-commerce platform. Traditional SQL queries fell short, especially when spanning extended time periods. By systematically breaking down and optimizing data processing logic, this tool efficiently managed vast datasets (over PB on the daily basis), overcoming the platform's constraints and enabling seamless operations.

## Installation

## Usage

```bash

You can use the TableDataEngine class in your Python scripts:

from TableDataEngine import TableDataEngine

# Create an instance of TableDataEngine
engine = TableDataEngine(client, start_date, end_date)

# Process a query configuration
engine.process_query_config(query_name, query_config)

```

## Notes
Run the following SQL commands for the target table.
   CONVERT TO DELTA P_DATA_T.SRP_AC;
   ALTER TABLE P_DATA_T.SRP_AC ADD COLUMN last_modified_ts TIMESTAMP;