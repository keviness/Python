# RDKit | 基于Ward方法对化合物进行分层聚类

从许多化合物构建结构多样的化合物库：

* 聚类方法
* 基于距离的方法
* 基于分类的方法
* 使用优化方法的方法

通过使用Ward方法进行聚类从化合物库中选择“各种”化合物，Ward方法是分层聚类方法之一。

---

**导入库**

```python
from rdkit import rdBase, Chem, DataStructs
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import rdMolDraw2D, IPythonConsole
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
%matplotlib inline
print(rdBase.rdkitVersion)
```

**载入数据**

```text
suppl = Chem.SDMolSupplier('Screening_Collection.sdf')
mols_free = [x for x in suppl if x is not None]
len(mols_free)
```

随机地改变分子的顺序

```text
np.random.seed(1234)
np.random.shuffle(mols_free)
```

## 基于scikit-learn通过Ward方法进行聚类

**Morgan指纹生成和距离矩阵计算**

创建指纹作为聚类的输入数据，并使用它创建距离矩阵。通过设置returnDistance = True选项，BulkTanimotoSimilarity的输出将更改为由“ 1 – Tanimoto系数”计算的距离，然后使用它来创建距离矩阵。

由于scikit-learn的输入必须是一个numpy数组，因此转换将在最后执行。

```text
morgan_fp = [AllChem.GetMorganFingerprintAsBitVect(x,2,2048) for x in mols_free]
dis_matrix = [DataStructs.BulkTanimotoSimilarity(morgan_fp[i], morgan_fp[:5000],returnDistance=True) for i in range(5000)]
dis_array = np.array(dis_matrix)
```

**使用 Ward方法进行聚类**

使用Ward方法将其分为6个类。在scikit-learn中，当达到指定数量的集群时，模型构建将终止。

```text
ward = AgglomerativeClustering(n_clusters=6)
ward.fit(dis_array)
pd.value_counts(ward.labels_)
```

1 1713

0 1622

3 719

2 420

5 372

4 154

dtype: int64

**通过Ward方法分类的每个簇中提取分子**

通过从每个簇中随机抽取分子来比较结构。将簇名称和分子与字典类型匹配之后随机选择一个分子。

```python
ward_library = {i: [] for i in range(6)}
for n,j in enumerate(ward.labels_):
    ward_library[j].append(mols_free[n])
selected_compounds = [np.random.choice(ward_library[i]) for i in range(6)]
Draw.MolsToGridImage(selected_compounds, molsPerRow=3,subImgSize=(300, 300), legends=["Group"+ ': ' + str(i) for i in range(6)])
```

![](https://pic1.zhimg.com/80/v2-8223a86ef8e19a37b59d2337b74eb444_1440w.jpg)

**通过树状图可视化聚类结果**

之所以将诸如Ward方法之类的聚集聚类称为**分层**聚类，是因为可以通过绘制逐个收集数据并形成一个组的过程来绘制类似于树状图的图。这样的图称为“ **树状图** ”。

```text
from scipy.cluster import hierarchy
linked_array = hierarchy.ward(dis_array)
hierarchy.dendrogram(linked_array)
ax = plt.gca()
bounds = ax.get_xbound()
ax.plot(bounds, [34.5,34.5], '--', c='gray')
ax.plot(bounds, [55,55], '--', c='gray')
ax.text(bounds[1], 55, ' 3 clusters', va='center')
ax.text(bounds[1], 34.5, ' 6 clusters')
plt.xlabel('Compounds', fontsize=12)
plt.xticks([])
plt.ylabel('Cluster distance', fontsize=12)
plt.title('Dendrogram for Ward method', fontsize=14)
```

![](https://pic3.zhimg.com/80/v2-5a3551e1649fc2b40cface03ac635b2a_1440w.jpg)

树状图中，x轴表示每个数据，y轴表示聚类之间的距离，与x轴上的水平线相交的聚类数是聚类数。

**PCA:主成分分析**

可视化聚类结果的另一种方法是数据降维。此数据是5000维数据，其中一个化合物由5000个特征表示，因此无法原样可视化。因此，有必要在保留数据集特征的同时将维数减小为我们可以理解的形式。最常用于此目的的方法称为“ 主成分分析（PCA） ”。

主成分分析在scikit-learn的sklearn.decomposition中实现。将转换为2D数据，并尝试通过使用簇号作为散点图上的标记颜色来可视化分类。

```text
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
#
pca.fit(dis_array)
dis_pca = pca.transform(dis_array)
#可视化
fig = plt.figure(figsize=(12,12))
ax = fig.add_subplot(111)
ax.scatter(dis_pca[:,0], dis_pca[:,1], s=50, c=ward.labels_[:5000], cmap='Paired', alpha=0.5)
ax.set_xlabel('PCA 1', fontsize=20)
ax.set_xticklabels([])
ax.set_ylabel('PCA 2', fontsize=20)
ax.set_yticklabels([])
ax.set_title('6-Clusters by sklearn ward', fontsize=28)
```

![](https://pic1.zhimg.com/80/v2-31b7deb9a1f5c4d509785b3ad0f12e9c_1440w.jpg)

**主成分分析中的累积贡献**

通过将数据从多维数据转换为具有大量信息的轴来实现主成分分析。在尺寸减小的过程中，从具有大量信息的轴中进行选择。在此过程中，最初沿轴的信息量最少的信息会丢失。围绕转换轴的信息量称为“ 贡献率 ”。

将5000维数据缩减为2维时丢失的信息量对于确定聚类是否成功很重要。

scikit学习PCA对象将贡献比率存储在explained_variance_ratio_中。在下面的代码中，“ 累积贡献 ”是针对前20个组件进行计算和绘制的。

```text
pca_all = PCA()
pca_all.fit(dis_array)
ev_ratio = np.hstack([0, np.cumsum(pca_all.explained_variance_ratio_)])
plt.plot(ev_ratio[:20])
plt.xlim([0,20])
plt.xticks(range(0,20,2))
plt.ylim([0,1.0])
plt.xlabel('n_components')
plt.ylabel('cumulative explained variance')
```

![](https://pic4.zhimg.com/80/v2-e1e0e128f44f53d3b450f993e7c72bd3_1440w.jpg)

随着主要成分数量的增加，累积贡献率逐渐增加。这种情况下，用于可视化的前两个组件只能解释大约37％的信息量。换句话说，如果主要使用剩余的60％信息进行聚类，则无法在2D平面上将其分离。进行主成分分析时，请确保在做出任何决定之前检查累积贡献。
