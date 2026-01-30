class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    task = line.strip()
                    if task:
                        self.tasks.append(task)
        except FileNotFoundError:
            pass

    def add_task(self):
        task = input("Görev adı: ").strip()
        if task:
            self.tasks.append(task)
            print("Görev eklendi.")
        else:
            print("Boş görev eklenemez.")

    def list_tasks(self):
        if not self.tasks:
            print("Henüz görev eklenmemiş.")
            return
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def save_tasks(self):
        with open(self.filename, "w") as f:
            for task in self.tasks:
                f.write(task + "\n")
        print("Görevler kaydedildi.")


tm = TaskManager()

while True:
    print("\n1 - Görev ekle")
    print("2 - Görevleri listele")
    print("3 - Kaydet ve çık")

    secim = input("Seçim: ").strip()

    if secim == "1":
        tm.add_task()
    elif secim == "2":
        tm.list_tasks()
    elif secim == "3":
        tm.save_tasks()
        print("Çıkılıyor.")
        break
   
# bu projede oop kullanımı görevleri ve işlemleri tek bir yapı altında toplamak için kullanıldı.