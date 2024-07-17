from infra.database import query, commitQuery


def get_data():
    res = query("SELECT * FROM teste;")
    return res


def post_data():
    commitQuery("INSERT INTO teste VALUES('umdoistres', 123);")
