# nsd1906_devweb_day04

## Model

```python
# 使用python shell
(nsd1906) [root@room8pc16 mysite]# python manage.py shell
# 导入模型
>>> from polls.models import Question, Choice

# 创建问题，方法一：直接创建实例
>>> q1 = Question(question_text="散伙饭去哪吃？", pub_date='2019-11-25')
>>> q1.save()

# 创建问题，方法二：使用objects管理器。django为每个实体类都创建了一个名为objects的管理，通过它的方法可以实现对模型的增删改查等操作。
# get_or_create是，如果没有相关记录则创建，如果库中已有相关记录则取出
>>> q2 = Question.objects.get_or_create(question_text="你打算到哪 个城市找工作？", pub_date="2019-12-1")

```










