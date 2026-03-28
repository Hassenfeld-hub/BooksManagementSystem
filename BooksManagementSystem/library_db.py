import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
import datetime

# ================= 数据库配置 =================
# 请确保这里的信息和你Navicat里的一致
import json
import os
import sys


# ================= 数据库配置加载逻辑 (安全版) =================
def load_config():
    # 1. 这里是“默认配置” (已脱敏)
    # 这里的密码必须改为空，或者填个假数据。
    default_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',  # <--- 注意：这里留空，或者写 'YOUR_PASSWORD'
        'database': 'booksmanagementsystem',
        'charset': 'utf8mb4'
    }

    config_file = 'config.json'

    # 2. 尝试读取外置文件 (核心逻辑)
    if os.path.exists(config_file):
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
                print(f"成功加载外置配置文件: {config_file}")
                return config
        except Exception as e:
            print(f"配置文件读取失败: {e}，将使用默认配置")
            return default_config
    else:
        # 如果找不到 config.json，就会用上面的 default_config (空密码)
        # 这会导致连接失败，但保护了你的隐私。
        print("提示：未找到 config.json 配置文件，将尝试使用默认（空）密码连接...")
        return default_config


# 初始化全局配置变量
DB_CONFIG = load_config()


# ================= 数据库操作类 (保持不变) =================
class DBManager:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = pymysql.connect(**DB_CONFIG)
            self.cursor = self.conn.cursor()
            return True
        except Exception as e:
            messagebox.showerror("连接错误", f"无法连接数据库: {e}")
            return False

    def close(self):
        if self.cursor: self.cursor.close()
        if self.conn: self.conn.close()

    def query(self, sql, params=None):
        self.connect()
        try:
            self.cursor.execute(sql, params)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            messagebox.showerror("查询错误", str(e))
            return []
        finally:
            self.close()

    def execute(self, sql, params=None):
        self.connect()
        try:
            self.cursor.execute(sql, params)
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror("执行错误", str(e))
            return False
        finally:
            self.close()


