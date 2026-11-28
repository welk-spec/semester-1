.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.

-- list every column for every driver
--SELECT * FROM drivers;

-- 2. List the name and price of every dish sold by Bangkok Garden (restaurant 3).
--SELECT name, price FROM dishes
--WHERE restaurant_id = 3;

--3. List the names of all the Indian restaurants.
--SELECT name FROM restaurants
--WHERE cuisine = 'Indian';

--4. How many customers does Leeds Eats have?
--SELECT COUNT(*) FROM customers


--silver
--5. **A student:** "I'm vegetarian and I've only got £8. What could I order? Cheapest first, please."
--SELECT name, price FROM menu_items
--WHERE is_vegetarian = 1 AND price <= 8
--ORDER BY price;

--6. **A food safety officer from Leeds City Council:** "Which restaurants have a hygiene rating below 4? Show the worst first."
--SELECT name, hygiene_rating FROM restaurants
--WHERE hygiene_rating < 4
--ORDER BY hygiene_rating;

--7. **A student who lives in LS6:** "Which restaurants are near me, best rated first?" Does a matching postcode really mean a restaurant is near? What could go wrong?
SELECT r.name, ROUND(AVG(v.rating), 2) AS avg_rating, COUNT(*) AS num_reviews
FROM restaurants r
JOIN orders o ON o.restaurant_id = r.restaurant_id
JOIN reviews v ON v.order_id = o.order_id
WHERE r.postcode LIKE 'LS6%'
GROUP BY r.restaurant_id
ORDER BY avg_rating DESC;

--8. **The marketing team:** "We want to email everyone who signed up with a University of Leeds email address, newest members first." Write the query, then say whether Leeds Eats should actually send this email.

--9. **The operations manager:** "Show me the 10 most recent cancelled orders."

--10. **The owner of Pasta Pronto (restaurant 4):** "Which of my dishes are vegetarian? And what's my most expensive dish?" (Two queries.)