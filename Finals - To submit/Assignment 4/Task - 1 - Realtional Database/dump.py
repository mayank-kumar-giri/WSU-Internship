import ast
import db

def dump(conn):
    columns = ['_id', '_index', '_type', '_score']
    source_ones = ['timestamp', 'Humidity', 'Temperature']
    wind_ones = ['wind_desc', 'wind_direction', 'feels_like']
    fp = open('weather_data.json', "r+")
    insert_query = """
    INSERT INTO Weather VALUES (?,?,?,?,?,?,?,?,?,?,?)
    """
    c = conn.cursor()
    for line in fp.read().splitlines(True):
        entry = ast.literal_eval(line)
        values = tuple(entry[c] for c in columns)
        values += tuple([entry['_source']['pin']['location']])
        values += tuple(entry['_source'][c] for c in source_ones)
        values += tuple(entry['_source']['Wind'][c] for c in wind_ones)
        c.execute(insert_query, values)
    conn.commit()

if __name__=="__main__":
    conn = db.create_connection("database.db")
    # DUMPING THE JSON FILE INTO DB
    # dump(conn)
    c = conn.cursor()
    db.display_weather_table(c)
    conn.close()