def season(i: int) -> str:
    seasons = {
        1: 'winter',
        2: 'winter',
        3: 'spring',
        4: 'spring',
        5: 'spring',
        6: 'summer',
        7: 'summer',
        8: 'summer',
        9: 'autumn',
        10: 'autumn',
        11: 'autumn',
        12: 'winter',
    }
    return seasons[i]


if __name__ == '__main__':
    print(season(int(input())))
