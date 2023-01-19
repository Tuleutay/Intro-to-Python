# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open("text.txt", encoding="utf-8") as f:
    text_file = str(f.readlines())

print(text_file.replace("абв", ""))
