instruct = '''
Ця програма дозволить вам за допомогою тесту Руф'є провести первинну діагностику вашого здоров'я.\n
Проба Руф'є являє собою навантажувальний комплекс, призначений для оцінки працездатності серця при \n
фізичному навантаженні.
У випробуваного визначають частоту пульсу за 15 секунд.
Потім протягом 45 секунд випробуваний виконує 30 присідань.\n
Після закінчення навантаження пульс підраховується знову: число \n
пульсацій за перші 15 секунд, 30 секунд відпочинку, число пульсацій за останні 15 секунд.\n '''

instruct2 = "Виміряйте пульс за 15с. \nРезультат запишіть у відповідне поле"
instruct3 = "Виконайте 30 присідань за 45с"
instruct4 = '''
Протягом хвилини заміряйте пульс двічі \n 
за перші 15 секунд, потім за останні 15 секунд \n 
результати запишіть у відповідні поля'''

def test(p1, p2, p3):
    s = 4*(p1 + p2 + p3)
    ir = (s - 200) / 10
    return ir

def finish(age, ruf):
    if age >=7 and age <=8:
        if ruf <= 6.4:
            return "чудово"