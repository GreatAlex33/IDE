import numpy as np
def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    predict = np.random.randint(1,101)
    while number != predict:
        count += 1
        if number > predict:
            if number - predict > 10:
                predict += 10
            else:
                predict += 1
        elif number < predict:
            if predict - number > 10:
                predict -= 10
            else:
                predict -= 1
    return (count)
print(f'Количество попыток: {game_core_v3()}')
    


