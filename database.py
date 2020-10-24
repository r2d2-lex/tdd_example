import sqlalchemy


def number_of_users_in_database(engine):
    return engine.execute('SELECT count(*) FROM users;').fetchone()[0]


def get_engine():
    return sqlalchemy.create_engine('sqlite://')


def number_in_users_in_database_2():
    engine = get_engine('config', 'qwe1234')
    return number_of_users_in_database(engine)