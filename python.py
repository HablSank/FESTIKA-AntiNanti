import json
import sys
import datetime
import os

TASK_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    try:
        with open(TASK_FILE, 'r') as f:
            tasks = json.load(f)
            return tasks
    except json.JSONDecodeError:
        print(f"Error: File {TASK_FILE} rusak atau tidak valid.")
        return []
    
def save_tasks(tasks_list):
    try:
        with open(TASK_FILE, 'w') as f:
            json.dump(tasks_list, f, indent=4)
    except IOError as e:
        print(f"Error saat menyimpan file: {e}")

def clear_screen():
    # Membersihkan layar terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def press_enter_to_continue():
    # jeda hingga pengguna menekan enter
    input("\nTekan Enter untuk kembali ke menu...")

def main_menu():
    while True:
        clear_screen()

        # menampilkan pilihan menu
        print("="*35)
        print("   Selamat Datang Di AntiNanti😊   ")
        print("="*35)
        print("\nMenu Utama")
        print("  1.Lihat Daftar Tugas Anda ")
        print("  2.Input Tugas Baru ")
        print("  3.Kerjakan Tugas (Sesuai Produktivitas) ")
        print("  4.Selesaikan Tugas ")
        print("  5.Keluar ")
        

        # input pilihan user
        pilihan = input("Masukan Pilihan Anda (1-5): ")

        if pilihan == '1':
         print("Dalam Proses Debug")
        # nanti akan diisi view_tasks() 
        elif pilihan == '2':
         print("Dalam Proses Debug")
        # nanti akan diisi add_task()
        elif pilihan == '3':
         print("Dalam Proses Debug")
        # nanti akan diisi get_productive_task()
        elif pilihan == '4':
         print("Dalam Proses Debug")
        # nanti akan diisi complete_task()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan AntiNanti!")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka 1-5.")
            input("Tekan Enter untuk melanjutkan...") # Jeda    

def view_task():
    task = load_tasks()

    if not task:
        print("Belum Ada Tugas")
        return
    
    for i, task in enumerate(task, start=1):
        today = datetime.date.today()
        deadline_date = datetime.datetime.strptime(task['deadline'], '%Y-%m-%d').date()
        delta = (deadline_date - today).days

        if delta == 0:
            status = ("Hari Ini")
        elif delta == 1:
            status = ("H-1")
        elif status < 0:
            status = ("Terlewat")
        else:
            status = ""

