# vessel loading

## 部署说明
### step1
#### 相关包依赖
```shell
pip requirement
Django         2.2
mysqlclient    1.4.1
```
### step2
#### 新建数据库 
```mysql
    CREATE DATABASE final_vessel CHARACTER SET 'utf8';
```
![Create database](/note/database_create.png)
### step3
#### django 
        change PASSWORD settings.py 
![django migration](/note/update_password.png)

```shell
    python manage.py makemigrations
```

```shell
    python manage.py migrate
```
![django migration](/note/migration.png)

### step4
#### 堆场数据导入
```mysql
    use final_vessel;
```

```mysql
    source 文件路径
```
![django migration](/note/data_import.png)
