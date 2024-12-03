import os

def create_day_folder(day):
    folder_name = f"day-{day:02d}"
    os.makedirs(folder_name, exist_ok=True)
    
    files = ["input.txt", "part_1.py", "part_2.py", "README.md"]
    for file in files:
        open(os.path.join(folder_name, file), 'w').close()

if __name__ == "__main__":
    try:
        day = int(input("Ingrese el número del día (del 01 al 25): "))

        if day < 1 or day > 25:
            raise ValueError

        create_day_folder(day)
        print(f"Folder and files for day-{day:02d} created successfully.")
    except ValueError:
        print("Por favor, ingrese un número entero válido para el día (1 al 25).")