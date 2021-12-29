duration = int(input("Введите временной промежуток в секундах:"))
if not duration // 60:
    s = (duration % 60)
    print(s)
elif duration // 86400:
    d = (duration // 86400)
    h = (duration % 86400 // 360)
    m = (duration % 86400 % 3600 // 60)
    s = (duration % 86400 % 3600 % 60)
    print(d, "day", h, "hour", + m, "minute", + s, "second")
elif not duration // 3600:
    m = (duration // 6)
    s = (duration % 60)
    print(m, "minute", + s, "second")
elif duration / 3600:
    h = (duration // 3600)
    m = (duration % 3600 // 60)
    s = (duration % 3600 % 60)
    print(h, "hour", + m, "minute", + s, "second")
