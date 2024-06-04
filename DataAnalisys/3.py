def f(line):
   return sum(1 for x in line if x in "aoeu")


silence = ["Sand Rustling",
          "Snake Sliding",
          "wind whispering",
          "Night In The Village"]
params = {
   "sort_key": f
}

def alertness(*args, **kwargs):
    res = dict()
    heavy = kwargs.get("heavy", "wxyz")
    unique = kwargs.get("unique", 10)
    sort_key = kwargs.get("sort_key", None)
    for item in args:
        for l in heavy.lower():
            if l in item.lower():
                res.setdefault("strong", [])
                res["strong"].append(item.upper())
                break
        if len(set(filter(lambda x: x.isalpha(), item))) >= unique:
            res.setdefault("careful", [])
            res["careful"].append(item)
        if len(item.split()) >= 2:
            for i in item.split():
                if not i[0].isupper():
                    break
            else:
                res.setdefault("alert", [])
                res["alert"].append(item.split()[-1].lower())
    for k in res.keys():
        if sort_key:
            res[k].sort(key=sort_key)
    return res


result = alertness(*silence, **params)
print(result)