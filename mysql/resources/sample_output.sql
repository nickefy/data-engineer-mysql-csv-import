with cte as (
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
INTO OUTFILE '/var/lib/mysql-files/summary_output.json'