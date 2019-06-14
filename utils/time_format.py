def split_time(value):
    h = value.split('h')
    m = h[1].split('m')
    s = m[1].split('s')
    ms = s[1].split('ms')
    result = int(h[0]) * 60 * 60 * 1000 + int(m[0]) * 60 * 1000 + int(s[0]) * 1000 + int(ms[0])
    return result
