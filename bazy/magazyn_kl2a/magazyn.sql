DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS subscriptions;
DROP TABLE IF EXISTS orders;

CREATE TABLE customers (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	address TEXT
);

CREATE TABLE subscriptions (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	description TEXT,
	price_per_month DECIMAL,
	subscription_length TEXT
);

CREATE TABLE orders (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	customer_id INTEGER,
	subscription_id INTEGER,
	purchase_date DATE,
	FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (subscription_id) REFERENCES subscriptions(id)
);
