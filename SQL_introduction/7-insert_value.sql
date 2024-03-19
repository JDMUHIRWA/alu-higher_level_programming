--this is my script 
--about inserting a new row in the first table
# Get the database name from the command line argument
db_name="$1"
# Check if the database name was provided
if [ -z "$db_name" ]; then
    echo "Error: Database name not provided"
    exit 1
fi

# Insert the new row into the first_table table
mysql -e "USE $db_name; INSERT INTO first_table (id, name) VALUES (89, 'Best School');"
