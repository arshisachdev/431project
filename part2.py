import psycopg2 as db_connect
from tabulate import tabulate
host_name="localhost"
db_user="postgres"
db_password="123"
db_name="postgres"

connection = db_connect.connect(host=host_name,user=db_user,password=db_password,database=db_name)

cursor = connection.cursor()

print("Welcome to the SuperMarket Sales CLI Interface!\n\n")
print("Please Select an option:")
print(" 1. Insert Data\n 2. Delete Date \n 3. Update data \n 4. Search Data \n 5. Aggregate Functions \n 6. Sorting \n 7. Joins\n 8. Grouping\n 9. Subqueries \n 10.Transactions \n 11.Error Handling \n")
query=input("Enter your choice (1-11):")

if query=="1":
    insert_query= "INSERT INTO product (product_line) VALUES ('Books');"
    cursor.execute(insert_query)
    print("\nInsert Successfull!")
elif query=="2":
    delete_query="DELETE FROM purchase WHERE invoice_ID= '750-67-8428';"
    cursor.execute(delete_query)
    print("\nDelete Successfull!")
elif query=="3":
    update_query="UPDATE product SET product_line = 'Home Decor' WHERE product_line = 'Home and Lifestyle';"
    cursor.execute(update_query)
    print("\nUpdate Successfull!")
elif query=="4":
    select_query="SELECT invoice_ID FROM purchase WHERE date='2019-02-08' LIMIT 10;"
    cursor.execute(select_query)
    select_results=cursor.fetchall()
    column_names = [desc.name for desc in cursor.description]
    table = tabulate(select_results, headers=column_names, tablefmt="psql")
    print(table)
elif query=="5":
    aggregate_query="SELECT COUNT(invoice_ID) FROM purchase;"
    cursor.execute(aggregate_query)
    aggregate_results=cursor.fetchall()
    column_names = [desc.name for desc in cursor.description]
    table = tabulate(aggregate_results, headers=column_names, tablefmt="psql")
    print(table)
elif query=="6":
    order_by_query="SELECT invoice_ID, date FROM purchase ORDER BY date asc LIMIT 10;"
    cursor.execute(order_by_query)
    order_by_results=cursor.fetchall()
    column_names = [desc.name for desc in cursor.description]
    table = tabulate(order_by_results, headers=column_names, tablefmt="psql")
    print(table)
elif query=="7":
    join_query="SELECT * FROM income, cost WHERE income.total_cost=cost.total_cost LIMIT 10;"
    cursor.execute(join_query)
    join_results=cursor.fetchall()
    column_names = [desc.name for desc in cursor.description]
    table = tabulate(join_results, headers=column_names, tablefmt="psql")
    print(table)
elif query=="8":
    group_by_query="SELECT COUNT(invoice_ID) FROM purchase GROUP BY Date LIMIT 10;"
    cursor.execute(group_by_query)
    group_by_results=cursor.fetchall()
    column_names = [desc.name for desc in cursor.description]
    table = tabulate(group_by_results, headers=column_names, tablefmt="psql")
    print(table)
elif query=="9":
    nested_query="SELECT * FROM income WHERE total_cost IN (SELECT total_cost FROM cost WHERE gross_income=21.595) LIMIT 10;"
    cursor.execute(nested_query)
    nested_results=cursor.fetchall()
    column_names = [desc.name for desc in cursor.description]
    table = tabulate(nested_results, headers=column_names, tablefmt="psql")
    print(table)
elif query=="10":
    print("TXN Completed")
else:
    print("Error - Please run again and select a valid option")


connection.commit()

connection.close()
