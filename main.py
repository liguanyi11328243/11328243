def add_task():
    print("Add task")

def show_tasks():
    print("Show tasks")

def main():
    while True:
        print("\n=== To-Do List 管理系統 ===")
        print("1. 顯示任務清單")
        print("2. 新增任務")
        print("3. 離開系統")
        
        choice = input("請選擇功能（輸入數字）：").strip()
        
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            print("感謝使用，再見！")
            break
        else:
            print("無效的選擇，請重新輸入。\n")

# 啟動主程式
main()
def complete_task():
    if not pending_tasks:
        print("\n目前沒有未完成的任務！\n")
        return

    show_tasks()
    try:
        task_idx = int(input("請輸入要完成的任務編號：")) - 1
        if 0 <= task_idx < len(pending_tasks):
            task = pending_tasks.pop(task_idx)
            completed_tasks.append(task)
            print(f"\n成功完成任務：{task['title']}\n")
        else:
            print("\n無效的編號！請重新選擇。\n")
    except ValueError:
        print("\n輸入無效！請輸入數字。\n")