from main import user,Session
from sqlalchemy import text

s2=Session()

query=text('SELECT * FROM users')
query2=text('select name from users where id>2')

# Execute a SQL query
result = s2.execute(query2)

# Fetch the results
for row in result:
    print(row)
