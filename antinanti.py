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

def view_tasks(enter_continue=False):
    tasks = load_tasks()
    if not tasks:
        print("Belum Ada Tugas")
        input("Tekan Enter Untuk Kembali....")
        return
    
    print("\n")
    print("="*25)
    print(" 🧾 Daftar Tugas Anda 🧾")
    print("="*25)
    
    for i, task in enumerate(tasks, start=1):
        today = datetime.date.today()
        deadline_date = datetime.datetime.strptime(task['deadline'], '%Y-%m-%d').date()
        delta = (deadline_date - today).days

        if delta > 1:
            status = f"(H-{delta})"
        elif delta == 0:
            status = ("(Hari Ini)")
        elif delta == 1:
            status = ("(H-1)")
        elif delta < 0:
            status = ("(Terlewat)")
        else:
            status = ""
        
        print(f"{i}. {task['nama']} {status}")
        print(f"   Deskripsi: {task['deskripsi']}")
        print("-"*25)
    if not enter_continue:
        press_enter_to_continue()
    else:
        return

def add_task():
    print("\n--- ➕ Tambah Tugas Baru ➕ ---")
    # input nama
    nama = input("Masukan Nama Tugas: ")
    # Input Deskripsi
    deskripsi = input("Masukan Deskripsi (Opsional, tekan Enter jika tidak ada ): ")
    while True:
        deadline = input("Masukan Deadline Anda(format YYYY-MM-DD): ")
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
    waktu_map =  {"1": "Singkat", "2": "Netral", "3": "Lama"}

    energi_string = energi_map[energi]
    waktu_string = waktu_map[waktu]

    new_task = {
        "nama": nama,
        "deskripsi": deskripsi,
        "deadline": deadline,
        "energi": energi_string,
        "waktu": waktu_string
    }


    tasks = load_tasks()
    tasks.append(new_task)
    save_tasks(tasks)

def complete_task():
         
        view_tasks(enter_continue=True)
        tasks = load_tasks()

        if not tasks:
            print("Tidak Ada Tugas untuk diselesaikan")
            return
        
        finish_number = input("Masukan nomor tugas yang telah diselesaikan (contoh: 1) :")

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

def get_productive_task():

    tasks = load_tasks()

    if not tasks:
        print("Belum Ada Tugas Sama Sekali")
        return

    today = datetime.date.today()
    urgent_tasks = []

    for task in tasks:
        deadline_date = datetime.datetime.strptime(task['deadline'], '%Y-%m-%d').date()
        delta = (deadline_date - today).days

        if delta == 1 or delta == 0:
            urgent_tasks.append(task)

    if urgent_tasks: # jika ditemukan tugas urgent maka akan terdapat peringatan
        print("\n")
        print("‼️  PRIOTITAS: DITEMUKAN TUGAS H-1 (BESOK)‼️")

        # loop untuk menampilkan tugas urgent nya apa saja
        for i, task in enumerate (urgent_tasks, start=1):
            print(f"{i}. {task['nama']} (deadline: {task['deadline']})")

        print("\nSARAN: Kerjakan dahulu jangan nunggu mood, karena ini sudah MEPETT!")
        input("Tekan Enter untuk kembali ke menu...")
        return

    # Jika tidak ada urgent
    
    print("\n--- ⚡ Mode Produktivitas ⚡ ---")
    print("Tidak ada deadline mendesak. Mari cari tugas yang cocok!")

    # 1. Input Energi 
    print("\n🔋 Energi kamu sekarang?")
    print("1. Rendah | 2. Netral | 3. Tinggi")
    while True:
        energi_input = input("Pilih (1-3): ")
        if energi_input in ["1", "2", "3"]:
            break
        print("Pilih 1, 2, atau 3.")

    # 2. Input Waktu 
    print("\n⏳ Waktu kamu sekarang?")
    print("1. Singkat | 2. Netral | 3. Lama")
    while True:
        waktu_input = input("Pilih (1-3): ")
        if waktu_input in ["1", "2", "3"]:
            break
        print("Pilih 1, 2, atau 3.")

    # 3. Mapping 
    energi_map = {"1": "Rendah", "2": "Netral", "3": "Tinggi"}
    waktu_map = {"1": "Singkat", "2": "Netral", "3": "Lama"}

    user_energi = energi_map[energi_input] 
    user_waktu = waktu_map[waktu_input]     

    # 4. FILTERING 
    matched_tasks = [] 

    for task in tasks:
        deadline_date = datetime.datetime.strptime(task['deadline'], '%Y-%m-%d').date()
        delta = (deadline_date - today).days
        # Cek kecocokan
        if task ['energi'] == user_energi and task['waktu'] == user_waktu and delta >= 0:
            matched_tasks.append(task)

    # 5. TAMPILKAN HASIL
    if matched_tasks:
        print(f"\n--- Rekomendasi Tugas ({user_energi} & {user_waktu}) ---")
        for i, task in enumerate(matched_tasks, start=1):
            print(f"{i}. {task['nama']} (Deadline: {task['deadline']})")
    else:
        print("\nTidak ada tugas yang cocok dengan kondisimu saat ini.")
        print("Coba pilih mood yang lain atau kerjakan tugas acak!")

    input("Tekan Enter untuk kembali...")

def main_menu():
    while True:
        clear_screen()

        # menampilkan pilihan menu
        print("="*35)
        print("   Selamat Datang Di AntiNanti😊   ")
        print("="*35)
        print("\nMenu Utama")
        print("1.🧾 Lihat Daftar Tugas Anda ")
        print("2.➕ Input Tugas Baru ")
        print("3.📝 Kerjakan Tugas (Sesuai Produktivitas) ")
        print("4.✔️  Selesaikan Tugas ")
        print("5.🚪 Keluar ")
        
        # input pilihan user
        pilihan = input("Masukan Pilihan Anda (1-5): ")

        if pilihan == '1':
            view_tasks() 
        elif pilihan == '2':
            add_task()
        elif pilihan == '3':
            get_productive_task()
        elif pilihan == '4':
            complete_task()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan AntiNanti!")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka 1-5.")
            input("Tekan Enter untuk melanjutkan...") # Jeda  

if __name__ == "__main__":
    main_menu()  