# Пример данных: три множества участников конкурсов
konkurs1 = {"Алиса", "Боб", "Чарли", "Давид"}
konkurs2 = {"Боб", "Давид", "Ева", "Фёдор"}
konkurs3 = {"Чарли", "Давид", "Григорий", "Ирина"}

# 1. Кто участвовал во всех трёх конкурсах: пересечение всех трёх множеств (intersection)
uchastniki_vo_vseh = konkurs1.intersection(konkurs2, konkurs3)
print(f"1. Участники, участвовавшие во всех трёх конкурсах: {uchastniki_vo_vseh}")

# 2. Кто участвовал хотя бы в одном конкурсе: объединение всех трёх множеств (union)
uchastniki_hotya_by_v_odnom = konkurs1.union(konkurs2, konkurs3)
print(f"2. Участники, участвовавшие хотя бы в одном конкурсе: {uchastniki_hotya_by_v_odnom}")

# 3. Участники, которые участвовали только в одном конкурсе:
#    Сначала находим, кто участвовал во всех и кто в двух, затем вычитаем их из общего множества.
uchastniki_tolko_v_odnom = (uchastniki_hotya_by_v_odnom - uchastniki_vo_vseh)
# Удаляем тех, кто участвовал в двух конкурсах
uchastniki_tolko_v_odnom = uchastniki_tolko_v_odnom - (konkurs1.intersection(konkurs2) - konkurs3) - \
                           (konkurs1.intersection(konkurs3) - konkurs2) - \
                           (konkurs2.intersection(konkurs3) - konkurs1)
print(f"3. Участники, участвовавшие только в одном конкурсе: {uchastniki_tolko_v_odnom}")

# Альтернативный способ для №3 (более наглядно):
# Создаём словарь, где ключ - участник, а значение - количество конкурсов.
uchastniki_kolichestvo = {}
for uchastnik in uchastniki_hotya_by_v_odnom:
    kolichestvo = 0
    if uchastnik in konkurs1:
        kolichestvo += 1
    if uchastnik in konkurs2:
        kolichestvo += 1
    if uchastnik in konkurs3:
        kolichestvo += 1
    uchastniki_kolichestvo[uchastnik] = kolichestvo

uchastniki_tolko_v_odnom_alt = {uchastnik for uchastnik, count in uchastniki_kolichestvo.items() if count == 1}
print(f"3. Участники, участвовавшие только в одном конкурсе (альтернативный): {uchastniki_tolko_v_odnom_alt}")


# 4. Находим участников, которые участвовали ровно в двух конкурсах:
#    Сначала находим все попарные пересечения, затем вычитаем тех, кто участвовал во всех трёх.
uchastniki_v_dvuh_konkursah = (konkurs1.intersection(konkurs2) | konkurs1.intersection(konkurs3) | konkurs2.intersection(konkurs3)) - uchastniki_vo_vseh
print(f"4. Участники, участвовавшие ровно в двух конкурсах: {uchastniki_v_dvuh_konkursah}")

# Альтернативный способ для №4:
uchastniki_rovno_dva = {uchastnik for uchastnik, count in uchastniki_kolichestvo.items() if count == 2}
print(f"4. Участники, участвовавшие ровно в двух конкурсах (альтернативные): {uchastniki_rovno_dva}")