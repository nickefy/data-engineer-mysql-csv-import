# MYSQL CSV IMPORT

This section of the repository contains the resources and code to load the CSV files provided. The pipeline will then produce a summary of the database to summary_output.json file.
Docker was used in this project.

# Install and Run the Project 

1. Install Docker as per instructions here - https://docs.docker.com/engine/install/
2. Clone the project 
3. Remove the ./mysql/resources/data/summary_output.json file
4. Run 'docker compose up' in the terminal
5. Validate the summary_output.json file

# Files and Folder Structure
- docker-compose.yaml: Contains configurations for the docker compose file
- mysql: mysql service to spin up MySQL database and create necessary schema from the CSV files
- mysql-load: python service to load CSV files into MySQL Database and Output a summary json file to the determined filepath
- .png and readme: Explaination and Documentation for the project

# Extra
Diagram to visualize Pipeline Logic.

The projects starts by deploying a MySQL Database container using the MySQL parent image from Docker. It then creates the necessary schema from the CSV files provided. The python service will then load the CSV data into the MySQL Database and outputs the output_summary.json file using SQL query in ./mysql-load/resources/sample_output.sql.


![Diagram to visualize Pipeline Logic](mysql-csv-import.png?raw=true "Data Pipeline Logic")

* Successfully processed summary_output.json file can be found in ./mysql/resources/data/summary_output.json 