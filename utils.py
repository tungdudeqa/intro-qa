from datetime import datetime, timedelta
import calendar


def retention_date_format(end_date, retention_days):
    retention_days = int(retention_days)
    base_date = datetime.strptime(end_date, "%Y-%m-%d")
    result_date = base_date + timedelta(days=7 + retention_days)
    formatted = f"{retention_days} Days ({result_date.strftime('%d %b %Y')})"
    return formatted


def month_abbr_to_num(month_abbr):
    return list(calendar.month_abbr).index(month_abbr.capitalize())