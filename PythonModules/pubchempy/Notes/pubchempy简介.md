# PubChem的Python接口PubChemPy

【摘要】 PubChem PubChem，即有机小分子生物活性数据，是一种化学模组的数据库，由美国国家健康研究院（ US National Institutes of Health，NIH）支持，美国国家生物技术信息中心负责维护。 PubChem数据库包括 3个子数据库： PubChem BioAssay 库用于存储生化实验数据，实验数据主要来自高通量筛选实验和科技文献； PubC...

## PubChem

PubChem，即有机小分子生物活性数据，是一种化学模组的数据库，由美国国家健康研究院（ US National Institutes of Health，NIH）支持，美国国家生物技术信息中心负责维护。

PubChem数据库包括 3个子数据库： PubChem BioAssay 库用于存储生化实验数据，实验数据主要来自高通量筛选实验和科技文献； PubChem Compound 库用于存储整理后的化合物化学结构信息； PubChem Substance 用于存储机构和个人上传的化合物原始数据。

## PubChemPy简介

    PubChemPy提供了一种Python与PubChem进行交互的方法。 允许按名称、子结构和相似性进行化学搜索、化学标准化、化学文件格式之间的转换、化学性质的描述和检索。

## PubChemPy功能

* 通过名称，SMILES，InChI和SDF搜索PubChem物质和化合物数据库。
* 检索给定输入结构的标准化化合物记录。
* 在SDF，SMILES，InChI，PubChem CID等之间转换。
* 检索计算的属性，指纹和描述符。
* 生成2D和3D坐标。
* 获取给定化合物的IUPAC系统名称，商品名称和所有已知的同义词。
* 将复合记录下载为XML，ASNT / B，JSON，SDF并以PNG图像形式进行描述。
* 使用pandas DataFrames构造属性表。

文章来源: drugai.blog.csdn.net，作者：DrugAI，版权归原作者所有，如需转载，请联系作者。

原文链接：drugai.blog.csdn.net/article/details/102725120
