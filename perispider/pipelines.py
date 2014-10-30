# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.contrib.exporter import JsonLinesItemExporter

class PerispiderPipeline(object):
	def open_spider(self, spider):
		name = "%s.json" % spider.name
		self.file = open(name, 'w')
		self.exporter = JsonLinesItemExporter(self.file)
		self.exporter.start_exporting()

	def process_item(self, item, spider):
		self.exporter.export_item(item)
		return item
