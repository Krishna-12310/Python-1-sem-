from datetime import datetime, date

def validate_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_overdue(due_date, status):
    if status == "Completed":
        return False

    due = datetime.strptime(due_date, "%Y-%m-%d").date()
    return due < date.today()



