contacts = {}

while True:
    action = input("Chọn hành động (thêm, tìm, thoát): ")

    if action == "thêm":
        name = input("Nhập tên: ")
        phone = input("Nhập số điện thoại: ")
        contacts[name] = phone
    elif action == "tìm":
        name = input("Nhập tên để tìm: ")
        print(contacts.get(name, "Không tìm thấy"))
    elif action == "thoát":
        break

