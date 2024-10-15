def main():
    tasks = []

    while True:
        print("\n==========================")
        print("--- Danh sách việc làm ---")
        print("1. Thêm công việc")
        print("2. Xóa công việc")
        print("3. Hiển thị danh sách")
        print("4. Thoát")
        print("==========================")

        choice = input("Chọn chức năng (1-4): ")

        if choice == '1':
            task = input("Nhập công việc: ")
            tasks.append(task.capitalize())
            print("Công việc đã được thêm.")
        elif choice == '2':
            if len(tasks) == 0:
                print("Danh sách hiện đang trống.")
            else:
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task}")
                index = int(input("Nhập số thứ tự công việc muốn xóa: ")) - 1
                if 0 <= index < len(tasks):
                    del tasks[index]
                    print("Công việc đã được xóa.")
                else:
                    print("Số thứ tự không hợp lệ.")
        elif choice == '3':
            if len(tasks) == 0:
                print("Danh sách hiện đang trống.")
            else:
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task}")
        elif choice == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()