import random
random.seed()


def judge(file_path, question):
    runTimeErrors = []
    timeLimitErrors = []
    correctAnswers = []
    wrongAnswers = []
    runningTimes = []
    score = 0
    for i in range(numberOfTestCases):
        b = random.randint(0, 4)
        if(b == 0):
            runTimeErrors.append(0)
            timeLimitErrors.append(0)
            correctAnswers.append(1)
            wrongAnswers.append(0)
        elif(b == 1):
            runTimeErrors.append(0)
            timeLimitErrors.append(0)
            correctAnswers.append(0)
            wrongAnswers.append(1)
            score += scores[i]
        elif(b == 2):
            runTimeErrors.append(1)
            timeLimitErrors.append(0)
            correctAnswers.append(0)
            wrongAnswers.append(0)
        elif(b == 3):
            runTimeErrors.append(0)
            timeLimitErrors.append(1)
            correctAnswers.append(0)
            wrongAnswers.append(0)
    return parameters = {"runTimeErrors": runTimeErrors,
                         "timeLimitErrors": timeLimitErrors, "correctAnswers": correctAnswers,
                         "wrongAnswers": wrongAnswers, "runningTimes": runningTimes, "score": score}