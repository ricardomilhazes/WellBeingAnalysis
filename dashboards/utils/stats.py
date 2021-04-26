def question_stats(questions):
    size = questions.count()
    averages = []

    for entry in questions:
        entry_total = (
            entry["difficulty"]
            + entry["time"]
            + entry["clarity"]
            + entry["content"]
            + entry["knowledge"]
            + entry["interactivity"]
            + entry["comment_rating"]
        )
        average = round((entry_total / 7), 2)
        averages.append(average)

    return max(averages), min(averages), round((sum(averages) / size), 2), size
