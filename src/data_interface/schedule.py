from infra.database import query, commitQuery


def get_data():
    res = query("SELECT * FROM schedule;")
    return res


def post_data(name, service, data, time):
    commitQuery(
        "INSERT INTO schedule (name, service, data, time) VALUES (?, ?, ?, ?);", (name, service, data, time))


def delete_data(data, time):
    commitQuery(
        "DELETE FROM schedule WHERE data = ? AND time = ?;", (data, time))
