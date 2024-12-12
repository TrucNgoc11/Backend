# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def calculator():
    while True:
        print("\n=== Máy tính mini ===")
        print("1. Cộng")
        print("2. Trừ")
        print("3. Nhân")
        print("4. Chia")
        print("5. Thoát")

        choice = input("Chọn một phép toán (1-5): ")
        if choice == "5":
            print("Thoát chương trình. Tạm biệt!")
            break

        num1 = float(input("Nhập số liệu thứ nhất:"))
        num2 = float(input("Nhập số liệu thứ hai: "))

        if choice == '1':
            print(f"Kết quả: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Kết quả: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Kết quả: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"Kết quả: {num1} / {num2} = {num1 / num2}")
            else:
                print("Không thể chia cho 0!")
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

calculator()