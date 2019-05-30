# vessel loading

## 部署说明
### step1
#### 相关包依赖
    pip module list
    mysqlclient
### step2
#### 新建数据库 
        login mysql account in cmd control panel
    
```mysql
    CREATE DATABASE final_vessel CHARACTER SET 'utf8';
```
### step3
#### django 
        change PASSWORD settings.py 

```shell
    python manage.py makemigrations
```

```shell
    python manage.py migrate
```

### step4
#### 堆场数据导入
        mysql cmd panel
```mysql
    use final_vessel;
```

```mysql
    source 文件路径

    example：
    source C:\\Users\\wode2\\Desktop\\vessel\\LE-FINAL-DESIGN\\server\\vessel\\yardmon_yard.sql;
```
