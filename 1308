import datetime

today_year, today_month, today_day = map(int, input().split())
Dday_year, Dday_month, Dday_day = map(int, input().split())


today_time = datetime.datetime(today_year, today_month, today_day)
Dday_time = datetime.datetime(Dday_year, Dday_month, Dday_day)
diff_day = (Dday_time - today_time).days
if (Dday_year - today_year > 1000) or (Dday_year - today_year == 1000 and (Dday_month > today_month or (Dday_month == today_month and Dday_day >= today_day))):
    print("gg")
else:
    print("D-" + str(diff_day))
