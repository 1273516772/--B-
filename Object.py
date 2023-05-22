import re
import os

curr_path=os.path.dirname(os.path.abspath(__file__))    ##定义当前路径
hds = {
    "User-Agent": "Hello world"}  # 反扒
obj = re.compile(
    r'{"rpid".*?"root":(?P<is_top_comment>.*?),".*?mid":"(?P<uid>.*?)","uname":"(?P<name>.*?)".*?"content":{"message":"(?P<comment>.*?)"',
    re.S)
objtitle=re.compile(r'<title data-vue-meta="true">(?P<title>.*?)</title>',re.S)


EntryStyle='primary'


if __name__ == '__main__':
    result=obj.finditer('"dynamic_id_str":"0"},{"rpid":156497667232,"oid":653520954,"type":1,"mid":3230004,"root":156488282688,"parent":156488282688,"dialog":156497667232,"count":0,"rcount":0,"state":0,"fansgrade":0,"attr":0,"ctime":1678955183,"rpid_str":"156497667232","root_str":"156488282688","parent_str":"156488282688","like":1786,"action":0,"member":{"mid":"3230004","uname":"福尔康利","sex":"保密","sign":"","avatar":"http://i0.hdslb.com/bfs/face/490c14e41a3e1392475b20ec425c8215c0568bff.jpg","rank":"10000","face_nft_new":0,"is_senior_member":0,"senior":{},"level_info":{"current_level":6,"current_min":0,"current_exp":0,"next_exp":0},"pendant":{"pid":0,"name":"","image":"","expire":0,"image_enhance":"","image_enhance_frame":""},"nameplate":{"nid":0,"name":"","image":"","image_small":"","level":"","condition":""},"official_verify":{"type":-1,"desc":""},"vip":{"vipType":0,"vipDueDate":0,"dueRemark":"","accessStatus":0,"vipStatus":0,"vipStatusWarn":"","themeType":0,"label":{"path":"","text":"","label_theme":"","text_color":"","bg_style":0,"bg_color":"","border_color":"","use_img_label":true,"img_label_uri_hans":"","img_label_uri_hant":"","img_label_uri_hans_static":"https://i0.hdslb.com/bfs/vip/d7b702ef65a976b20ed854cbd04cb9e27341bb79.png","img_label_uri_hant_static":"https://i0.hdslb.com/bfs/activity-plat/static/20220614/e369244d0b14644f5e1a06431e22a4d5/KJunwh19T5.png"},"avatar_subscript":0,"nickname_color":""},"fans_detail":null,"user_sailing":null,"is_contractor":false,"contract_desc":"","nft_interaction":null,"avatar_item":{"container_size":{"width":1.8,"height":1.8},"fallback_layers":{"layers":[{"visible":true,"general_spec":{"pos_spec":{"coordinate_pos":2,"axis_x":0.9,"axis_y":0.9},"size_spec":{"width":1,"height":1},"render_spec":{"opacity":1}},"layer_config":{"tags":{"AVATAR_LAYER":{}},"is_critical":true,"layer_mask":{"general_spec":{"pos_spec":{"coordinate_pos":2,"axis_x":0.9,"axis_y":0.9},"size_spec":{"width":1,"height":1},"render_spec":{"opacity":1}},"mask_src":{"src_type":3,"draw":{"draw_type":1,"fill_mode":1,"color_config":{"day":{"argb":"#FF000000"}}}}}},"resource":{"res_type":3,"res_image":{"image_src":{"src_type":1,"placeholder":6,"remote":{"url":"http://i0.hdslb.com/bfs/face/490c14e41a3e1392475b20ec425c8215c0568bff.jpg","bfs_style":"widget-layer-avatar"}}}}}],"is_critical_group":true},"mid":"3230004"}},"content":{"message":"明白你的意思 我也打了一大篇 想了想还是删了 还真是一眼望到头 核心的玩意儿是一点没变过","members":[],"jump_url":{},"max_line":6},"replies":null,"assist":0,"up_action":{"like":false,"reply":false},"invisible":false,"reply_control":{"max_line":6,"time_desc":"32天前发布","location":"IP属地：湖北"},"folder":{"has_folded":false,"is_folded":false,"rule":""},')
    for i in result:
        print(type(result))
        print(i.group('name'),i.group('comment'))


