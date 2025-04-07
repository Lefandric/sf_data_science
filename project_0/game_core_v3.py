import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    max_number = 100
    min_number = 1
    count = 0
    predict = 0
    # Цикл работает пока число которое нужно угадать не будет равно предпологаемому числу
    while number != predict:
        count += 1
        # В качестве предпологаемого числа берётся среднее число в диапазоне
        predict = (min_number + max_number) // 2
        # В зависимости от того число больше предпологаемого или меньше изменяется диапазон
        if number > predict:
            min_number = predict + 1
            
        elif number < predict:
            max_number = predict - 1

    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


score_game(game_core_v3)