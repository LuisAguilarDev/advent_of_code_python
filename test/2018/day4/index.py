from test_utils import load_module
from global_utils.utils import read_file

part1 = load_module("src/2018/day4/part1.py")
part2 = load_module("src/2018/day4/part2.py")

sample = read_file("test/2018/day4/sample.txt")

# Part 1

## Caso 1: Un guardia, dos siestas
def test_single_guard_single_nap():
    naps = part1.parse_data([
        "[1518-11-01 00:00] Guard #10 begins shift",
        "[1518-11-01 00:04] falls asleep",
        "[1518-11-01 00:10] wakes up",
        "[1518-11-01 00:03] falls asleep",
        "[1518-11-01 00:05] wakes up",
    ])
    guard, minute = part1.get_best_guard_and_minute(naps)
    assert guard == 10
    assert minute == 4 # el 4 esta en las dos siestas


## Caso 2: Un guardia, múltiples siestas que repiten el mismo minuto
def test_single_guard_overlapping_minute():
    naps = part1.parse_data([
        "[1518-11-01 00:00] Guard #10 begins shift",
        "[1518-11-01 00:05] falls asleep",
        "[1518-11-01 00:10] wakes up",
        "[1518-11-02 00:00] Guard #10 begins shift",
        "[1518-11-02 00:07] falls asleep",
        "[1518-11-02 00:12] wakes up",
    ])
    guard, minute = part1.get_best_guard_and_minute(naps)
    assert guard == 10
    # Siesta 1: min 5,6,7,8,9 | Siesta 2: min 7,8,9,10,11
    # min 7,8,9 tienen freq 2 -> most_common devuelve 7
    assert minute == 7


## Caso 3: Dos guardias, gana el que más duerme en total
def test_two_guards_most_total_sleep_wins():
    naps = part1.parse_data([
        "[1518-11-01 00:00] Guard #10 begins shift",
        "[1518-11-01 00:10] falls asleep",
        "[1518-11-01 00:40] wakes up",
        "[1518-11-02 00:00] Guard #99 begins shift",
        "[1518-11-02 00:05] falls asleep",
        "[1518-11-02 00:10] wakes up",
    ])
    guard, minute = part1.get_best_guard_and_minute(naps)
    # Guard 10: 30 min totales | Guard 99: 5 min totales
    assert guard == 10


## Caso 4: Datos desordenados - debe ordenar internamente
def test_unsorted_input():
    naps = part1.parse_data([
        "[1518-11-01 00:25] wakes up",
        "[1518-11-01 00:00] Guard #10 begins shift",
        "[1518-11-01 00:05] falls asleep",
    ])
    guard, minute = part1.get_best_guard_and_minute(naps)
    assert guard == 10
    assert minute == 5


## Caso 5: Guardia comienza turno el día anterior (23:58)
def test_guard_starts_before_midnight():
    naps = part1.parse_data([
        "[1518-11-01 23:58] Guard #10 begins shift",
        "[1518-11-02 00:05] falls asleep",
        "[1518-11-02 00:10] wakes up",
    ])
    guard, minute = part1.get_best_guard_and_minute(naps)
    assert guard == 10
    assert minute == 5


## Caso 6: Siesta de un solo minuto (caso mínimo)
def test_one_minute_nap():
    naps = part1.parse_data([
        "[1518-11-01 00:00] Guard #10 begins shift",
        "[1518-11-01 00:30] falls asleep",
        "[1518-11-01 00:31] wakes up",
    ])
    guard, minute = part1.get_best_guard_and_minute(naps)
    assert guard == 10
    assert minute == 30


## Caso 7: Múltiples guardias, múltiples siestas intercaladas
def test_interleaved_guards():
    naps = part1.parse_data([
        "[1518-11-01 00:00] Guard #10 begins shift",
        "[1518-11-01 00:05] falls asleep",
        "[1518-11-01 00:15] wakes up",
        "[1518-11-01 23:58] Guard #99 begins shift",
        "[1518-11-02 00:10] falls asleep",
        "[1518-11-02 00:20] wakes up",
        "[1518-11-03 00:00] Guard #10 begins shift",
        "[1518-11-03 00:05] falls asleep",
        "[1518-11-03 00:15] wakes up",
    ])
    guard, minute = part1.get_best_guard_and_minute(naps)
    # Guard 10: 10+10 = 20 min | Guard 99: 10 min
    assert guard == 10
    # Guard 10 durmió min 5-14 dos veces -> todos freq 2, most_common = 5
    assert minute == 5


