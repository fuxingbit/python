# @Time    : 2018/7/23 15:51
# @Author  : Jennings
# @Email   : zjn@wiwi.ink

import pymysql

# 创建连接
conn = pymysql.connect(host='106.14.3.173', port=3306, user='Jennings', passwd='um7cpphy', db='wiwi')
# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from student")

# 取结果的一条
print(cursor.fetchone())

# 取所有结果
print(cursor.fetchall())

data = {
    ('N1', 21, '广州'),
    ('N2', 18, '厦门'),
    ('N3', 19, '甘肃'),
}

# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update hosts set host = '1.1.1.2' where nid > %s", (1,))

# 执行SQL，并返回受影响行数
# effect_row = cursor.executemany("insert into student (name, age, addr) values (%s, %s, %s)", data)


# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()



