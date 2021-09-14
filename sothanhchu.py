def read_number(num = "", level = -1):
    if int(num) <= 0: return ""
    if len(num) > 3:
        to_read = int(num[-3:])
        remaining = num[0:-3]
    else:
        remaining = "0"
        to_read = int(num)
    res = read_number(remaining, level + 1)
    
   # đọc bình thường theo hàng trăm + explicit ở cuối (nghìn, triệu, tỉ)
    explicit = ""
    if level >= 0:
        explicit = level_name[level%3]
    if to_read <= 0: 
        if explicit == "tỉ ": return res + explicit
        return res

    second_name, third_name = "", ""
    second_explicit = ""
    unit = to_read % 10
    tenth = int((to_read%100)/10)
    hundredth = int(to_read/100)

    first = digit_name[hundredth] + "trăm " if int(remaining) + hundredth > 0 else ""
    if tenth == 0:
        if unit > 0 and first != "": 
            second_explicit = "lẻ "
    elif tenth == 1: second_name = "mười "
    else:
        second_name = digit_name[tenth]
        second_explicit = "mươi "
    if unit == 1 and tenth > 1: third_name = "mốt "
    elif unit != 0: third_name = digit_name[unit]
    return res + first + second_name + second_explicit + third_name + explicit

#Thêm hàm này để catch exception invalid syntax
def TransferToText(value = ""):
    try: 
        val = int(value)
        if val == 0: return digit_name[0]
        return read_number(value)
    except ValueError:
        return "Error: Invalid syntax"