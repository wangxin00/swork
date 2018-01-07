DELETE FROM s_t_course;
DELETE FROM course;
DELETE FROM student;
DELETE FROM teacher;

INSERT INTO student (no, name, gender, cl)  VALUES
    ('S001',  '王五',  '男',  '101'),
    ('S002',  '马六',  '女',  '101'),
    ('S003',  '李勇',  '男',  '102'),
    ('S004',  '刘晨',  '女',  '102');
INSERT INTO course (no, name)  VALUES 
    ('C01',  '高数'), 
    ('C02',  '外语'),
    ('C03',  '线代'),
    ('C04',  '物理');
INSERT INTO teacher (no, name, gender)  VALUES
    ('T001',  '张立',  '男'),
    ('T002',  '王敏',  '女'), 
    ('T003',  '冯灵',  '女'),
    ('T004',  '李华',  '男');
INSERT INTO s_t_course (cou_no, tea_no, stu_no, time, place)  VALUES 
    ('C01',  'T001',   'S001',  '周一第一节 8:20-10:00',  '一教A101'), 
    ('C03',  'T003',   'S001',  '周二第三节14:00-15:40',  '一教A303'),
    ('C04',  'T004',   'S001',  '周三第一节 8:20-10:00',  '一教A404'),
    ('C02',  'T002',   'S001',  '周四第二节10:20-12:00',  '一教A202'),
    ('C02',  'T002',   'S003',  '周一第二节10:20-12:00',  '一教A202'),
    ('C01',  'T001',   'S003',  '周二第一节 8:20-10:00',  '一教A101'),
    ('C03',  'T003',   'S003',  '周三第三节14:00-15:40',  '一教A303'),
    ('C04',  'T004',   'S003',  '周四第二节10:20-12:00',  '一教A404');



    