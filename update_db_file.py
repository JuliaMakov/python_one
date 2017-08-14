from make_db_file import loadDbase, storeDbase
db = loadDbase()
db['bob']['pay'] *= 0.111
db['tom']['name'] = 'Tom Tom'
storeDbase(db)
