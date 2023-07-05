ori_n = input()
if (ori_n == "0") :
    print("1")
else: 
    if int(ori_n) < 10:
        ori_n = '0' + ori_n
    count = 0
    n = ori_n
    new_n = "00"
    new_l = list(new_n)
    while new_n != ori_n:
        new_l[0] = n[1]
        new_l[1] = str((int(n[0]) + int(n[1])) % 10)
        new_n = "".join(new_l)
        n = new_n
        count += 1
    print(count)
