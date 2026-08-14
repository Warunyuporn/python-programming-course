scores = []
for i in range(0, 5):
    score = int(input(f"Enter score of student {i + 1}: "))
    scores.append(score)
 
for i, score in enumerate(scores):
    if score >= 50:
        result = "ผ่าน"
    else:
        result = "ไม่ผ่าน"
    print(f"Student {i + 1}: {score} -> {result}")