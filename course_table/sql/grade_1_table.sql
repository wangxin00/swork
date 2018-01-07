DROP TABLE IF EXISTS student;
CREATE TABLE IF NOT EXISTS student  (
    no       VARCHAR(10), --学号
    name     TEXT,        --姓名
    gender   TEXT,        --性别(男/女)
    cl       VARCHAR(10),    --班级
    PRIMARY KEY(no)
);

-- 学号唯一
CREATE UNIQUE INDEX idx_student_no ON student(no);

DROP TABLE IF EXISTS teacher;
CREATE TABLE IF NOT EXISTS teacher  (
    no       VARCHAR(10), --教师工号
    name     TEXT,        --姓名
    gender   TEXT,        --性别(男/女)
    PRIMARY KEY(no)
);

CREATE UNIQUE INDEX idx_teacher_no ON teacher(no);

-- === 课程信息表
DROP TABLE IF EXISTS course;
CREATE TABLE IF NOT EXISTS course  (
    no       VARCHAR(10), --课程号
    name     TEXT,        --课程名称
    PRIMARY KEY(no)
);

CREATE UNIQUE INDEX idx_course_no ON course(no);

-- === 课程表
DROP TABLE IF EXISTS s_t_course;
CREATE TABLE IF NOT EXISTS s_t_course (
    cou_no VARCHAR(10),     -- 课程号
    tea_no VARCHAR(10),     -- 教师工号
    stu_no VARCHAR(10),     -- 学号
    time   TEXT,            -- 上课时间
    place  TEXT,            -- 上课地点
    PRIMARY KEY(cou_no, tea_no, stu_no)
);

ALTER TABLE s_t_course 
    ADD CONSTRAINT cou_no_fk FOREIGN KEY (cou_no) REFERENCES course(no);
ALTER TABLE s_t_course 
    ADD CONSTRAINT tea_no_fk FOREIGN KEY (tea_no) REFERENCES teacher(no);
ALTER TABLE s_t_course 
    ADD CONSTRAINT stu_no_fk FOREIGN KEY (stu_no) REFERENCES student(no);
