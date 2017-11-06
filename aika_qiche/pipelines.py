# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import hashlib
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.exceptions import DropItem
from aika_qiche.items import AikaQicheItem


class MysqlPipeline(object):
	def __init__(self):
		self.conn = pymysql.connect(host='172.31.215.38', port=3306, user='spider', password='spider', db='spider',
		                            charset='utf8', cursorclass=pymysql.cursors.DictCursor)
		self.cursor = self.conn.cursor()
		self.item_list = []
		dispatcher.connect(self.spider_closed, signals.spider_closed)

	def spider_closed(self, spider):
		print("spider closed")
		sql = """insert into che_aika (cat, comp_name, comp_url, phone, addr, intro, short, jibie) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""
		self.cursor.executemany(sql, self.item_list)
		self.conn.commit()
		print('%s insert' % len(self.item_list))

	def process_item(self, item, spider):
		print(str(item['comp_url']) + ' ' + str(item['comp_name']))
		if isinstance(item, AikaQicheItem):
			if len(self.item_list) == 10:
				sql = """insert into che_aika_copy (cat, comp_name, comp_url, phone, addr, intro, short, jibie) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""
				self.cursor.executemany(sql, self.item_list)
				self.conn.commit()
				self.item_list.clear()
				print('200 insert')
			else:
				self.item_list.append(
					[item['cat'], item['comp_name'], item['comp_url'], item['phone'], item['addr'], item['intro'],
					 item['short'], item['jibie']])


class DuplicatesPipeline(object):
	def __init__(self):
		self.item_set = set()

	def process_item(self, item, spider):
		m = self.gen_md5(item['comp_url'])
		if m in self.item_set:
			raise DropItem("Duplicate item found")
		else:
			self.item_set.add(m)
			return item

	def gen_md5(self, comp_name):
		"""
		生成唯一id
		:return:
		0cc2662f5eb157c8ffcd43c145de499f2ab27a71
		72843135390705548651698998647502012318670289521
		a3f4a5b080e2a4ef4a708b9c9f5ad003
		217934444328053067635429399579879723011
		"""
		m = hashlib.md5()
		m.update(comp_name.encode('utf-8'))
		comp_md5 = m.hexdigest()
		# only_id_full = int(comp_md5, 16)
		# return str(only_id_full)
		return comp_md5
