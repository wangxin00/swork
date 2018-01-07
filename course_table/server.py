# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

import dbconn
dbconn.register_dsn("host=localhost dbname=classdb user=classdbo password=pass")


class BaseReqHandler(tornado.web.RequestHandler):

    def db_cursor(self, autocommit=True):
        return dbconn.SimpleDataCursor(autocommit=autocommit)
    

class MainHandler(BaseReqHandler):
    def get(self):
        with self.db_cursor() as cur:
            sql = '''
            SELECT s_t.cou_no, s_t.tea_no, s_t.stu_no, c.name as cou_name,
                t.name as tea_name,  s_t.time, s_t.place 
            FROM s_t_course as s_t
            INNER JOIN student as s ON s_t.stu_no = s.no
            INNER JOIN teacher as t ON s_t.tea_no = t.no
            INNER JOIN course as c  ON s_t.cou_no = c.no
            ORDER BY s_t.cou_no;
            '''
            cur.execute(sql)
            items = cur.fetchall()
        self.set_header("Content-Type", "text/html; charset=UTF-8")
        self.render("list.html", title="课程表", items=items)

class StudentHandler(BaseReqHandler):
    def get(self):
        with self.db_cursor() as cur:
            sql = '''
            SELECT s_t.cou_no, s_t.tea_no, s_t.stu_no, s.name as stu_name, c.name as cou_name,
                t.name as tea_name, s.cl as stu_cl, s_t.time, s_t.place 
            FROM s_t_course as s_t
            INNER JOIN student as s ON s_t.stu_no = s.no
            INNER JOIN teacher as t ON s_t.tea_no = t.no
            INNER JOIN course as c  ON s_t.cou_no = c.no
            ORDER BY s_t.stu_no;
            '''
            cur.execute(sql)
            items = cur.fetchall()
        self.set_header("Content-Type", "text/html; charset=UTF-8")
        self.render("student.html", title="学生课表", items=items)

class TeacherHandler(BaseReqHandler):
    def get(self):
        with self.db_cursor() as cur:
            sql = '''
            SELECT s_t.cou_no, s_t.tea_no, s_t.stu_no, c.name as cou_name,
                t.name as tea_name, s.cl as stu_cl, s_t.time, s_t.place 
            FROM s_t_course as s_t
            INNER JOIN student as s ON s_t.stu_no = s.no
            INNER JOIN teacher as t ON s_t.tea_no = t.no
            INNER JOIN course as c  ON s_t.cou_no = c.no
            ORDER BY s_t.tea_no;
            '''
            cur.execute(sql)
            items = cur.fetchall()
        self.set_header("Content-Type", "text/html; charset=UTF-8")
        self.render("teacher.html", title="教师课表", items=items)

class CourseAddHandler(BaseReqHandler):
    def post(self):
        cou_no = self.get_argument("cou_no")
        tea_no = self.get_argument("tea_no")
        stu_no = self.get_argument("stu_no")
        time   = self.get_argument("time")
        place  = self.get_argument("place")
        
        with self.db_cursor() as cur:
            sql = '''INSERT INTO s_t_course 
            (cou_no, tea_no, stu_no, time, place)  VALUES(%s, %s, %s, %s, %s);'''
            cur.execute(sql, (cou_no, tea_no, stu_no, time, place))
            cur.commit()
        
        self.set_header("Content-Type", "text/html; charset=UTF-8") 
        self.redirect("/")

class CourseEditHandler(BaseReqHandler):
    def get(self, cou_no, tea_no, stu_no):
        cou_no, tea_no, stu_no 
        self.set_header("Content-Type", "text/html; charset=UTF-8")
        with self.db_cursor() as cur:
            sql = '''
            SELECT time, place FROM s_t_course
                WHERE cou_no = %s AND tea_no = %s AND stu_no = %s;
            '''
            cur.execute(sql, (cou_no, tea_no, stu_no))
            row = cur.fetchone()
            if row:
                self.render("edit.html",  cou_no=cou_no, tea_no = tea_no,
                stu_no= stu_no, time=row[0], place=row[1])
            else:
                self.write('Not FOUND!')
    
    def post(self):
        cou_no=self.get_argument("cou_no")
        tea_no=self.get_argument("tea_no")
        stu_no=self.get_argument("stu_no")
        time = self.get_argument("time")
        place = self.get_argument("place")
        self.set_header("Content-Type", "text/html; charset=UTF-8")
        with self.db_cursor() as cur:
            sql = '''
            UPDATE s_t_course SET time=%s, place=%s
                WHERE cou_no= %s AND tea_no = %s AND stu_no = %s;'''
            cur.execute(sql, (time, place, cou_no, tea_no, stu_no))
            cur.commit()
        self.redirect("/")

class CourseDelHandler(BaseReqHandler):
    def get(self, cou_no, tea_no, stu_no):
        cou_no, tea_no, stu_no
        
        with self.db_cursor() as cur:
            sql = '''
            DELETE FROM s_t_course 
                WHERE cou_no= %s AND tea_no = %s AND stu_no = %s;'''
            cur.execute(sql, (cou_no, tea_no, stu_no))
            cur.commit()

        self.set_header("Content-Type", "text/html; charset=UTF-8")
        self.redirect("/")

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/student", StudentHandler),
    (r"/teacher", TeacherHandler),
    (r"/course.add", CourseAddHandler),
    (r"/course.edit/([A-Z0-9]+)/([A-Z0-9]+)/([A-Z0-9]+)", CourseEditHandler),
    (r"/course.del/([A-Z0-9]+)/([A-Z0-9]+)/([A-Z0-9]+)", CourseDelHandler),
], debug=True)


if __name__ == "__main__":
    application.listen(8888)
    server = tornado.ioloop.IOLoop.instance()
    tornado.ioloop.PeriodicCallback(lambda: None, 500, server).start()
    server.start()

