
class LibraryBorrow:
    def __init__(self, id, reader_name, book_name, borrow_days, late_days, fine_per_day):
        self.id = id 
        self.reader_name = reader_name
        self.book_name = book_name
        self.borrow_days = borrow_days
        self.late_days = late_days
        self.fine_per_day = fine_per_day 
        self.total_fine = 0
        self.fine_type = ""
    def calculate_fine(self):
        self.total_fine = self.late_days * self.fine_per_day
    def classify_fine(self):
        if self.total_fine == 0:
            self.fine_type = "Không phạt"
        elif self.total_fine > 0:
            self.fine_type = "Nhẹ"
        elif self.total_fine >= 50000:
            self.fine_type = "Trung bình"
        else:
            self.fine_type = "Nặng"

class LibraryBorrowManager:
    def __init__(self):
        self.borrow_records = []
    def add_borrow_record(self):
        id = input("Nhập mã phiếu mượn:")
        reader_name = input("Nhập họ tên bạn đọc:")
        book_name = input("Nhập Tên sách:")
        borrow_days = int(input("Nhập số ngày đã mượn:"))
        late_days = int(input("Nhập số ngày trễ hạn:"))
        fine_per_day = int(input("Nhập tiền phạt mỗi ngày:"))

        new_book = LibraryBorrow(
            id,reader_name,book_name,borrow_days,late_days,fine_per_day
        )
        new_book.calculate_fine()
        new_book.classify_fine()

        self.borrow_records.append(new_book)
        print("Thêm thành công")
    def show_all(self):
        #if not self.borrow_records:
        #    print("Danh sách phiếu mượn đang rỗng")
        #    return
        print("-- Danh sách phiếu mượn -- ")
        print(f"Mã phiếu mượn | Họ tên bạn đọc | Tên sách | Số ngày đã mượn | Số ngày trễ hạn | Tiền phạt mỗi ngày | Tổng tiền phạt | Phân loại mức phạt")
        for book in self.borrow_records:
            print(f"{book.id} | {book.reader_name} | {book.borrow_days} | {book.late_days} | {book.fine_per_day} | {book.total_fine} | {book.fine_type}")
    def update_borrow_record(self):
        update_id = input("Nhập mã phiếu mượn cần cập nhật")
        found = False
        for book in self.borrow_records:
            if book.id == update_id:
                self.borrow_days = int(input("Nhập số ngày đã mượn:"))
                self.late_days = int(input("Nhập số ngày trễ hạn:"))
                self.fine_per_day = int(input("Nhập tiền phạt mỗi ngày:"))
                print("Cập nhật thành công")
                found = True
                break
        if found == False:
            print("Mã phiếu không tồn tại")
    def delete_borrow_record(self):
        delete_id = input("Nhập mã phiếu mượn muốn xoá ")
        pass

    
using_method = LibraryBorrowManager()
while True:
    choice  = input("""================ MENU ================
1. Hiển thị danh sách phiếu mượn
2. Thêm phiếu mượn mới
3. Cập nhật phiếu mượn
4. Xóa phiếu mượn
5. Tìm kiếm phiếu mượn
6. Thoát
=====================================
Nhập lựa chọn của bạn:
""")
    match choice:
        case '1':
            using_method.show_all()
        case '2':
            using_method.add_borrow_record()
        case '3':
            using_method.update_borrow_record()
        case '4':
            pass
        case '5':
            pass
        case '6':
            print("Thoát chương trình")
            break
        case _:
            print("Lựa chọn không hợp lệ! Vui lòng nhập lại")