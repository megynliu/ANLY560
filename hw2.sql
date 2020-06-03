SELECT film.film_id, film.title, film.description, actor.actor_id, actor.first_name, actor.last_name
FROM  film LEFT JOIN film_actor ON film.film_id = film_actor.film_id
	LEFT JOIN actor ON film_actor.actor_id = actor.actor_id
where film.title like ('zo%'); 
