import numpy as np

def random_predict(number: int = 1) -> int:
    """
    guessing the number
    :param number:The number that the function made up
    :return:The number of attempts for which the number was guessed
    """
    max_number = 101
    min_number = 0

    if number >= max_number:
        number = max_number - 1
    if number <= min_number:
        number = min_number + 1

    count = 0
    predict_number = max_number // 2

    while True:
        count += 1

        if number == predict_number:
            break
        elif number < predict_number:
                max_number = predict_number
                predict_number = predict_number - (max_number - min_number) // 2
        else:
            min_number = predict_number
            predict_number = predict_number + (max_number - min_number) // 2

    return count

random_predict(100)

def score_game(random_predict) -> int:
    """
    For how many attempts on average out of 1000
    approaches does our algorithm guess
    :param random_predict: the guessing function
    :return: The average number of attempts for which the number was guessed
    """
    count_ls = []  # list for saving attempts

    random_array = np.random.randint(1, 101, size=1000)  # made a list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))  # the average number of attempts

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score


if __name__ == '__main__':
    score_game(random_predict)
