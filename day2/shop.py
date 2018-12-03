#Author: Jenliver

product_list = [
    ('Iphone', 5800),
    ('Mac Pro', 9800),
    ('Bike', 1800),
    ('Watch', 10000),
    ('Book', 80)
]
shop_list = []
salary = input("请输入您带了多少钱:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index, item in enumerate(product_list):
            #print(product_list.index(item), item)
            print(index, item)
        user_choice = input("请选择商品编号进行购买，按【q】键退出>>>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:   #买的起
                    shop_list.append(p_item)
                    salary -= p_item[1]
                    print("将商品 %s 加入到购物车,您的余额还有 \033[31;1m%s\033[0m" %(p_item, salary))
                else:
                    print("\033[32;1m你的余额只剩[%s]了，还买个毛线\033[0m" % salary)
            else:
                print("商品[%s]不存在。" % user_choice)
        elif user_choice == 'q':
            print('-----------shopping list-------------')
            for p in shop_list:
                print(p)
            print("您的余额还有:", salary)
            exit()
        else:
            print('Invalid option')
else:
    print("请输入数字")


招聘：运维工程师  薪资2W左右
要求：3年左右经验
      ELK、Python用的熟，docker玩的6
      Nginx Tomcat Redis MongoDB MySQL RabbitMQ kafka等熟练
坐标：北京东三环  呼家楼地铁站（6号线，10号线）
有意向请发简历   zjn@fuyinhy.com
