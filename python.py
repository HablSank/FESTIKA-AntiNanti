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
            view_tasks() 
        elif pilihan == '2':
            print("Dalam Proses Debug")
            add_task()
        elif pilihan == '3':
            print("Dalam Proses Debug")
            get_productive_task()
        elif pilihan == '4':
            print("Dalam Proses Debug")
            complete_task()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan AntiNanti!")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka 1-5.")
            input("Tekan Enter untuk melanjutkan...") # Jeda  

def view_tasks():
    tasks = load_tasks()

    if not tasks:
        print("Belum Ada Tugas")
        return
    

    for i, task in enumerate(tasks, start=1):
        today = datetime.date.today()
        deadline_date = datetime.datetime.strptime(task['deadline'], '%Y-%m-%d').date()
        delta = (deadline_date - today).days

        if delta == 0:
            status = ("Hari Ini")
    # Input Waktu
        elif delta == 1:
            status = ("H-1")
        elif status < 0:
            status = ("Terlewat")
        else:
            status = ""

def add_task():
    # input nama
    nama = input("Masukan Nama Tugas: ")
    # Input Deskripsi
    deskripsi = input("Masukan Deskripsi (Opsional, tekan Enter jika tidak ada ): ")
    while True:
        deadline = input("Masukan Deadline Anda(format YYY-MM-DD): ")
        try:
            datetime.datetime.strptime(deadline, '%Y-%m-%d')
        except ValueError:
            print("Format Salah Coba Lagi")
        else:
            break

    # Input Energi
    print("\n--- Kebutuhan Energi ---")
    print("1. Rendah (Tugas ringan)")
    print("2. Netral (Tugas biasa)")
    print("3. Tinggi (Tugas berat, butuh fokus tinggi)")
    while True:
        energi = input("Pilih Kebutuhan Energi Anda(1/2/3)")

        if energi =="1" or energi == "2" or energi == "3":
            break
        else:
            print("Input tidak valid! Harap masukan input yang valid (1/2/3)")
    
    print("\n--- Kebutuhan Waktu ---")
    print("1. Singkat (< 30 menit)")
    print("2. Netral (30 menit - 2 jam)")
    print("3. Lama (> 2 jam)")
    while True:
        waktu = input("Pilih kebutuhan waktu (1/2/3): ")
        if waktu in ["1", "2", "3"]:
            break
        else:
            print("Input tidak valid! Harap masukkan HANYA angka 1, 2, atau 3.")

    
    energi_map = {"1": "Rendah", "2": "Netral", "3": "Tinggi"}
    Time_map =  {"1": "Singkat", "2": "Netral", "3": "Lama"}

    energi_string = energi_map[energi]
    waktu_string = energi_map[waktu]

    new_task = {
        "nama": nama,
        "deskripsi": deskripsi,
        "deadline": deadline,
        "energi": energi,
        "waktu": waktu
    }


    tasks = load_tasks()
    tasks.append(new_task)
    save_tasks(tasks)

def complete_task():
        
        view_tasks()
        tasks = load_tasks()

        if not tasks:
            print("Tidak Ada Tugas untuk diselesaikan")
            return
        
        finish_number = input("Masukan nomor tugas yang telah diselesaikan (contoh: 1)")

        try:
            finish_number = int(finish_number)

            if 1 <= finish_number <= len(tasks):

                remove_index = finish_number - 1
                remove_task = tasks.pop(remove_index)
                save_tasks(tasks)

                print(f"\nSelamat Tugas '{remove_task['nama']} telah selesai")
            
            else:
                print(f"Error: Nomor {finish_number} tidak ada dalam daftar")
        
        except ValueError:
            print("Error: Input harus berupa angka.")
        
        input("Tekan Enter untuk kembali ke menu..")

