from query import backlog
class Backlog:
    def get(self):
        global cur
        return backlog.backlog_fetch(cur)