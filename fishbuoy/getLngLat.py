#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 15:58
# @File    : getLngLat.py
# @Software: Pycharm
# @Author  : Changan
import os
import pymysql

sql =  sql = "select * from city_aqi"
conn = pymysql.connect('127.0.0.1', 'root', '132441', 'aqi', charset = 'utf8')
cur = conn.cursor()
cur.execute(sql)
results = cur.fetchall()  # 搜取所有结果
cur.close()
conn.close()
list = []
for res in results:
    data = {}
    data['city'] = res[2]+'市'
    data['aqi'] = res[4]
    list.append(data)
print(list)
lngLat =  [{"北京市": [116.395645,39.929986],
                "天津市": [117.210813,39.14393],
                "上海市": [121.487899,31.249162],
                "重庆市": [106.530635,29.544606],
                "香港特别行政区": [114.186124,22.293586],
                "澳门特别行政区": [113.557519,22.204118],
                "台湾省": [120.961454,23.80406],
                # //新疆维吾尔自治区
                "克拉玛依市": [84.88118,45.594331],
                "乌鲁木齐市": [87.564988,43.84038],
                "巴音郭楞蒙古自治州": [86.121688,41.771362],
                "伊犁哈萨克自治州": [81.297854,43.922248],
                "吐鲁番地区": [89.181595,42.96047],
                "阿勒泰地区": [88.137915,47.839744],
                "哈密地区": [93.528355,42.858596],
                "博尔塔拉蒙古自治州": [82.052436,44.913651],
                "阿克苏地区": [80.269846,41.171731],
                "克孜勒苏柯尔克孜自治州": [76.137564,39.750346],
                "昌吉回族自治州": [87.296038,44.007058],
                "喀什地区": [75.992973,39.470627],
                "和田地区": [79.930239,37.116774 ],
                "塔城地区": [82.974881,46.758684],
                "省直辖行政单位": [85.564988,40.84038],
                # //广西壮族自治区
                "崇左市": [107.357322, 22.415455],
                "柳州市": [109.422402, 24.329053],
                "百色市": [106.631821, 23.901512],
                "南宁市": [108.297234,22.806493 ],
                "梧州市": [111.305472, 23.485395],
                "北海市": [109.122628, 21.472718],
                "桂林市": [110.26092, 25.262901],
                "河池市": [108.069948, 24.699521],
                "贵港市": [109.613708, 23.103373],
                "钦州市": [108.638798, 21.97335],
                "来宾市": [109.231817, 23.741166],
                "防城港市": [108.351791, 21.617398],
                "贺州市": [111.552594, 24.411054],
                "玉林市": [110.151676, 22.643974],
                # // 西藏自治区
                "山南地区": [91.750644, 29.229027],
                "那曲地区": [92.067018, 31.48068],
                "阿里地区": [81.107669, 30.404557],
                "拉萨市": [91.111891, 29.662557],
                "昌都地区": [97.185582, 31.140576],
                "林芝地区": [94.349985, 29.666941],
                "日喀则地区": [88.891486, 29.269023],
                # //宁夏回族自治区
                "银川市": [106.206479, 38.502621],
                "吴忠市": [106.208254, 37.993561],
                "中卫市": [105.196754, 37.521124],
                "石嘴山市": [106.379337, 39.020223],
                "固原市": [106.285268, 36.021523],
                # // 内蒙古自治区
                "乌海市": [106.831999,39.683177],
                "鄂尔多斯市": [109.993706,39.81649],
                "兴安盟": [122.048167,46.083757],
                "锡林郭勒盟": [116.02734,43.939705],
                "巴彦淖尔市": [107.423807,40.76918],
                "赤峰市": [118.930761,42.297112],
                "乌兰察布市": [113.112846,41.022363],
                "呼伦贝尔市": [119.760822,49.201636],
                "通辽市": [122.260363,43.633756],
                "阿拉善盟": [105.695683,38.843075],
                "包头市": [109.846239,40.647119],
                "呼和浩特市": [111.660351, 40.828319],
                # //四川省
                "遂宁市": [105.564888,30.557491],
                "雅安市": [103.009356,29.999716],
                "巴中市": [106.757916,31.869189],
                "攀枝花市": [101.722423,26.587571],
                "自贡市": [104.776071,29.359157],
                "凉山彝族自治州": [102.259591,27.892393],
                "广元市": [105.819687,32.44104],
                "广安市": [106.63572,30.463984],
                "宜宾市": [104.633019,28.769675],
                "达州市": [107.494973,31.214199],
                "南充市": [106.105554,30.800965],
                "成都市": [104.067923,30.679943],
                "内江市": [105.073056,29.599462],
                "资阳市": [104.633019,28.769675],
                "阿坝藏族羌族自治州": [102.228565,31.905763],
                "甘孜藏族自治州": [101.969232,30.055144],
                "绵阳市": [104.705519,31.504701],
                "乐山市": [103.760824,29.600958],
                "泸州市": [105.44397,28.89593],
                "德阳市": [104.402398,31.13114],
                "眉山市": [103.84143,30.061115],
                # //陕西省
                "安康市": [109.038045,32.70437],
                "咸阳市": [108.707509,34.345373],
                "渭南市": [109.483933,34.502358],
                "汉中市": [107.045478,33.081569],
                "延安市": [109.50051,36.60332],
                "榆林市": [109.745926,38.279439],
                "西安市": [108.953098,34.2778],
                "铜川市": [108.968067,34.908368],
                "宝鸡市": [107.170645,34.364081],
                "商洛市": [109.934208,33.873907],
                # // 河南省
                "焦作市": [113.211836,35.234608],
                "南阳市": [112.542842,33.01142],
                "三门峡市": [111.181262,34.78332],
                "平顶山市": [113.300849,33.745301],
                "驻马店市": [114.049154,32.983158],
                "新乡市": [113.91269,35.307258],
                "许昌市": [113.835312,34.02674],
                "洛阳市": [112.447525,34.657368],
                "开封市": [114.351642,34.801854],
                "安阳市": [114.351807,36.110267],
                "周口市": [114.654102,33.623741],
                "信阳市": [114.085491,32.128582],
                "郑州市": [113.649644,34.75661],
                "濮阳市": [115.026627,35.753298],
                "商丘市": [115.641886,34.438589],
                "漯河市": [114.046061,33.576279],
                "鹤壁市": [114.29777,35.755426],
                # //浙江省
                "丽水市": [119.929576,28.4563],
                "衢州市": [118.875842,28.95691],
                "台州市": [121.440613,28.668283],
                "宁波市": [121.579006,29.885259],
                "杭州市": [120.219375,30.259244],
                "金华市": [119.652576,29.102899],
                "温州市": [120.690635,28.002838],
                "绍兴市": [120.592467,30.002365],
                "嘉兴市": [120.760428,30.773992],
                "湖州市": [120.137243,30.877925],
                "舟山市": [122.169872,30.03601],
                # // 海南省
                "海口市": [110.330802,20.022071],
                "三亚市": [109.522771,18.257776],
                "省直辖县级行政单位": [109.9267865,19.1399235],
                # // 山西省
                "运城市": [111.006854,35.038859],
                "忻州市": [112.727939,38.461031],
                "晋城市": [112.867333,35.499834],
                "临汾市": [111.538788,36.099745],
                "阳泉市": [113.569238,37.869529],
                "长治市": [113.120292,36.201664],
                "吕梁市": [111.143157,37.527316],
                "太原市": [112.550864,37.890277],
                "大同市": [113.290509,40.113744],
                "朔州市": [112.479928,39.337672],
                "晋中市": [112.738514,37.693362],
                # // 广东省
                "韶关市": [113.594461,24.80296],
                "惠州市": [114.410658,23.11354],
                "揭阳市": [116.379501,23.547999],
                "云浮市": [112.050946,22.937976],
                "深圳市": [114.025974,22.546054],
                "潮州市": [116.630076,23.661812],
                "清远市": [113.040773,23.698469],
                "梅州市": [116.126403,24.304571],
                "广州市": [113.30765,23.120049],
                "东莞市": [113.763434,23.043024],
                "江门市": [113.078125,22.575117],
                "肇庆市": [112.479653,23.078663],
                "茂名市": [110.931245,21.668226],
                "阳江市": [111.97701,21.871517],
                "汕尾市": [115.372924,22.778731],
                "河源市": [114.713721,23.757251],
                "中山市": [113.42206,22.545178],
                "佛山市": [113.134026,23.035095],
                "汕头市": [116.72865,23.383908],
                "湛江市": [110.365067,21.257463],
                "珠海市": [113.562447,22.256915],
                # // 云南省
                "怒江傈僳族自治州": [98.859932,25.860677],
                "迪庆藏族自治州": [99.713682,27.831029],
                "昭通市": [103.725021,27.340633],
                "西双版纳傣族自治州": [100.803038,22.009433],
                "玉溪市": [102.545068,24.370447],
                "临沧市": [100.092613,23.887806],
                "大理白族自治州": [100.223675,25.5969],
                "丽江市": [100.229628,26.875351],
                "楚雄彝族自治州": [101.529382,25.066356],
                "红河哈尼族彝族自治州": [103.384065,23.367718],
                "文山壮族苗族自治州": [104.089112,23.401781],
                "昆明市": [102.714601,25.049153],
                "曲靖市": [103.782539,25.520758],
                "保山市": [99.177996,25.120489],
                "思茅市": [100.980058,22.788778],
                "德宏傣族景颇族自治州": [98.589434,24.44124],
                # // 贵州省
                "贵阳市": [106.709177,26.629907],
                "黔西南布依族苗族自治州": [104.900558,25.095148],
                "铜仁地区": [109.196161,27.726271],
                "黔东南苗族侗族自治州": [107.985353,26.583992],
                "遵义市": [106.93126,27.699961],
                "毕节地区": [105.300492,27.302612],
                "黔南布依族苗族自治州": [107.523205,26.264536],
                "六盘水市": [104.852087,26.591866],
                "安顺市": [105.92827,26.228595],
                # // 辽宁省
                "鞍山市": [123.007763,41.118744],
                "本溪市": [123.778062,41.325838],
                "营口市": [122.233391,40.668651],
                "大连市": [121.593478,38.94871],
                "铁岭市": [123.85485,42.299757],
                "朝阳市": [120.446163,41.571828],
                "抚顺市": [123.92982,41.877304],
                "盘锦市": [122.073228,41.141248],
                "丹东市": [124.338543,40.129023],
                "葫芦岛市": [120.860758,40.74303],
                "锦州市": [121.147749,41.130879],
                "沈阳市": [123.432791,41.808645],
                "辽阳市": [123.172451,41.273339],
                "阜新市": [121.660822,42.01925],
                # // 河北省
                "廊坊市": [116.703602,39.518611],
                "衡水市": [115.686229,37.746929],
                "秦皇岛市": [119.604368,39.945462],
                "承德市": [117.933822,40.992521],
                "沧州市": [116.863806,38.297615],
                "张家口市": [114.893782,40.811188],
                "石家庄市": [114.522082,38.048958],
                "保定市": [115.49481,38.886565],
                "唐山市": [118.183451,39.650531],
                "邢台市": [114.520487,37.069531],
                "邯郸市": [114.482694,36.609308],
                # // 青海省
                "海南藏族自治州": [100.624066,36.284364],
                "海西蒙古族藏族自治州": [97.342625,37.373799],
                "海东地区": [102.085207,36.51761],
                "果洛藏族自治州": [100.223723,34.480485],
                "西宁市": [101.767921,36.640739],
                "海北藏族自治州": [100.879802,36.960654],
                "黄南藏族自治州": [102.0076,35.522852],
                "玉树藏族自治州": [97.013316,33.00624],
                # // 湖南省
                "邵阳市": [111.461525,27.236811],
                "张家界市": [110.48162,29.124889],
                "益阳市": [112.366547,28.588088],
                "怀化市": [109.986959,27.557483],
                "湘西土家族苗族自治州": [109.745746,28.317951],
                "郴州市": [113.037704,25.782264],
                "衡阳市": [112.583819,26.898164],
                "永州市": [111.614648,26.435972],
                "株洲市": [113.131695,27.827433],
                "岳阳市": [113.146196,29.378007],
                "长沙市": [112.979353,28.213478],
                "湘潭市": [112.935556,27.835095],
                "常德市": [111.653718,29.012149],
                "娄底市": [111.996396,27.741073],
                # // 江苏省
                "镇江市": [119.455835,32.204409],
                "常州市": [119.981861,31.771397],
                "南通市": [120.873801,32.014665],
                "泰州市": [119.919606,32.476053],
                "南京市": [118.778074,32.057236],
                "苏州市": [120.619907,31.317987],
                "盐城市": [120.148872,33.379862],
                "宿迁市": [118.296893,33.95205],
                "无锡市": [120.305456,31.570037],
                "连云港市": [119.173872,34.601549],
                "徐州市": [117.188107,34.271553],
                "淮安市": [119.030186,33.606513],
                "扬州市": [119.427778,32.408505],
                # // 山东省
                "潍坊市": [119.142634,36.716115],
                "日照市": [119.50718,35.420225],
                "济宁市": [116.600798,35.402122],
                "聊城市": [115.986869,36.455829],
                "德州市": [116.328161,37.460826],
                "临沂市": [118.340768,35.072409],
                "枣庄市": [117.279305,34.807883],
                "莱芜市": [117.684667,36.233654],
                "烟台市": [121.309555,37.536562],
                "淄博市": [118.059134,36.804685],
                "滨州市": [117.968292,37.405314],
                "泰安市": [117.089415,36.188078],
                "荷泽市": [115.46336,35.26244],
                "济南市": [117.024967,36.682785],
                "威海市": [122.093958,37.528787],
                "青岛市": [120.384428,36.105215],
                "东营市": [118.583926,37.487121],
                # // 安徽省
                "宣城市": [118.752096,30.951642],
                "阜阳市": [115.820932,32.901211],
                "亳州市": [115.787928,33.871211],
                "蚌埠市": [117.35708,32.929499],
                "黄山市": [118.29357,29.734435],
                "六安市": [116.505253,31.755558],
                "池州市": [117.494477,30.660019],
                "滁州市": [118.32457,32.317351],
                "淮南市": [117.018639,32.642812],
                "铜陵市": [117.819429,30.94093],
                "合肥市": [117.282699,31.866942],
                "芜湖市": [118.384108,31.36602],
                "马鞍山市": [118.515882,31.688528],
                "安庆市": [117.058739,30.537898],
                "淮北市": [116.791447,33.960023],
                "宿州市": [116.988692,33.636772],
                "巢湖市": [117.88049,31.608733],
                # //黑龙江省
                "双鸭山市": [131.171402,46.655102],
                "绥化市": [126.989095,46.646064],
                "大兴安岭地区": [124.196104,51.991789],
                "佳木斯市": [130.284735,46.81378],
                "黑河市": [127.50083,50.25069],
                "哈尔滨市": [126.657717,45.773225],
                "大庆市": [125.02184,46.596709],
                "七台河市": [131.019048,45.775005],
                "伊春市": [128.910766,47.734685],
                "牡丹江市": [129.608035,44.588521],
                "鸡西市": [130.941767,45.321541],
                "齐齐哈尔市": [123.987289,47.3477],
                "鹤岗市": [130.292472,47.338666],
                # // 福建省
                "三明市": [117.642194,26.270835],
                "厦门市": [118.103886,24.489231],
                "龙岩市": [117.017997,25.078685],
                "莆田市": [119.077731,25.44845],
                "南平市": [118.181883,26.643626],
                "宁德市": [119.542082,26.656527],
                "泉州市": [118.600362,24.901652],
                "漳州市": [117.676205,24.517065],
                "福州市": [119.330221,26.047125],
                # // 甘肃省
                "定西市": [104.626638,35.586056],
                "嘉峪关市": [98.281635,39.802397],
                "庆阳市": [107.644227,35.726801],
                "酒泉市": [98.508415,39.741474],
                "临夏回族自治州": [103.215249,35.598514],
                "金昌市": [102.208126,38.516072],
                "张掖市": [100.459892,38.93932],
                "白银市": [104.171241,36.546682],
                "陇南市": [104.934573,33.39448],
                "天水市": [105.736932,34.584319],
                "兰州市": [103.823305,36.064226],
                "武威市": [102.640147,37.933172],
                "平凉市": [106.688911,35.55011],
                "甘南藏族自治州": [102.917442,34.992211],
                # // 湖北省
                "鄂州市": [114.895594,30.384439],
                "武汉市": [114.3162,30.581084],
                "荆门市": [112.21733,31.042611],
                "恩施土家族苗族自治州": [109.517433,30.308978],
                "随州市": [113.379358,31.717858],
                "湖北省直辖行政单位": [110.487231,31.595768],
                "孝感市": [113.935734,30.927955],
                "襄樊市": [112.176326,32.094934],
                "黄冈市": [114.906618,30.446109],
                "荆州市": [112.241866,30.332591],
                "十堰市": [110.801229,32.636994],
                "宜昌市": [111.310981,30.732758],
                "黄石市": [115.050683,30.216127],
                "咸宁市": [114.300061,29.880657],
                # // 吉林省
                "长春市": [125.313642,43.898338],
                "通化市": [125.94265,41.736397],
                "吉林市": [126.564544,43.871988],
                "白山市": [126.435798,41.945859],
                "松原市": [124.832995,45.136049],
                "延边朝鲜族自治州": [129.485902,42.896414],
                "辽源市": [125.133686,42.923303],
                "白城市": [122.840777,45.621086],
                "四平市": [124.391382,43.175525],
                # // 江西省
                "抚州市": [116.360919,27.954545],
                "九江市": [115.999848,29.71964],
                "宜春市": [114.400039,27.81113],
                "上饶市": [117.955464,28.457623],
                "赣州市": [114.935909,25.845296],
                "南昌市": [115.893528,28.689578],
                "吉安市": [114.992039,27.113848],
                "景德镇市": [117.186523,29.303563],
                "萍乡市": [113.859917,27.639544],
                "新余市": [114.947117,27.822322],
                "鹰潭市": [117.03545,28.24131]
                }]