# ================= 主应用程序类 =================
class LibrarySystem:
    def __init__(self, root):
        self.root = root
        self.root.title("图书管理系统")
        self.root.geometry("1000x600")
        self.db = DBManager()

        # 存储当前登录用户信息
        self.current_user = None
        self.user_role = None  # 'admin' 或 'reader'

        self.show_login_frame()

    # ================= 1. 登录界面 (修改点) =================
    def show_login_frame(self):
        self.clear_frame()
        frame = tk.Frame(self.root)
        frame.pack(pady=80)

        tk.Label(frame, text="图书管理系统", font=("黑体", 24, "bold")).grid(row=0, column=0, columnspan=2, pady=20)

        # 用户名
        tk.Label(frame, text="账号:").grid(row=1, column=0, pady=10)
        self.entry_user = tk.Entry(frame, font=("Arial", 12))
        self.entry_user.grid(row=1, column=1, pady=10)
        # 默认填一个读者账号方便测试 (PDF里的张三)
        # self.entry_user.insert(0, "zhangsan")

        # 密码
        tk.Label(frame, text="密码:").grid(row=2, column=0, pady=10)
        self.entry_pass = tk.Entry(frame, show="*", font=("Arial", 12))
        self.entry_pass.grid(row=2, column=1, pady=10)
        self.entry_pass.insert(0, "123456")

        # 身份选择
        tk.Label(frame, text="身份:").grid(row=3, column=0, pady=10)
        self.var_role = tk.StringVar(value="reader")  # 默认选中读者

        radio_frame = tk.Frame(frame)
        radio_frame.grid(row=3, column=1, sticky="w")
        tk.Radiobutton(radio_frame, text="读者", variable=self.var_role, value="reader").pack(side="left", padx=5)
        tk.Radiobutton(radio_frame, text="管理员", variable=self.var_role, value="admin").pack(side="left", padx=5)

        # 登录按钮
        tk.Button(frame, text="登  录", font=("Arial", 12), width=20, bg="#007bff", fg="white",
                  command=self.login).grid(row=4, column=0, columnspan=2, pady=30)

    def login(self):
        user = self.entry_user.get()
        pwd = self.entry_pass.get()
        role = self.var_role.get()

        if role == "admin":
            # 管理员查 admin 表
            sql = "SELECT * FROM admin WHERE username=%s AND password=%s"
            res = self.db.query(sql, (user, pwd))
            if res:
                self.current_user = res[0]  # (id, user, pwd)
                self.user_role = "admin"
                self.show_admin_interface()
            else:
                messagebox.showerror("错误", "管理员账号或密码错误")

        elif role == "reader":
            # 读者查 reader_card 表
            sql = "SELECT reader_id, username FROM reader_card WHERE username=%s AND password=%s"
            res = self.db.query(sql, (user, pwd))
            if res:
                self.current_user = res[0]  # (reader_id, username)
                self.user_role = "reader"
                self.show_reader_interface()
            else:
                messagebox.showerror("错误", "读者账号或密码错误")

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ================= 2. 管理员界面 (保持原有逻辑) =================
    def show_admin_interface(self):
        self.clear_frame()
        # 顶部栏
        menu_frame = tk.Frame(self.root, bg="#dddddd", height=40)
        menu_frame.pack(fill="x")
        tk.Label(menu_frame, text=f"当前管理员: {self.current_user[1]}", bg="#dddddd").pack(side="left", padx=10)
        tk.Button(menu_frame, text="退出登录", command=self.show_login_frame).pack(side="right", padx=10, pady=5)

        # 选项卡
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.tab_books = tk.Frame(notebook)
        self.tab_lend = tk.Frame(notebook)
        self.tab_reader = tk.Frame(notebook)

        notebook.add(self.tab_books, text="图书管理")
        notebook.add(self.tab_lend, text="借阅管理")
        notebook.add(self.tab_reader, text="读者管理")

        self.init_admin_book_tab()
        self.init_admin_lend_tab()
        self.init_admin_reader_tab()

    # --- 管理员功能实现 (简化版) ---
    def init_admin_book_tab(self):
        # 搜索栏
        f = tk.Frame(self.tab_books)
        f.pack(fill="x", pady=5)
        self.search_var = tk.StringVar()
        tk.Entry(f, textvariable=self.search_var).pack(side="left", padx=5)
        tk.Button(f, text="搜书名", command=self.admin_load_books).pack(side="left")
        tk.Button(f, text="录入新书", command=self.popup_add_book, bg="lightgreen").pack(side="right", padx=10)

        # 表格
        cols = ("ID", "书名", "作者", "出版社", "ISBN", "库存")
        self.tree_books = ttk.Treeview(self.tab_books, columns=cols, show="headings")
        for c in cols: self.tree_books.heading(c, text=c)
        self.tree_books.pack(fill="both", expand=True)
        self.admin_load_books()

    def admin_load_books(self):
        key = self.search_var.get()
        sql = "SELECT book_id, name, author, publish, ISBN, number FROM book_info WHERE name LIKE %s"
        rows = self.db.query(sql, (f'%{key}%',))
        for i in self.tree_books.get_children(): self.tree_books.delete(i)
        for r in rows: self.tree_books.insert("", "end", values=r)

    def popup_add_book(self):
        # 简单的录入弹窗
        win = tk.Toplevel(self.root)
        win.title("录入图书")
        fields = ["ID", "书名", "作者", "出版社", "ISBN", "语言", "价格", "日期", "库存", "分类ID"]
        entries = []
        for i, txt in enumerate(fields):
            tk.Label(win, text=txt).grid(row=i, column=0)
            e = tk.Entry(win)
            e.grid(row=i, column=1)
            entries.append(e)

        def save():
            vals = [e.get() for e in entries]
            if self.db.execute("INSERT INTO book_info VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", vals):
                messagebox.showinfo("成功", "录入成功")
                win.destroy()
                self.admin_load_books()

        tk.Button(win, text="保存", command=save).grid(row=len(fields), columnspan=2)

    def init_admin_lend_tab(self):
        # 借书操作
        f = tk.Frame(self.tab_lend)
        f.pack(fill="x", pady=5)
        tk.Label(f, text="读者ID:").pack(side="left")
        self.ent_rid = tk.Entry(f, width=8);
        self.ent_rid.pack(side="left")
        tk.Label(f, text="图书ID:").pack(side="left")
        self.ent_bid = tk.Entry(f, width=8);
        self.ent_bid.pack(side="left")
        tk.Button(f, text="确认借出", command=self.admin_lend_book).pack(side="left", padx=10)

        # 列表
        cols = ("流水号", "书名", "读者", "借出日期", "应还日期")
        self.tree_lend = ttk.Treeview(self.tab_lend, columns=cols, show="headings")
        for c in cols: self.tree_lend.heading(c, text=c)
        self.tree_lend.pack(fill="both", expand=True)
        self.admin_load_lends()

    def admin_load_lends(self):
        sql = """SELECT l.ser_num, b.name, r.name, l.lend_date, l.back_date 
                 FROM lend_list l 
                 JOIN book_info b ON l.book_id=b.book_id 
                 JOIN reader_info r ON l.reader_id=r.reader_id ORDER BY l.ser_num DESC"""
        rows = self.db.query(sql)
        for i in self.tree_lend.get_children(): self.tree_lend.delete(i)
        for r in rows: self.tree_lend.insert("", "end", values=r)

    def admin_lend_book(self):
        rid = self.ent_rid.get()
        bid = self.ent_bid.get()
        # 简单校验
        if not rid or not bid: return
        # 事务：减库存+加记录
        try:
            self.db.connect()
            cur = self.db.conn.cursor()
            # 查库存
            cur.execute("SELECT number FROM book_info WHERE book_id=%s", (bid,))
            stock = cur.fetchone()
            if not stock or stock[0] < 1:
                messagebox.showerror("错误", "库存不足或书籍不存在")
                return

            today = datetime.date.today()
            back = today + datetime.timedelta(days=30)

            cur.execute("UPDATE book_info SET number=number-1 WHERE book_id=%s", (bid,))
            cur.execute("INSERT INTO lend_list (book_id, reader_id, lend_date, back_date) VALUES (%s,%s,%s,%s)",
                        (bid, rid, today, back))
            self.db.conn.commit()
            messagebox.showinfo("成功", "借阅成功")
            self.admin_load_lends()
            self.admin_load_books()
        except Exception as e:
            self.db.conn.rollback()
            messagebox.showerror("失败", str(e))
        finally:
            self.db.close()

    def init_admin_reader_tab(self):
        cols = ("ID", "姓名", "电话", "地址")
        self.tree_reader = ttk.Treeview(self.tab_reader, columns=cols, show="headings")
        for c in cols: self.tree_reader.heading(c, text=c)
        self.tree_reader.pack(fill="both", expand=True)
        rows = self.db.query("SELECT reader_id, name, phone, address FROM reader_info")
        for r in rows: self.tree_reader.insert("", "end", values=r)

    # ================= 3. 读者界面 (新增功能) =================
    def show_reader_interface(self):
        self.clear_frame()
        # 读者顶部栏
        reader_id = self.current_user[0]
        reader_name = self.current_user[1]

        # 获取读者真实姓名
        real_name_res = self.db.query("SELECT name FROM reader_info WHERE reader_id=%s", (reader_id,))
        real_name = real_name_res[0][0] if real_name_res else reader_name

        menu_frame = tk.Frame(self.root, bg="#e6f7ff", height=40)
        menu_frame.pack(fill="x")
        tk.Label(menu_frame, text=f"欢迎你，{real_name}", bg="#e6f7ff", font=("Arial", 12)).pack(side="left", padx=10)
        tk.Button(menu_frame, text="退出登录", command=self.show_login_frame).pack(side="right", padx=10, pady=5)

        # 读者选项卡
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.tab_my_books = tk.Frame(notebook)
        self.tab_search = tk.Frame(notebook)
        self.tab_profile = tk.Frame(notebook)

        notebook.add(self.tab_my_books, text="我的借阅")
        notebook.add(self.tab_search, text="图书查询")
        notebook.add(self.tab_profile, text="个人信息")

        self.init_reader_my_books()
        self.init_reader_search()
        self.init_reader_profile()

    def init_reader_my_books(self):
        # 显示当前登录读者的借阅记录
        cols = ("图书名称", "借出日期", "应还日期")
        tree = ttk.Treeview(self.tab_my_books, columns=cols, show="headings")
        for c in cols: tree.heading(c, text=c)
        tree.pack(fill="both", expand=True)

        rid = self.current_user[0]
        sql = """
            SELECT b.name, l.lend_date, l.back_date
            FROM lend_list l
            JOIN book_info b ON l.book_id = b.book_id
            WHERE l.reader_id = %s
            ORDER BY l.lend_date DESC
        """
        rows = self.db.query(sql, (rid,))
        for r in rows: tree.insert("", "end", values=r)

    def init_reader_search(self):
        # 读者只能查，不能改
        f = tk.Frame(self.tab_search)
        f.pack(fill="x", pady=5)
        self.reader_search_var = tk.StringVar()
        tk.Entry(f, textvariable=self.reader_search_var).pack(side="left", padx=5)

        def do_search():
            key = self.reader_search_var.get()
            sql = "SELECT name, author, publish, price, number FROM book_info WHERE name LIKE %s"
            rows = self.db.query(sql, (f'%{key}%',))
            for i in tree.get_children(): tree.delete(i)
            for r in rows: tree.insert("", "end", values=r)

        tk.Button(f, text="查询", command=do_search).pack(side="left")

        cols = ("书名", "作者", "出版社", "价格", "剩余库存")
        tree = ttk.Treeview(self.tab_search, columns=cols, show="headings")
        for c in cols: tree.heading(c, text=c)
        tree.pack(fill="both", expand=True)

        # 默认加载所有
        do_search()

    def init_reader_profile(self):
        # 显示个人信息
        rid = self.current_user[0]
        sql = "SELECT * FROM reader_info WHERE reader_id=%s"
        res = self.db.query(sql, (rid,))

        frame = tk.Frame(self.tab_profile, padx=20, pady=20)
        frame.pack(anchor="w")

        if res:
            info = res[0]  # (id, name, sex, birth, address, phone)
            # 简单的展示
            labels = [f"卡号: {info[0]}", f"姓名: {info[1]}", f"性别: {info[2]}",
                      f"生日: {info[3]}", f"地址: {info[4]}", f"电话: {info[5]}"]
            for txt in labels:
                tk.Label(frame, text=txt, font=("Arial", 14), pady=5).pack(anchor="w")
        else:
            tk.Label(frame, text="未找到详细信息").pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = LibrarySystem(root)
    root.mainloop()
