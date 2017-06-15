import sqlite3


class Person:
    db = None

    def __init__(self, config):
        self.config = config
        if not Person.db:
            Person.db = sqlite3.connect(self.config.DB_FILE)

    def add(self, name, comment):
        self.db.execute('insert into persons (name, comment) values ("%s", "%s")' % (name, comment))
        self.db.commit()

    def read_all(self):
        res = self.db.execute('select name, comment, id from persons').fetchall()
        return [{'id': i[2], 'name': i[0], 'comment': i[1]} for i in res]

    def read_random(self, number):
        # Не самый эффективный способ но все же
        res = self.db.execute('select * from persons order by random() limit %i' % (number, )).fetchall()
        return [{'id': i[0], 'name': i[1], 'comment': i[2]} for i in res]

    def update(self, id_):
        pass

    def read(self, id_):
        pass

    def remove(self, id_):
        # TODO Добавить проверку существует ли запись

        self.db.execute('delete from persons where id = %s' % (id_,))
        self.db.commit()
