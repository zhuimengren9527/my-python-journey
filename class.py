class Book:
    """定义图书类"""
    def __init__(self, book_name, book_author, book_publication_year):
        """初始化书本信息"""
        self.book_name = book_name
        self.book_author = book_author
        self.book_publication_year = book_publication_year

    def get_book_info(self):
        """打印图书信息"""
        print(f"图书信息：{self.book_name} | 作者：{self.book_author} | 出版年份：{self.book_publication_year}")


class Member:
    """定义会员类"""
    def __init__(self, member_name):
        self.member_name = member_name
        self.borrow_books_list = []

    def borrow_books(self, book):
        """借书方法"""
        self.borrow_books_list.append(book)
        print(f"{self.member_name} 借了《{book.book_name}》")

    def return_books(self, book):
        """还书方法"""
        if book in self.borrow_books_list:
            self.borrow_books_list.remove(book)
            print(f"{self.member_name} 归还了《{book.book_name}》")
        else:
            print(f"{self.member_name} 没有借过《{book.book_name}》这本书")

    def show_borrowed_books(self):
        """展示会员已借的书籍"""
        if self.borrow_books_list:
            print(f"{self.member_name} 借过的书籍：")
            for book in self.borrow_books_list:
                print(f"《{book.book_name}》 {book.book_author} {book.book_publication_year}")
        else:
            print(f"{self.member_name} 没有借书。")


class Library:
    """定义图书馆类"""
    def __init__(self):
        self.books_list = []  # 图书馆中的书籍列表
        self.members_list = []  # 图书馆中的会员列表

    def add_book(self, book):
        """添加书籍到图书馆"""
        self.books_list.append(book)
        print(f"图书馆已添加书籍：{book.book_name}")

    def add_member(self, member):
        """添加会员到图书馆"""
        self.members_list.append(member)
        print(f"图书馆已添加会员：{member.member_name}")

    def borrow_books(self, member, book):
        """借书方法"""
        if book in self.books_list:
            member.borrow_books(book)
            self.books_list.remove(book)
            print(f"《{book.book_name}》已借出。")
        else:
            print(f"《{book.book_name}》没有这本书了。")

    def return_books(self, member, book):
        """还书方法"""
        member.return_books(book)
        self.books_list.append(book)
        print(f"《{book.book_name}》已归还。")


# 创建书籍
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book2 = Book("1984", "George Orwell", 1949)
book3 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

# 创建会员
member1 = Member("Alice")
member2 = Member("Bob")

# 创建图书馆
library = Library()

# 添加图书到图书馆
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# 添加会员到图书馆
library.add_member(member1)
library.add_member(member2)

# 借书
library.borrow_books(member1, book1)
library.borrow_books(member2, book2)

# 查看会员借书情况
member1.show_borrowed_books()
member2.show_borrowed_books()

# 归还书籍
library.return_books(member1, book1)
library.return_books(member2, book2)

# 查看归还后的书籍情况
member1.show_borrowed_books()
member2.show_borrowed_books()

    
        
             


















