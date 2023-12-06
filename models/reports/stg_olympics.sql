with olympics_cte as (
SELECT 
team, sport,  count(case when medal = 'NA' then 0 else 1 end) total_medals
 FROM ahmedsharif_test.olympics_history
 group by 1,2)
 select * from olympics_cte
