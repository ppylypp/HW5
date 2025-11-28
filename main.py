#updated code
def main():
    print("--- АНКЕТА СТУДЕНТА (ДЗ) ---")
    name = input("Введіть ваше ім'я: ")
    status = input("Введіть ваш статус (студент/викладач): ")
    print(f"\nПривіт, {name}! Ваш статус '{status}' зафіксовано у Docker-контейнері.")
    print("Робота завершена успішно.")

if __name__ == "__main__":
    main()