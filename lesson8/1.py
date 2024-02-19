fruit1 = ['rottenKiwi', 'strawberry', 'mango', 'rottenBanana', 'tomato', 'apple']

# Перетворюємо всі рядки в нижній регістр за допомогою методу lower()
fruit1_lower = [fruit.lower() for fruit in fruit1]

rotten_index = next((index for index, fruit in enumerate(fruit1_lower) if 'rotten' in fruit), None)

# Перевіряємо, чи є гнилий фрукт
if rotten_index is not None:
    # Замінюємо гнилий фрукт свіжим
    edited_fruit = fruit1_lower[rotten_index].replace('rotten', '')

print(edited_fruit)
