#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2020/4/15
"""

import random
import math


# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


    if name=="ʯͷ":
        player_choice=0
    elif name=="ʷ����":
        player_choice=1
    elif name=="ֽ":
        player_choice=2
    elif name=="����":
        player_choice=3
    elif name=="����":
        player_choice=4
    else:
        player_choice=5
    return player_choice

def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

    if number==0:
	    comp_choice="ʯͷ"
    elif number==1:
        comp_choice="ʷ����"  
    elif number==2:
        comp_choice3="ֽ"          
    elif number==3:
        comp_choice="����"
    else:    
	    comp_choice="����"
    return comp_choice


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�
    
    player_choice_number=name_to_number(player_choice)
    if player_choice_number==5:
        print("Error:No Correct Name")
    else:
        comp_number=random.randrange(5)
        com_choice=number_to_name(comp_number)
        print("�������ѡ��Ϊ:%s"%(com_choice))
        if comp_number==player_choice_number:
            print("���ͼ��������һ����")
        elif comp_number>player_choice_number:
            print("�����Ӯ��")
        else:
            print("��Ӯ��")


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


