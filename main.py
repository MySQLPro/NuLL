import mysql.connector
import random


class MySQL_VIRTUAL:
    def __init__(self, base = None, user = "admin", passwd = "root"):
        self.sql = mysql.connector.connect \
                (
                host = "localhost",
                user = user,
                passwd = passwd,
                database = base
            )
        self.cursor = self.sql.cursor()

        self.count = -1

    def MANV(self):
        self.count += 1
        l = len(str(self.count))
        if l == 1:
            return "MS0000" + str(self.count)
        if l == 2:
            return "MS000" + str(self.count)
        if l == 3:
            return "MS00" + str(self.count)
        if l == 4:
            return "MS0" + str(self.count)
        else:
            return "MS" + str(self.count)

    def HO_TEN(self):
        A = []
        NAM = ["TRẦN VĂN", "NGUYỄN VĂN", "NGUYỄN MINH", "NGUYỄN QUỐC", "NGÔ BÁ"]
        NU = ["LÊ THỊ", "TRẦN THỊ NGỌC", "NGUYỄN HƯƠNG", "PHẠM THỊ QUỲNH", "LÊ BÍCH"]
        for i in range(65, 91):
            A += [chr(i)]

        if self.count % 2 == 0:
            rand1 = random.choice(NAM)
            rand2 = random.choice(A)
            return f"{rand1} {rand2}"
        else:
            rand1 = random.choice(NU)
            rand2 = random.choice(A)
            return f"{rand1} {rand2}"

    @staticmethod
    def NAM_SINH():
        A = []
        for i in range(1995, 2006):
            A += [i]
        return random.choice(A)

    def GIOI_TINH(self):
        if self.count % 2 == 0:
            return "NAM"
        else:
            return "NỮ"

    @staticmethod
    def CHUC_VU():
        A = ["BẢO VỆ", "LAO CÔNG", "NHÂN VIÊN", "QUẢN LÝ", "GIÁM ĐỐC", "CHỦ TỊCH"]
        return random.choice(A)

    @staticmethod
    def SDT():
        if random.randint(0, 10) % 5 == 0:
            return ""
        else:
            return "+84" + str(random.randint(100000000, 999999999))

    def INSERT_INTO(self):
        for i in range(3000):
            self.cursor.execute(f'INSERT INTO NHAN_VIEN VALUES '
                                f'("{self.MANV()}", "{self.HO_TEN()}", {self.NAM_SINH()}, '
                                f'"{self.GIOI_TINH()}", "{self.CHUC_VU()}", '
                                f'"{self.SDT()}")')

    def __del__(self):
        self.sql.commit()


SQL = MySQL_VIRTUAL("CSDL_CTY", "admin", "zxcv")
SQL.INSERT_INTO()
