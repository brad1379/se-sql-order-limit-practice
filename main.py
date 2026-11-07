import pandas as pd
import sqlite3


conn = sqlite3.connect('data.sqlite')


# # ----------------- Select all products -----------------
# products = pd.read_sql("""
# SELECT *
#     FROM products;
# """, conn)
# print(products)


# ----------------- TASK 1: ORDER BY productCode DESC -----------------
order_by_productCode = pd.read_sql("""
SELECT *
    FROM products
    ORDER BY productCode DESC;
""", conn)
print(order_by_productCode)


# ----------------- TASK 2: Sort by productLine then productName -----------------
sort_by_product_line_and_name = pd.read_sql("""
SELECT productCode, productLine, productName, productVendor
    FROM products
    ORDER BY productLine, productName;
""", conn)
print(sort_by_product_line_and_name)


# ----------------- TASK 3: Count how many distinct product lines -----------------
count_distinct_product_lines = pd.read_sql("""
SELECT COUNT(DISTINCT productLine) AS num_productLine
    FROM products
""", conn)
print(count_distinct_product_lines)


# ----------------- TASK 4: Order by difference in MSRP and buyPrice then order by quantityInStock  -----------------
order_by_diff_and_quant = pd.read_sql("""
SELECT productName, quantityInStock, MSRP, buyPrice,
        MSRP - buyPrice AS difference
    FROM products
    ORDER BY difference DESC, CAST(quantityInStock AS INTEGER) ASC
""", conn)
print(order_by_diff_and_quant)


# ----------------- TASK 5:  -----------------
order_by_diff_and_quant = pd.read_sql("""
SELECT productName, productLine, MSRP, buyPrice,
        ABS(MSRP - buyPrice) AS abs_difference
    FROM products
    WHERE productLine = "Classic Cars"
    ORDER BY abs_difference DESC
    LIMIT 10
""", conn)
print(order_by_diff_and_quant)


conn.close()
