import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'your_host',  # Use 'localhost' for a local database
    'port': 'your_port'   # Default PostgreSQL port is 5432
}

# Initialize a dictionary to store the count of posts by country
post_counts = {}

try:
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**db_params)
    
    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Query to count posts by country
    query = "SELECT country, COUNT(*) FROM posts GROUP BY country;"

    # Execute the query
    cursor.execute(query)

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Populate the post_counts dictionary
    for row in rows:
        country, count = row
        post_counts[country] = count

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Print the post counts by country
    for country, count in post_counts.items():
        print(f"{country}: {count} posts")

except psycopg2.Error as e:
    print("Error connecting to the database:", e)