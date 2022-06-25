'''
This code is used to process the summer data in 2021，by person
'''
import pandas as pd
import csv
import seaborn as sns
import matplotlib.pyplot as plt


def plt_summer():
    # 读取2021年夏季数据并查看PMV分布
    df = pd.read_csv('../dataset/dataset1/summer_2021_by_person.csv', encoding="gbk")
    df.dropna(axis=0, how='any')

    names = ['卞云山', '柴臻豪', '程延', '杜帅飞', '段婷芳', '付业琛', '何向萌', '贺思哲', '吉睿琨', '李佳欣',
             '李新路', '李星奇', '李杨', '李宇婷', '李子文', '梁天堡', '刘亚萍', '吕晓亮', '乔潇逸', '邵柯',
             '邵世彪', '申沅均', '沈婷', '田颖', '王青乙', '魏亚鹏', '杨晨阳', '杨雨洁', '余俊', '余香南', '袁丹夫',
             '张栋', '张艺潇', '张远东', '张悦仙', '赵浩铭', '赵艳玲', '朱济琛']

    for i in range(len(names)):
        data = df.loc[df["no"] == i]
        pmv_distribution = sns.kdeplot(data['thermal sensation'], shade=True)
        pmv_distribution.axes.set_title('no {} \'s distribution plot of 2021 summer'.format(str(i)), fontsize=10)
        pmv_distribution.set_xlabel('pmv', fontsize=10)
        pmv_distribution.set_ylabel('density', fontsize=10)
        plt.savefig('./result/summer/no {} \'s distribution plot of 2021 summer'.format(str(i)), dpi=200,
                    bbox_inches='tight')
        plt.show()

    temp_distribution = sns.kdeplot(data['temp'], shade=True)
    temp_distribution.axes.set_title('temp distribution plot of 2021 summer', fontsize=10)
    temp_distribution.set_xlabel('temp', fontsize=10)
    temp_distribution.set_ylabel('density', fontsize=10)
    plt.savefig('./result/summer/temp distribution plot of 2021 summer', dpi=200,
                bbox_inches='tight')
    plt.show()

    humid_distribution = sns.kdeplot(data['humid'], shade=True)
    humid_distribution.axes.set_title('humid distribution plot of 2021 summer', fontsize=10)
    humid_distribution.set_xlabel('humid', fontsize=10)
    humid_distribution.set_ylabel('density', fontsize=10)
    plt.savefig('./result/summer/humid distribution plot of 2021 summer', dpi=200,
                bbox_inches='tight')
    plt.show()



def plt_winter():
    # 读取2021年冬季季数据并查看PMV分布
    df = pd.read_csv('../dataset/dataset1/winter_2021_by_person.csv', encoding="gbk")
    df.dropna(axis=0, how='any')
    names = ['边策', '曹天翔', '董翔翔', '杜帅飞', '高泱晗',
             '顾腾', '顾妍', '侯江伟', '吉睿琨', '李佳欣',
             '李星奇', '李杨', '李子文', '刘家丞', '刘亚萍',
             '乔潇逸', '苏莹', '田颖', '王洁', '王秦龙',
             '王青乙', '王姝婕', '王钰琳', '魏冬阳', '魏佳利',
             '魏亚鹏', '武龙坤', '余俊', '袁丹夫', '张艺潇',
             '张源鸿', '张远东', '赵国梁', '郑超', '周春翔']
    for i in range(len(names)):
        data = df.loc[df["no"] == i]
        pmv_distribution = sns.kdeplot(data['thermal sensation'], shade=True)
        pmv_distribution.axes.set_title('no {} \'s pmv distribution plot of 2021 winter'.format(str(i)), fontsize=10)
        pmv_distribution.set_xlabel('pmv', fontsize=10)
        pmv_distribution.set_ylabel('density', fontsize=10)
        plt.savefig('./result/winter/no {} \'s pmv distribution plot of 2021 winter'.format(str(i)), dpi=200,
                    bbox_inches='tight')
        plt.show()

    temp_distribution = sns.kdeplot(data['temp'], shade=True)
    temp_distribution.axes.set_title('temp distribution plot of 2021 winter', fontsize=10)
    temp_distribution.set_xlabel('temp', fontsize=10)
    temp_distribution.set_ylabel('density', fontsize=10)
    plt.savefig('./result/winter/temp distribution plot of 2021 winter', dpi=200,
                bbox_inches='tight')
    plt.show()

    humid_distribution = sns.kdeplot(data['humid'], shade=True)
    humid_distribution.axes.set_title('humid distribution plot of 2021 winter', fontsize=10)
    humid_distribution.set_xlabel('humid', fontsize=10)
    humid_distribution.set_ylabel('density', fontsize=10)
    plt.savefig('./result/winter/humid distribution plot of 2021 winter', dpi=200,
                bbox_inches='tight')
    plt.show()


# 查看相关性

def corr():

    # 读取2021年夏季数据并并查看相关性
    df = pd.read_csv('../dataset/dataset1/summer_2021_by_person.csv', encoding="gbk")
    df.dropna(axis=0, how='any')
    print("2021年夏季各参数与热投票值之间的相关性分析如下：")
    result1 = df.corr()['thermal sensation'].sort_values()
    print(result1)
    # 选取相关性最强的6个

    most_correlated = df.corr().abs()['thermal sensation'].sort_values(ascending=False)

    most_correlated = most_correlated[:7]
    print("2021夏季相关性最强5个参数：")
    print(most_correlated)
    # 读取2021年秋季数据并查看相关性
    df = pd.read_csv('../dataset/dataset1/winter_2021_by_person.csv', encoding="gbk")
    df.dropna(axis=0, how='any')
    print("2021年冬季各参数与热投票值之间的相关性分析如下：")
    # result2 = df.corr()['thermal sensation'].sort_values()
    # print(result2)

    most_correlated = df.corr().abs()['thermal sensation'].sort_values(ascending=False)

    most_correlated = most_correlated[:7]
    print("2021夏季相关性最强5个参数：")
    print(most_correlated)


if __name__ == '__main__':
    # plt_summer()
    # plt_winter()
    corr()
