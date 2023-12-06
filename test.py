# SELECT x.Amount 
# FROM   (SELECT amount, 
#                Count(1) OVER (partition BY 'A')        AS TotalRows, 
#                Row_number() OVER (ORDER BY Amount ASC) AS AmountOrder 
#         FROM   facttransaction ft) x 
# WHERE  x.AmountOrder = Round(x.TotalRows / 2.0, 0)  



# select x.min_score min, x.median median, x.max_score max 
# FROM   (SELECT min(score) min_score, max(score) max_score, COALESCE(score,0) median, 
#                Count(1) OVER (partition BY 'A')        AS TotalRows, 
#                Row_number() OVER (ORDER BY score ASC) AS scoreOrder 
#         FROM   result ft) x 
# WHERE  x.scoreOrder = Round(x.TotalRows / 2.0, 0);



# SELECT x.min_score min, x.score as median, x.max_score as max
# FROM   (SELECT score, 
#                min(score) OVER (partition BY 'A') as min_score,
#                max(score) OVER (partition BY 'A') as max_score,
#                Count(1) OVER (partition BY 'A')        AS TotalRows, 
#                Row_number() OVER (ORDER BY score ASC) AS ScoreOrder 
#         FROM   scores ft) x 
# WHERE  x.ScoreOrder = Round(x.TotalRows / 2.0, 0)  

"""
Write a query that displays the top 5 rolls by net profit (qty_sold * (price - cost)) from orders made in the past week.

Retrieve four columns labeled ranking, id, name and net_profit where the name id refers to the column menu_item.id.
Any rows with identical net_profit should be ordered by menu_item.id ascending and share the same ranking number, leaving a gap for the tied row(s). For example, if there is a two-item tie for second place, the ranking column would contain 1, 2, 2, 4, 5.
Do not format the net_profit column as currency.


menu_item:
id | price | cost  |  name
---+-------+-------+------------
1  | 14.99 | 4     | mushroom
2  | 8.99  | 4.09  | dragon
3  | 4.99  | 1.63  | zucchini
4  | 3.99  | 1.25  | rainbow
5  | 13.99 | 5.8   | portobello
6  | 15.99 | 11.35 | brown rice
sales_order:
id | order_time                | chef_station
---+---------------------------+-------------
1  | 2018-11-24 17:58:26 +0000 | 2
2  | 2018-11-27 18:22:26 +0000 | 1
3  | 2018-12-01 17:53:38 +0000 | 2
4  | 2018-12-02 18:08:02 +0000 | 1
order_item:
id | sales_order_id | menu_item_id
---+----------------+-------------
1  | 1              | 2
2  | 1              | 6
3  | 2              | 6
4  | 2              | 4
5  | 2              | 1
6  | 3              | 1
7  | 3              | 2
8  | 3              | 4
9  | 4              | 1
10 | 4              | 5
11 | 4              | 2
The result table returned by the query is:

ranking | id | name       | net_profit
--------+----+------------+----------
1       | 1  | mushroom   | 21.98
2       | 2  | dragon     | 9.8
3       | 5  | portobello | 8.19
4       | 4  | rainbow    | 2.74
"""

"""
select 
rank() over (order by net_profit desc) rank,
id, name, net_profit
from 
(
select x.id, name, price, (qty_sold * (price - cost)) net_profit 
from (
select c.id, c.name, sum(price) price, sum(cost) as cost,
count(*) qty_sold
from order_item a
inner join sales_order b on a.sales_order_id = b.id 
inner join menu_item c on a.menu_item_id = c.id
 group by 1,2
) x
) y;



"""


def binary_tree_compare(a, b):
    if a is None and b is None:
        return True
 
    if a is not None and b is not None:
        return ((a.val == b.val) and
                binary_tree_compare(a.left, b.left) and
                binary_tree_compare(a.right, b.right))
 
    return False


C:/kafka-3.3.1-src/bin/zookeeper-server-start.sh C:/kafka-3.3.1-src/config/zookeeper.properties
C:/kafka-3.3.1-src/bin/kafka-server-start.sh C:/kafka-3.3.1-src/config/server.properties
C:/kafka-3.3.1-src/bin/kafka-topics.sh --create --zookeeper localhost:2181 --topic pyspark-kafka-demo --replication-factor 1 --partitions 3
C:/kafka-3.3.1-src/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic pyspark-kafka-demo