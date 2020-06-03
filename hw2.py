pip install pymysql
#!/usr/bin/python3
import pymysql
db = pymysql.connect("localhost","root","********","sakila" )
cursor = db.cursor()
sql="SELECT film.film_id AS FID, film.title AS title, film.description AS description, actor.first_name, actor.last_name \
FROM  film JOIN film_actor ON film.film_id = film_actor.film_id \
JOIN actor ON film_actor.actor_id = actor.actor_id \
WHERE film.title like ('zo%')"
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        film_id = row [0]
        title = row[1]
        description = row[2]
        first_name = row[3]
        last_name = row[4]
    

        print ("film_id = %s,title = %s,description = %s,first_name = %s,last_name = %s" % (film_id, title, description, first_name, last_name))

except:
   print ("Error: unable to fecth data")