## Caso 8: Sample del problema - verificar resultado conocido
def test_sample():
    naps = part1.parse_data(sample)
    guard, minute = part1.get_best_guard_and_minute(naps)
    assert guard == 10
    assert minute == 24
    assert guard * minute == 240


# Part 2

## Caso 1: Un guardia, una siesta - todos los minutos tienen freq 1
def test_p2_single_guard_single_nap():
    naps = part2.parse_data([
        "[1518-11-01 00:00] Guard #10 begins shift",
        "[1518-11-01 00:05] falls asleep",
        "[1518-11-01 00:08] wakes up",
    ])
    guard, minute = part2.get_best_guard_and_minute(naps)
    assert guard == 10
    assert minute == 5


## Caso 2: Un guardia repite un minuto en varias siestas
def test_p2_repeated_minute_same_guard():
    naps = part2.parse_data([
        "[1518-11-01 00:00] Guard #10 begins shift",
        "[1518-11-01 00:10] falls asleep",
        "[1518-11-01 00:15] wakes up",
        "[1518-11-02 00:00] Guard #10 begins shift",
        "[1518-11-02 00:12] falls asleep",
        "[1518-11-02 00:18] wakes up",
    ])
    guard, minute = part2.get_best_guard_and_minute(naps)
    assert guard == 10
    # Siesta 1: 10,11,12,13,14 | Siesta 2: 12,13,14,15,16,17
    # min 12,13,14 tienen freq 2 -> most_common = 12
    assert minute == 12


## Caso 3: Guardia con pocas siestas pero alta frecuencia en un minuto gana
def test_p2_frequency_beats_total_sleep():
    naps = part2.parse_data([
        "[1518-11-01 00:00] Guard #10 begins shift",
        "[1518-11-01 00:00] falls asleep",
        "[1518-11-01 00:50] wakes up",
        "[1518-11-02 00:00] Guard #99 begins shift",
        "[1518-11-02 00:20] falls asleep",
        "[1518-11-02 00:22] wakes up",
        "[1518-11-03 00:00] Guard #99 begins shift",
        "[1518-11-03 00:20] falls asleep",
        "[1518-11-03 00:22] wakes up",
        "[1518-11-04 00:00] Guard #99 begins shift",
        "[1518-11-04 00:20] falls asleep",
        "[1518-11-04 00:22] wakes up",
    ])
    guard, minute = part2.get_best_guard_and_minute(naps)
    # Guard 10: 50 min totales, todos freq 1
    # Guard 99: 6 min totales, min 20,21 tienen freq 3
    assert guard == 99
    assert minute == 20


## Caso 4: Datos desordenados
def test_p2_unsorted_input():
    naps = part2.parse_data([
        "[1518-11-02 00:10] wakes up",
        "[1518-11-01 00:00] Guard #10 begins shift",
        "[1518-11-02 00:05] falls asleep",
        "[1518-11-01 23:58] Guard #10 begins shift",
    ])
    guard, minute = part2.get_best_guard_and_minute(naps)
    assert guard == 10
    assert minute == 5


## Caso 5: Múltiples guardias, el que tiene máxima frecuencia en un minuto
def test_p2_three_guards():
    naps = part2.parse_data([
        "[1518-11-01 00:00] Guard #10 begins shift",
        "[1518-11-01 00:05] falls asleep",
        "[1518-11-01 00:10] wakes up",
        "[1518-11-02 00:00] Guard #10 begins shift",
        "[1518-11-02 00:05] falls asleep",
        "[1518-11-02 00:10] wakes up",
        "[1518-11-03 00:00] Guard #20 begins shift",
        "[1518-11-03 00:15] falls asleep",
        "[1518-11-03 00:20] wakes up",
        "[1518-11-04 00:00] Guard #30 begins shift",
        "[1518-11-04 00:25] falls asleep",
        "[1518-11-04 00:30] wakes up",
    ])
    guard, minute = part2.get_best_guard_and_minute(naps)
    # Guard 10: min 5-9 con freq 2 | Guard 20: freq 1 | Guard 30: freq 1
    assert guard == 10
    assert minute == 5


## Caso 6: Sample del problema - verificar resultado conocido
def test_p2_sample():
    naps = part2.parse_data(sample)
    guard, minute = part2.get_best_guard_and_minute(naps)
    assert guard == 99
    assert minute == 45
    assert guard * minute == 4455
