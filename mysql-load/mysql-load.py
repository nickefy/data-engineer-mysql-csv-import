import mysql.connector
import time

time.sleep(60)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="mysqltest",
  allow_local_infile=True
)

mycursor = mydb.cursor()

mycursor.execute("set global local_infile = true;")
mycursor.execute("LOAD DATA LOCAL INFILE 'resources/load/places.csv' INTO TABLE mysqltest.places FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;")
mycursor.execute("LOAD DATA LOCAL INFILE 'resources/load/people.csv' INTO TABLE mysqltest.people FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS (given_name,family_name,date_of_birth,place_of_birth);")
mycursor.execute("""with cte as (
    SELECT
        country,
        count(distinct people_id) as count_of_people_born
    from mysqltest.places a
    left join mysqltest.people b on 
        a.city = b.place_of_birth 
    group by 1 
    order by 2 desc

)

select 
    concat( '{',GROUP_CONCAT(concat('"',country,'"',':', count_of_people_born)),'}') from cte
INTO OUTFILE '/var/lib/mysql-files/summary_output.json'""")


mydb.commit()
myresult = mycursor.fetchall()
