# def add_task(title):
#     task = {"title": title}
def add_task(title):
    task = {"title": title.strip()}
    return task


def list_tasks():
    return []
