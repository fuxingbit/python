#Author: Jenliver

data = {
    '北京': {
        '昌平': {
            '沙河': ["XDL", "oldboy"],
            '天通苑': ["链家", "我爱我家"]
        },
        '朝阳': {
            '望京': ["奔驰", "陌陌"],
            '国贸': ["CICC", "HP"]
        }
    },
    '山东': {
        '德州': {
            '沙河': ["XDL", "oldboy"],
            '天通苑': ["链家", "我爱我家"]
        },
        '烟台': {
            '望京': ["奔驰", "陌陌"],
            '国贸': ["CICC", "HP"]
        }
    }
}
while True:
    for i in data:
        print(i)
    choice = input("选择进入1>>>>:")
    if choice in data:
        while True:
            for i2 in data[choice]:
                print("\t", i2)
            choice2 = input("选择进入2>>>>:")
            if choice2 in data[choice]:
                while True:
                    for i3 in data[choice][choice2]:
                        print("\t\t", i3)
                    choice3 = input("选择进入3>>>>:")
                    if choice3 in data[choice][choice2]:
                        for i4 in  data[choice][choice2][choice3]:
                            print("\t\t\t", i4)
                        choice4 = input("最后一层，按b返回，按q退出>>>>:")
                        if choice4 == "b":
                            pass
                        elif choice4 == "q":
                            exit()
                    if choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit()
            if choice2 == "b":
                break
            elif choice2 == "q":
                exit()

    else:
        print("你的输入不存在，请重新输入")