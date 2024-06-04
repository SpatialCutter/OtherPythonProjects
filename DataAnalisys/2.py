def ideas(*args, letters="ae"):
    mx = 0
    for item in args:
        lc = len(item)
        word = ""
        for letter in item[::-1]:
            if letter not in letters:
                word += letter
        if word not in holiday:
            if lc > mx: mx = lc
            holiday.append(word)
    return mx

holiday = ["building", "owl"]
data = ["fealowe", "lawoe",
        "tnuom", "akecora",
        "tune", "gnidleiaub"]
result = ideas(*data)
print(result)
print(*holiday)
