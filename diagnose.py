import time

t0 = time.perf_counter()
from eng_to_ru_transcriptor import transcribe
t1 = time.perf_counter()
print(f"1. Импорт пакета:          {t1 - t0:.3f} сек")

t2 = time.perf_counter()
result = transcribe("hello world")
t3 = time.perf_counter()
print(f"2. Первый вызов:           {t3 - t2:.3f} сек")

t4 = time.perf_counter()
result = transcribe("hello world")
t5 = time.perf_counter()
print(f"3. Второй вызов:           {t5 - t4:.3f} сек")