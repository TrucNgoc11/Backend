contacts = {}


def add_contact():
    name = input("Nhập tên: ")
    phone = input("Nhập số điện thoại: ")
    contacts[name] = phone
    print(f"Đã thêm {name} với số điện thoại {phone}.")


def view_contacts():
    if not contacts:
        print("Danh bạ trống.")
    else:
        print("\n=== Danh bạ hiện tại ===")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")


def search_contact():
    name = input("Nhập tên cần tìm: ")
    if name in contacts:
        print(f"Số điện thoại của {name} là {contacts[name]}")
    else:
        print(f"Không tìm thấy {name} trong danh bạ.")


def delete_contact():
    name = input("Nhập tên cần xóa: ")
    if name in contacts:
        del contacts[name]
        print(f"Đã xóa {name} khỏi danh bạ.")
    else:
        print(f"{name} không tồn tại trong danh bạ.")


while True:
    print("\n=== Quản lý danh bạ ===")
    print("1. Thêm danh bạ")
    print("2. Hiển thị danh bạ")
    print("3. Tìm kiếm danh bạ")
    print("4. Xóa danh bạ")
    print("5. Thoát")

    choice = input("Chọn một chức năng (1-5): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Thoát chương trình. Tạm biệt!")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")