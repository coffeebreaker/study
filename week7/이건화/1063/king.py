king, stone, n = input().split()
k = [ord(king[0]) - 64, int(king[1])]
s = [ord(stone[0]) - 64, int(stone[1])]
options = {
    'R': [1, 0], 
    'L': [-1, 0], 
    'B': [0, -1], 
    'T': [0, 1], 
    'RT': [1, 1], 
    'LT': [-1, 1], 
    'RB': [1, -1], 
    'LB': [-1, -1]
}
for _ in range(int(n)) :
    o = input()
    new_k = [k[0] + options[o][0], k[1] + options[o][1]]
    if 0 < new_k[0] <= 8 and 0 < new_k[1] <= 8 :
        if new_k == s :
            new_s = [s[0] + options[o][0], s[1] + options[o][1]]
            if 0 < new_s[0] <= 8 and 0 < new_s[1] <= 8 :
                k = new_k
                s = new_s
        else :
            k = new_k
print(f"{chr(k[0] + 64)}{k[1]}")
print(f"{chr(s[0] + 64)}{s[1]}")