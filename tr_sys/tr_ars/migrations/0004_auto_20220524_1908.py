# # Generated by Django 3.2.4 on 2022-05-24 19:08
#
# from django.db import migrations, models
#
#
# class Migration(migrations.Migration):
#
#     dependencies = [
#         ('tr_ars', '0003_auto_20211109_1820'),
#     ]
#
#     operations = [
#         migrations.RemoveConstraint(
#             model_name='actor',
#             name='unique_actor',
#         ),
#         migrations.AlterField(
#             model_name='actor',
#             name='channel',
#             field=models.JSONField(null=True),
#         ),
#         migrations.AddConstraint(
#             model_name='actor',
#             constraint=models.UniqueConstraint(fields=('agent', 'path'), name='unique_actor'),
#         ),
#     ]