bob = dict(name='Bob Smith', age=42, pay=30000,  job='dev')
sue = dict(name='Sue Johns', age=45, pay=40000,  job='hdv')
tom = dict(name='Tom', age=50, pay=0,  job=None)
db = {'bob': bob, 'sue': sue, 'tom': tom}
if __name__ == '__main__':
    for key in db:
        print(db[key])