	# -*- coding: UTF-8 -*-

import api
import appModuleHandler
import controlTypes
import ui
from logHandler import log


class AppModule(appModuleHandler.AppModule):


	def event_NVDAObject_init(self,obj):

		if obj.name==u'NeteaseMusic.ViewModels.SideBarGroupViewModel' :
			obj.name=obj.children[0].children[0].name
		elif obj.name==u'NeteaseMusic.ViewModels.SideBarItemViewModel':
			obj.name=obj.children[0].name
		elif obj.name==u'NeteaseMusic.ViewModels.PersonalizeGroupViewModel' :
			if obj.children[0].role==controlTypes.ROLE_STATICTEXT:
				obj.name=obj.children[0].name
			else:
				obj.name=obj.children[0].children[0].name
		elif obj.name==u'NeteaseMusic.ViewModels.PlaylistSongViewModel':
			#歌单中的项目朗读的是项目的内部类名
			#序号、名称、歌手、专辑等描述在子元素中
			#所以我们使用子元素为歌曲列表项目命名

			obj.name=obj.children[0].name+obj.children[2].name+obj.children[3].name+','+obj.children[4].name
		elif obj.name==u'NeteaseMusic.ViewModels.PersonalizeItemViewModel':
			obj.name=obj.children[2].name
		elif obj.name==u'NeteaseMusic.ViewModels.PrivateContentItemViewModel':
			obj.name=obj.children[0].name
		elif obj.name==u'NeteaseMusic.ViewModels.PlaylistHotTagViewModel':
			obj.name=obj.children[0].name
		elif obj.name==u'NeteaseMusic.ViewModels.PlaylistItemViewModel':
			obj.name=obj.children[0].name
		elif obj.name==u'NeteaseMusic.ViewModels.ArtistFilterItemViewModel':
			obj.name=obj.children[0].name
		elif obj.name==u'NeteaseMusic.ViewModels.ArtistViewModel':
			obj.name=obj.children[0].name
		elif obj.name==u'NeteaseMusic.ViewModels.NewSongViewModel':
			obj.name=obj.children[0].name+obj.children[2].name

		elif obj.name==u'NeteaseMusic.ViewModels.Commons.SongViewModel':
			obj.name=obj.children[0].name+obj.children[2].name

	



