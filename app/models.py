from sqlalchemy import Column, String, Integer, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask import redirect
from app import db, admin
from flask_login import UserMixin, current_user, logout_user


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

    def __str__(self):
        return self.name

    def is_accessible(self):
        return current_user.is_authenticated


class Bangcap(db.Model):
    __tablename__ = "bangcap"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    employee = relationship('Employee', backref='bangcap', lazy=True)

    def __str__(self):
        return self.name


class Bophan(db.Model):
    __tablename__ = "bophan"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    employee = relationship('Employee', backref='bophan', lazy=True)

    def __str__(self):
        return self.name


class Employee(db.Model):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String(50), nullable=False)
    address = Column(String(255))
    birthday = Column(Date)
    phone = Column(String(10))
    bangcap_id = Column(Integer, ForeignKey(Bangcap.id), nullable=False)
    bophan_id = Column(Integer, ForeignKey(Bophan.id), nullable=False)

    def __str__(self):
        return self.name


class Loaidocgia(db.Model):
    __tablename__ = "loaidocgia"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    reader = relationship('Reader', backref='loaidocgia', lazy=True)

    def __str__(self):
        return self.name


class Reader(db.Model):
    __tablename__ = "docgia"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String(50), nullable=False)
    loaidocgia_id = Column(Integer, ForeignKey(Loaidocgia.id), nullable=False)
    birthday = Column(Date)
    address = Column(String(255))
    email = Column(String(50))
    createdate = Column(Date)
    nhanvien_id = Column(Integer, ForeignKey(Employee.id), nullable=False)

    def __str__(self):
        return self.name


class Loaisach(db.Model):
    __tablename__ = "loaisach"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    book = relationship('Book', backref='loaisach', lazy=True)

    def __str__(self):
        return self.name


class Book(db.Model):
    __tablename__ = "sach"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    loaisach_id = Column(Integer, ForeignKey(Loaisach.id), nullable=False)
    author = Column(String(50))
    namxuatban = Column(String(4))
    nxb = Column(String(50))
    createdate = Column(Date)
    price = Column(Integer)
    nhanvien_id = Column(Integer, ForeignKey(Employee.id), nullable=False)

    def __str__(self):
        return self.name


class LogoutView(BaseView):
    @expose("/")
    def index(self):
        logout_user()

        return redirect("/admin")

    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(ModelView(Employee, db.session))
admin.add_view(ModelView(Bophan, db.session))
admin.add_view(ModelView(Bangcap, db.session))
admin.add_view(ModelView(Reader, db.session))
admin.add_view(ModelView(Loaidocgia, db.session))
admin.add_view(LogoutView(name="Logout"))

if __name__ == "__main__":
    db.create_all()
