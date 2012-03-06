import os
import common
from pysqlite2 import dbapi2 as sqlite

# Initialize the database and perform startup actions
def init():
  global connection
  common.create_dir()
  connection = create_connection()
  setup_db()
#  check_version()

def create_connection():
  confdir = common.confdir;
  return sqlite.connect(confdir + os.sep + 'radula.db')

# Setup the db
def setup_db():
  cursor = connection.cursor()

  # Setup the database
  cursor.execute('select name from sqlite_master where type="table" and name=?', ('radula',))
  data = cursor.fetchone()
  if data is None:
    print('No radula table found, building it.')
    cursor.execute('CREATE TABLE radula (key VARCHAR(256) PRIMARY KEY, value VARCHAR(256))')
    cursor.execute('INSERT INTO radula VALUES ("version", ?)', (common.version,))
    connection.commit()
  else:
    print(data)

# Check the version
def check_version():
  cursor = connection.cursor()
  cursor.execute('SELECT value FROM shoal WHERE key = "version"')
  data = cursor.fetchone()
  if data is None:
    print('No version information found.  Bailing!')
  elif data[0] == str(common.version):
    print('Versions match, great!')
  else:
    print('Uhoh, version mistmatch. Do something here.')

init();
