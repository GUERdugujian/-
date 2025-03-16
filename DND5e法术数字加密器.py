import random
import sys

# 示例命令: python script.py arg1 arg2
if len(sys.argv) > 1:
    input_str = sys.argv[1]  # 第一个参数
    separator = sys.argv[2]  # 第二个参数
else:
    separator="、"
spell_libraries = [
    # 0环
    ["光亮术", "魔法伎俩", "修复术", "冷冻射线", "传讯术", "酸液飞溅", "剑刃防护", "颤栗之触", 
     "舞光术", "德鲁伊伎俩", "魔能爆", "四象法门", "火焰箭", "交友术", "神导术", "法师之手",
     "心灵之楔", "次级幻象", "毒气喷涌", "燃火术", "抵抗术", "圣火术", "橡棍术", "电爪",
     "术法爆发", "维生术", "点点星芒", "奇术", "荆棘之鞭", "鸣雷破", "亡者丧钟", "克敌先击",
     "恶言相加", "光耀祷词"],
    # 1环
    ["魔法飞弹", "护盾术", "燃烧之手", "治愈真言", "羽落术", "警报术", "化兽为友", "黯冰狱铠",
     "哈达之臂", "灾祸术", "祝福术", "魅惑类人", "繁彩球", "七彩喷射", "命令术", "强令对决",
     "通晓语言", "造水术", "枯水术", "疗伤术", "侦测善恶", "侦测魔法", "侦测毒性和疾病",
     "易容术", "不谐低语", "神恩", "至圣斩", "捕获打击", "纠缠术", "脚底抹油", "妖火",
     "虚假生命", "寻获魔宠", "云雾术", "神莓术", "油腻术", "光导箭", "荆棘之雨", "炼狱叱喝",
     "英雄气概", "脆弱诅咒", "猎人印记", "冰刃", "鉴定术", "迷幻手稿", "致伤术", "跳跃术",
     "大步奔行", "法师护甲", "防护善恶", "净化饮食", "致病射线", "庇护术", "炽焰斩", "虔诚护盾",
     "无声幻影", "睡眠术", "动物交谈", "塔莎狂笑术", "谭森浮碟术", "雷鸣斩", "雷鸣波", "隐形仆役",
     "巫术箭", "激愤斩"],
    # 2环
    ["变身术", "秘法锁", "目盲术", "耳聋术", "安定心神", "朦胧术", "匕首之云", "疯狂冠冕",
     "不灭明焰", "黑暗术", "黑暗视觉", "侦测思想", "警戒箭阵", "强化属性", "变巨术", "缩小术",
     "炽焰法球", "遗体防腐", "造风术", "定身类人", "隐形术", "敲击术", "浮空术", "物件定位术",
     "魔嘴术", "魔化武器", "马友夫强酸箭", "镜影术", "迷踪步", "月华之光", "涅斯图魔法灵光",
     "魅影之力", "衰弱射线", "魔绳术", "灼热射线", "识破隐形", "粉碎音波", "蛛行术", "暗示术",
     "蛛网术", "援助术", "动物信使", "复苏秘法", "卜筮术", "树肤术", "野兽感官", "龙息术",
     "注目术", "寻获坐骑", "寻找陷阱", "火焰刀", "灼热金属", "次等复原术", "动植物定位术",
     "心灵尖刺", "行动无踪", "治疗祷言", "防护毒素", "闪耀斩", "沉默术", "荆棘丛生", "灵体武器",
     "野兽召唤术", "守护之链", "诚实之域"],
    # 3环
    ["降咒", "闪现术", "鹰眼术", "法术反制", "昼明术", "解除魔法", "恐惧术", "假死术", "火球术",
     "飞行术", "气化形体", "守卫刻纹", "加速术", "催眠图纹", "李欧蒙小屋", "闪电束",
     "回避侦测", "移除诅咒", "短讯术", "缓慢术", "臭云术", "妖精召唤术", "亡灵召唤术", "巧言术",
     "吸血鬼之触", "水下呼吸", "水上行走", "活化死尸", "活力灵光", "希望信标", "致盲斩",
     "召雷术", "咒唤兽群", "箭如雨下", "造粮术", "十字军披风", "元素武器", "哈达之欲", "闪电箭矢",
     "防护法阵", "高等幻象", "群体治愈真言", "融身入石", "魅影驹", "植物滋长", "防护能量",
     "回生术", "雪雨暴", "死者交谈", "植物交谈", "灵体卫士", "风墙术"],
    # 4环
    ["秘法眼", "生命灵光", "净化灵光", "放逐术", "枯萎术", "魅惑怪物", "强迫术", "困惑术",
     "咒唤微元素群", "咒唤林地卫士", "操控水体", "防死结界", "任意门", "预言术", "支配野兽",
     "艾伐黑触手", "鬼斧神工", "火焰护盾", "月光涌泉", "行动自如", "巨虫术", "擒抱藤", "高等隐形术",
     "信仰守卫", "幻景", "冰风暴", "李欧蒙秘藏箱", "生物定位术", "魔邓肯忠犬", "魔邓肯私人密室",
     "欧提路克弹力法球", "魅影杀手", "变形术", "惊惧斩", "塑石术", "石肤术", "异怪召唤术",
     "构装召唤术", "元素召唤术", "浓酸球", "火墙术"],
    # 5环
    ["活化物件", "防活物护罩", "启蒙术", "放逐斩", "毕格比之手", "原力法阵", "死云术", "通神术",
     "问道自然", "寒冰锥", "咒唤元素", "万箭齐发", "异界探知", "疫病术", "造物术", "湮灭波",
     "驱逐善恶", "支配类人", "托梦术", "焰击术", "指使术", "高等复原术", "圣居", "定身怪物",
     "疫病虫群", "贾拉兹光辉风暴", "通晓传奇", "群体疗伤术", "假象术", "篡改记忆", "穿墙术",
     "异界誓缚", "死者复活", "拉瑞心灵联结", "转生术", "探知", "伪装术", "钢风斩", "天界召唤术",
     "龙类召唤术", "迅捷箭袋", "突触静止", "心灵遥控", "传送法阵", "树跃术", "力场墙", "石墙术",
     "悠兰德王者威仪"],
    # 6环
    ["秘法门", "剑刃护壁", "连锁闪电", "死亡法阵", "咒唤妖精", "触发术", "唤起亡灵", "解离术",
     "卓姆吉瞬间召唤", "摄心目光", "寻路术", "石化术", "禁制术", "法术无效结界", "铜墙铁壁",
     "重伤术", "医疗术", "英雄宴", "魔魂壶", "群体暗示术", "地动术", "欧提路克冰封法球",
     "奥图迷舞", "异界誓盟", "预置幻象", "邪魔召唤术", "阳炎射线", "塔莎泡泡坩埚", "木遁术",
     "真知术", "冰墙术", "棘墙术", "御风而行", "回返真言"],
    # 7环
    ["咒唤圣光", "延迟爆裂火球", "圣言术", "以太化", "死亡一指", "火焰风暴", "力场监牢",
     "海市蜃楼", "魔邓肯豪宅术", "魔邓肯之剑", "位面转移", "律令巩固", "虹光喷射", "投影术",
     "再生术", "复生术", "反转重力", "隔离术", "拟像术", "徽记术", "传送术"],
    # 8环
    ["动物形态", "反魔法场", "嫌恶术", "关怀术", "摧心术", "克隆术", "操控天气", "半位面",
     "支配怪物", "地震术", "花言巧语", "圣洁灵光", "焚云术", "迷宫术", "心灵屏障", "律令震慑",
     "阳炎爆", "心灵感应", "海啸术"],
    # 9环
    ["星界投影", "预见术", "异界之门", "禁锢术", "群体医疗术", "流星爆", "律令医疗", "律令死亡",
     "虹光法墙", "形体变化", "复仇风暴", "时间停止", "完全变形术", "完全复生术", "怪影杀手",
     "祈愿术"]
]

def convert_spells(input_str, separator):
    if not input_str.isdigit():
        return "错误：请输入有效的数字串！"
    
    result = []
    for digit in input_str:
        level = int(digit)
        if 0 <= level < len(spell_libraries):
            result.append(random.choice(spell_libraries[level]))
        else:
            result.append("未知法术")
    
    return f"输出：{result}".join(result.split(separator))
