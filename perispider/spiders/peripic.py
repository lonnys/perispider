# -*- coding: utf-8 -*-
import scrapy
import urlparse
from scrapy.http import Request, FormRequest
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from perispider.items import PerispiderItem


class PeripicSpider(CrawlSpider):
	name = 'peripic'
	allowed_domains = ['22mm.cc']
	start_urls = ['http://www.22mm.cc/mm/qingliang/',
					'http://www.22mm.cc/mm/jingyan/',
					'http://www.22mm.cc/mm/bagua/',
					'http://www.22mm.cc/mm/suren/']
	def parse(self, response):
		'''
		处理分类页面翻页功能
		取分类页面中的不同风格的美女图片
		'''
		nextname = response.xpath('//div[@class="ShowPage"]//a/text()').extract()[-1]
		if nextname == u">":
			nexturl = response.xpath('//div[@class="ShowPage"]//a/@href').extract()[-1]
			nexturl = urlparse.urljoin(response.url, nexturl)
			# 对于下一分类页面直接回调当前的分析函数
			yield Request(nexturl, callback=self.parse)

		#picurl = response.xpath('//div[@class="c_inner"]//a/@href').extract()[7:-5]
		picurl = response.xpath('//div[@class="c_inner"]//a/@href').extract()[7:13]
		for purl in picurl:
			purl = urlparse.urljoin(response.url, purl)
			# 对不同风格的图片页面进行分析
			yield Request(purl, callback=self.styleparse)

	def styleparse(self, response):
		'''
		对不同风格美女页面进行分析
		处理翻页功能
		'''
		try:
			nextname = response.xpath('//div[@class="ShowPage"]//a/text()').extract()[-1]
			if nextname == u"\u4e0b\u4e00\u9875":
				nexturl1 = response.xpath('//div[@class="ShowPage"]//a/@href').extract()[-1]
				nexturl1 = urlparse.urljoin(response.url, nexturl1)
				yield Request(nexturl1, callback=self.picsrcparse)
		except:
			pass

		try:
			nexturl2 = response.xpath('//div[@class="lipagebtn"]//a[@class="nextp"]/@href').extract()
			nexturl2 = urlparse.urljoin(response.url, nexturl2)
			yield Request(nexturl2, callback=self.picsrcparse)
		except:
			pass
	
	def picsrcparse(self, response):
		'''
		对风格页面中的片页面进行分析
		提取图片URL地址
		将图片地址写入Json
		'''
		pictext = "".join(response.xpath('//script/text()').extract())
		for i in pictext.split(';'):
			if i.find('arrayImg[') >= 0:
				try:
					src = i.split('"')[1].replace('big','pic')
					self.log("PIC:%s"%src)
					yield PerispiderItem(url=src)
				except:
					continue
