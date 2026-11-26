import sqlite3

connection = sqlite3.connect(":memory:")
connection.execute("PRAGMA foreign_keys = ON")
cursor = connection.cursor()

cursor.executescript("""
CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    price REAL NOT NULL CHECK (price >= 0)
);

CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE OrderDetails (
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price REAL NOT NULL CHECK (unit_price >= 0),
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE INDEX idx_orders_user_date ON Orders(user_id, order_date);
CREATE INDEX idx_orderdetails_product ON OrderDetails(product_id);

INSERT INTO Users (name, email)
VALUES ('Asha Kumar', 'asha@example.com'),
       ('Ravi Shah', 'ravi@example.com');

INSERT INTO Products (product_name, price)
VALUES ('Notebook', 5.00), ('Pen', 2.00), ('Backpack', 30.00);

INSERT INTO Orders (user_id, order_date)
VALUES (1, '2026-03-02'), (1, '2026-03-18'), (2, '2026-03-20');

INSERT INTO OrderDetails (order_id, product_id, quantity, unit_price)
VALUES
    (1, 1, 2, 5.00),
    (1, 2, 3, 2.00),
    (2, 1, 1, 5.00),
    (3, 3, 1, 30.00);
""")

# Retrieve all orders by a user
user_id = 1
cursor.execute("""
    SELECT o.order_id, o.order_date,
           SUM(od.quantity * od.unit_price) AS order_total
    FROM Orders AS o
    JOIN OrderDetails AS od ON od.order_id = o.order_id
    WHERE o.user_id = ?
    GROUP BY o.order_id, o.order_date
    ORDER BY o.order_date
""", (user_id,))
print("User orders:", cursor.fetchall())

# Find the most purchased product by total quantity
cursor.execute("""
    SELECT p.product_name, SUM(od.quantity) AS quantity_purchased
    FROM OrderDetails AS od
    JOIN Products AS p ON p.product_id = od.product_id
    GROUP BY p.product_id, p.product_name
    ORDER BY quantity_purchased DESC
    LIMIT 1
""")
print("Most purchased product:", cursor.fetchone())

# Calculate revenue for a given month
month = "2026-03"
cursor.execute("""
    SELECT COALESCE(SUM(od.quantity * od.unit_price), 0) AS monthly_revenue
    FROM Orders AS o
    JOIN OrderDetails AS od ON od.order_id = o.order_id
    WHERE o.order_date >= ?
      AND o.order_date < date(?, '+1 month')
""", (month + "-01", month + "-01"))
print("Monthly revenue:", cursor.fetchone()[0])

connection.close()