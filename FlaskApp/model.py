import sqlite3


class Person():
    db = None

    def __init__(self, config):
        self.config = config
        if not Person.db:
            Person.db = sqlite3.connect(self.config.DB_FILE)

    def add(self, name, comment):
        self.db.execute('insert into %s (name, comment) values ("%s", "%s")' % (self.config.TABLE, name, comment))
        self.db.commit()

    def read_all(self):
        res = self.db.execute('select name, comment, id from %s' % (self.config.TABLE,)).fetchall()
        return [{'id': i[2], 'name': i[0], 'comment': i[1]} for i in res]

    def read_random(self, number):
        # Не самый эффективный способ но все же
        res = self.db.execute('select * from %s order by random() limit %i' % (self.config.TABLE, number)).fetchall()
        return [{'id': i[0], 'name': i[1], 'comment': i[2]} for i in res]


    def remove(self, id):
        # TODO Добавить проверку существует ли запись

        self.db.execute('delete from %s where id = %s' % (self.config.TABLE, id))
        self.db.commit()