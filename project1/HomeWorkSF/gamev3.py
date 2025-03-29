import numpy as np
def game_core_v3(number: int = 1) -> int:
    """Алгоритм угадывания загаданного рандомно числа
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0     # Переменная для подсчета попыток
    predict = np.random.randint(1,101) # Предполагаемое число
    np.random.seed(1)    # Фиксируем сид для воспроизводимости
    
    while number != predict:   # Бесконечный цикл, пока число не будет угадано
        count += 1     # Если не угадано, увеличиваем счетчик
        if number > predict:   # Если загаданное число больше предполагаемого
            if number - predict > 10:   # Если больше более чем на 10
                predict += 10    # Увеличиваем предполагаемое число на 10
            else:    
                predict += 1   # Если меньше чем на 10 прибавляем 1
        elif number < predict:   # Если загаданное число меньше предполагаемого
            if predict - number > 10:   # Если меньше более чем на 10 
                predict -= 10    # Уменьшаем предполагаемое на 10
            else:    
                predict -= 1   # Если менее чем на 10 уменьшаем на 1
    return (count)  


def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
score_game(game_core_v3)

