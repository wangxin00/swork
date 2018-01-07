DROP DATABASE IF EXISTS classdb;

DROP ROLE IF EXISTS classdb; 

-- 创建一个登陆角色（用户），用户名classdbo, 缺省密码pass
CREATE ROLE classdbo LOGIN
  ENCRYPTED PASSWORD 'md568cefad35fed037c318b1e44cc3480cf' -- password: pass
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE;

CREATE DATABASE classdb WITH OWNER = classdbo ENCODING = 'UTF8';
   

