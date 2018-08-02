from scrapy import Spider
from bbref.items import BBrefItem


class bbrefSpider(Spider):
	teams = ['ATL','TOR','BOS','PHI','NYK','BRK','POR','OKC','UTA','MIN','DEN','CLE','IND','MIL','DET','CHI','GSW','LAC','LAL',
				'SAC']
	name = 'bbref_spider'
	allowed_urls = ['https://www.basketball-reference.com/']
	start_urls = ['https://www.basketball-reference.com/teams/%s/stats_basic_totals.html/' % i for i in teams]

	def parse(self, response):
		rows = response.xpath('//*[@id="stats" ]/tbody/tr')
		rows = [row for row in rows if row.xpath('./th[@aria-label]') == []]
		
		for row in rows:
			season = row.xpath('./th[1]/a/text()').extract_first()
			league = row.xpath('./td[1]/a/text()').extract_first() 
			team = row.xpath('./td[2]/a/text()').extract_first()

			if(row.xpath('./td[3]/text()').extract_first() == None):
				wins = row.xpath('./td[3]/span/strong/text()').extract_first()
			else:
				wins = row.xpath('./td[3]/text()').extract_first() #Good
			if(row.xpath('./td[4]/text()').extract_first() == None):
				losses = row.xpath('./td[4]/span/strong/text()').extract_first()
			else:
				losses = row.xpath('./td[4]/text()').extract_first() #Good
			if(row.xpath('./td[5]/text()').extract_first() == None):
				finish = row.xpath('./td[5]/span/strong/text()').extract_first()
			else:
				finish = row.xpath('./td[5]/text()').extract_first() #Good
			if(row.xpath('./td[7]/text()').extract_first() == None):
				age = row.xpath('./td[7]/span/strong/text()').extract_first()
			else:
				age = row.xpath('./td[7]/text()').extract_first() #Good
			if(row.xpath('./td[8]/text()').extract_first() == None):
				height = row.xpath('./td[8]/span/strong/text()').extract_first()
			else:
				height = row.xpath('./td[8]/text()').extract_first() #Good
			if(row.xpath('./td[9]/text()').extract_first() == None):
				weight = row.xpath('./td[9]/span/strong/text()').extract_first()
			else:
				weight = row.xpath('./td[9]/text()').extract_first() #Good
			if(row.xpath('./td[11]/text()').extract_first() == None):
				games = row.xpath('./td[11]/span/strong/text()').extract_first()
			else:
				games = row.xpath('./td[11]/text()').extract_first() #Good
			if(row.xpath('./td[12]/text()').extract_first() == None):
				mp = row.xpath('./td[12]/span/strong/text()').extract_first()
			else:
				mp = row.xpath('./td[12]/text()').extract_first() #Good
			if(row.xpath('./td[13]/text()').extract_first() == None):
				fg = row.xpath('./td[13]/span/strong/text()').extract_first()
			else:
				fg = row.xpath('./td[13]/text()').extract_first() #Good
			if(row.xpath('./td[14]/text()').extract_first() == None):
				fga = row.xpath('./td[14]/span/strong/text()').extract_first()
			else:
				fga = row.xpath('./td[14]/text()').extract_first() #Good
			if(row.xpath('./td[15]/text()').extract_first() == None):
				fga_pct = row.xpath('./td[15]/span/strong/text()').extract_first()
			else:
				fga_pct = row.xpath('./td[15]/text()').extract_first() #Good
			if(row.xpath('./td[16]/text()').extract_first() == None):
				fg3 = row.xpath('./td[16]/span/strong/text()').extract_first()
			else:
				fg3 = row.xpath('./td[16]/text()').extract_first() #Good
			if(row.xpath('./td[17]/text()').extract_first() == None):
				fg3a = row.xpath('./td[17]/span/strong/text()').extract_first()
			else:
				fg3a = row.xpath('./td[17]/text()').extract_first() #Good
			if(row.xpath('./td[18]/text()').extract_first() == None):
				fg3_pct = row.xpath('./td[18]/span/strong/text()').extract_first()
			else:
				fg3_pct = row.xpath('./td[18]/text()').extract_first() #Good
			if(row.xpath('./td[19]/text()').extract_first() == None):
				fg2 = row.xpath('./td[19]/span/strong/text()').extract_first()
			else:
				fg2 = row.xpath('./td[19]/text()').extract_first() #Good
			if(row.xpath('./td[20]/text()').extract_first() == None):
				fg2a = row.xpath('./td[20]/span/strong/text()').extract_first()
			else:
				fg2a = row.xpath('./td[20]/text()').extract_first() #Good
			if(row.xpath('./td[21]/text()').extract_first() == None):
				fg2_pct = row.xpath('./td[21]/span/strong/text()').extract_first()
			else:
				fg2_pct = row.xpath('./td[21]/text()').extract_first() #Good
			if(row.xpath('./td[22]/text()').extract_first() == None):
				ft = row.xpath('./td[22]/span/strong/text()').extract_first()
			else:
				ft = row.xpath('./td[22]/text()').extract_first() #Good
			if(row.xpath('./td[23]/text()').extract_first() == None):
				fta = row.xpath('./td[23]/span/strong/text()').extract_first()
			else:
				fta = row.xpath('./td[23]/text()').extract_first() #Good
			if(row.xpath('./td[24]/text()').extract_first() == None):
				ft_pct = row.xpath('./td[24]/span/strong/text()').extract_first()
			else:
				ft_pct = row.xpath('./td[24]/text()').extract_first() #Good
			if(row.xpath('./td[25]/text()').extract_first() == None):
				orb = row.xpath('./td[25]/span/strong/text()').extract_first()
			else:
				orb = row.xpath('./td[25]/text()').extract_first() #Good
			if(row.xpath('./td[26]/text()').extract_first() == None):
				drb = row.xpath('./td[26]/span/strong/text()').extract_first()
			else:
				drb = row.xpath('./td[26]/text()').extract_first() #Good
			if(row.xpath('./td[27]/text()').extract_first() == None):
				trb = row.xpath('./td[27]/span/strong/text()').extract_first()
			else:
				trb = row.xpath('./td[27]/text()').extract_first() #Good
			if(row.xpath('./td[28]/text()').extract_first() == None):
				ast = row.xpath('./td[28]/span/strong/text()').extract_first()
			else:
				ast = row.xpath('./td[28]/text()').extract_first() #Good
			if(row.xpath('./td[29]/text()').extract_first() == None):
				stl = row.xpath('./td[29]/span/strong/text()').extract_first()
			else:
				stl = row.xpath('./td[29]/text()').extract_first() #Good
			if(row.xpath('./td[30]/text()').extract_first() == None):
				blk = row.xpath('./td[30]/span/strong/text()').extract_first()
			else:
				blk = row.xpath('./td[30]/text()').extract_first() #Good
			if(row.xpath('./td[31]/text()').extract_first() == None):
				tov = row.xpath('./td[31]/span/strong/text()').extract_first()
			else:
				tov = row.xpath('./td[31]/text()').extract_first() #Good
			if(row.xpath('./td[32]/text()').extract_first() == None):
				pf = row.xpath('./td[32]/span/strong/text()').extract_first()
			else:
				pf = row.xpath('./td[32]/text()').extract_first() #Good
			if(row.xpath('./td[33]/text()').extract_first() == None):
				pts = row.xpath('./td[33]/span/strong/text()').extract_first()
			else:
				pts = row.xpath('./td[33]/text()').extract_first() #Good

			item = BBrefItem()
			item['season'] = season
			item['league'] = league
			item['team'] = team
			item['wins'] = wins
			item['losses'] = losses
			item['finish'] = finish

			if(age == None):
				item['age'] = ''
			else:
				item['age'] = age

			if(height == None):
				item['height'] = ''
			else:
				item['height'] = height

			if(weight == None):
				item['weight'] = ''
			else:
				item['weight'] = weight

			item['games'] = games

			if(mp == None):
				item['mp'] = ''
			else:
				item['mp'] = mp

			item['fg'] = fg
			item['fga'] = fga
			item['fga_pct'] = fga_pct

			if(fg3 == None):
				item['fg3'] = ''
			else:
				item['fg3'] = fg3

			if(fg3a == None):
				item['fg3a'] = ''
			else:
				item['fg3a'] = fg3a

			if(fg3_pct == None):
				item['fg3_pct'] = ''
			else:
				item['fg3_pct'] = fg3_pct

			item['fg2'] = fg2
			item['fg2a'] = fg2a
			item['fg2_pct'] = fg2_pct
			item['ft'] = ft
			item['fta'] = fta
			item['ft_pct'] = ft_pct
			if(orb == None):
				item['orb'] = ''
			else:
				item['orb'] = orb

			if(drb == None):
				item['drb'] = ''
			else:
				item['drb'] = drb

			if(trb == None):
				item['trb'] = ''
			else:
				item['trb'] = trb

			item['ast'] = ast

			if(stl == None):
				item['stl'] = ''
			else:
				item['stl'] = stl

			if(blk == None):
				item['blk'] = ''
			else:
				item['blk'] = blk

			if(tov == None):
				item['tov'] = ''
			else:
				item['tov'] = tov
			item['pf'] = pf
			item['pts'] = pts

			yield item