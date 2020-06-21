# QComboBox

- 目录
  - [下拉数据关联](#1下拉数据关联)

## 1、下拉数据关联
[运行 CityLinkage.py](CityLinkage.py)

一个省市区关联的三级联动，数据源在data.json中

1. 主要用了`QComboBox`的`setModel`设置一个`QSortFilterProxyModel`过滤模型
2. 并根据唯一编码过滤，为了不影响内容显示，唯一编码的角色为`ToolTipRole`
3. 用`QColumnView`可以实现类似效果

![CityLinkage](ScreenShot/CityLinkage.gif)