- # each data

- **行情数据 Market Data** 行情数据代表上市公司股票月度交易行情，主要包括价格、成交量、成交额、换手率等。

- sheets

- - DATA
  - CN_EN



| TYPE_NAME_CN | TYPE_NAME_EN                 |
| ------------ | ---------------------------- |
| 金融服务     | Financial Service            |
| 银行         | Bank                         |
| 房地产       | Real Estate                  |
| 医药生物     | Medicine and Biology         |
| 公用事业     | Utilities                    |
| 休闲服务     | Leisure Service              |
| 综合         | Composite                    |
| 机械设备     | Mechanical Equipment         |
| 有色金属     | Non-Ferrous Metals           |
| 商业贸易     | Commercial Trade             |
| 建筑装饰     | Building Decorations         |
| 建筑建材     | Building Materials           |
| 建筑材料     | Building Material            |
| 家用电器     | Household Appliances         |
| 交运设备     | Delivery Equipment           |
| 汽车         | Automobile                   |
| 纺织服装     | Textile and Garment          |
| 食品饮料     | Food and Beverage            |
| 电子         | Electronics                  |
| 信息设备     | Information Devices          |
| 计算机       | Computer                     |
| 交通运输     | Transportation               |
| 轻工制造     | Light Manufacturing          |
| 通信         | Communication                |
| 农林牧渔     | Animal Husbandry and Fishery |
| 化工         | Chemical Industry            |
| 传媒         | Media                        |
| 钢铁         | Steel                        |
| 采掘         | Mining                       |
| 非银金融     | Non-bank Finance             |
| 国防军工     | Defense and Military         |
| 信息服务     | Information Services         |
| 电气设备     | Electronic Equipment         |



# 三大表

- **财务数据**包括三张表，分别为资产负债表 Balance Sheet、利润表 Income Statement、现金流量表 Cash Flow Statement。其中，由于非金融上市公司、证券、银行、保险四大行业的财务报表在结构上存在差异，所以每个类别又分为4个相对应的文档（csv格式）。这三张表代表了一个公司全部的财务信息，三大财务报表分析是投资的基础。

- 资产负债表：代表一个公司的资产与负债及股东权益，资产负债表是所有表格的基础。

- 利润表：代表一个公司的利润来源，而净利润则直接影响资产负债表中股东权益的变化。

- 现金流量表：代表一个公司的现金流量，更代表资产负债表的变化。现金流量表是对资产负债表变化的解释。现金的变化最终反映到资产负债表的现金及等价物一项。而现金的变化源泉则是净利润。净利润经过“经营”、“投资”、“筹资”三项重要的现金变动转变为最终的现金变化。

# 找到互相之间连接的键值

market

- | SECURITY_ID   | 证券内部编码，为通联数据内部编码，唯一，Int类型 |
  | ------------- | ----------------------------------------------- |
  | TICKER_SYMBOL | 证券在交易所的交易代码，如000001，String类型    |

  | TYPE_ID   | 行业ID，为行业在通联数据内部编码，唯一，String类型 |
  | --------- | -------------------------------------------------- |
  | TYPE_NAME | 行业名称，如“金融服务”，String类型                 |



# 我们的流程

- 对数据所需要的背景知识有所了解，理解每个字段的含义
- 明确任务的目标
  - 仅仅是预测任务还是什么别的？
  - 我的意思是某些场景下可能需要模型有较高的可解释性
  - 这会影响我们选择模型的范围
  - 譬如有日期型数据，看看需不需要用时间序列处理方法
  - 
- 读取数据，做数据预处理
  - 查看数据类型，填补缺失值
  - 数据类型统一化
  - 特殊情况：有汇总形式数据，可能要做差分
  - 有类别类型数据，encode一下
  - 数值型数据归一化
- 确定目标变量和解释变量
- 开始迭代
  - 由idea出发，写出一些code，然后用一个单一指标评估模型好坏
  - 接下来尝试多个模型，在计算资源有限的情况下，选中一个模型
  - 接下来就使用各种方法减少偏差和方差
  - 最后再放到测试集上进行测试
  - 如果时间充裕，每隔几天就要更换一些参数，做微调
  - 最终部署到应用环境中，看效果
  - 再进行迭代







## 参考网站

https://github.com/Gustrigos/Eigen-Portfolio

https://www.joinquant.com/view/factorlib/list