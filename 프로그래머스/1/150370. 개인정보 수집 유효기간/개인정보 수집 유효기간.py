from datetime import datetime


def compare_dates(y1, m1, d1, y2, m2, d2):
    date1 = f"{y1:04d}-{m1:02d}-{d1:02d}"
    date2 = f"{y2:04d}-{m2:02d}-{d2:02d}"

    date_obj1 = datetime.strptime(date1, "%Y-%m-%d")
    date_obj2 = datetime.strptime(date2, "%Y-%m-%d")

    if date_obj1 >= date_obj2:
        return True
    return False


def get_date(y, m, d, term):
    temp = m + term
    if temp <= 12:
        return y, temp, d
    a, b = divmod(temp, 12)
    return y + a if b != 0 else y + a - 1, b if b != 0 else 12, d


def solution(today, terms, privacies):
    answer = []
    ty, tm, td = map(int, today.split("."))

    terms_dict = {}
    for term in terms:
        a, b = term.split()
        terms_dict[a] = int(b)

    for idx, val in enumerate(privacies, start=1):
        date, term = val.split()
        y, m, d = map(int, date.split("."))
        ny, nm, nd = get_date(y, m, d, terms_dict[term])
        temp = compare_dates(ty, tm, td, ny, nm, nd)
        if temp:
            answer.append(idx)

    return answer
