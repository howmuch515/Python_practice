achievement = {"yoshimura": 1, "yamamoto": 74, "kido-kingdom": 95, "okuda": 59}

for name, score in achievement.items():
    if 60 <= score:
        evaluation = "A"
    elif 30 <= score < 60:
        evaluation = "B"
    else:
        evaluation = "C"

    print("{0}: {1}({2})".format(name, score, evaluation))
