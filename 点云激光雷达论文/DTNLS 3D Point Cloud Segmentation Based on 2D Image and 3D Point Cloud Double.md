
---

title: DTNLS: 3D Point Cloud Segmentation Based on 2D Image and 3D Point Cloud Double Texture Feature
author: Liu 等
year: 2025
topic: 点云分割 / 多模态融合 / LiDAR
status: 初读（未复现）在·

---

### 一句话总结

这篇文章提出了一种结合了二维图像信息的 LiDAR 三维**点云分割算法**，通过图像分割引导点云边界提取
### 研究问题

LiDAR 点云的范围信息准确（每个点距离测得准），但是缺少环境语义信息，边界分割不清，希望借助图像纹理辅助点云分割
（纹理就是数据在局部区域里呈现出来的模式、变化规律和结构特征，如图像的色彩变化，明暗分布，相邻像素的边界类型等，点云纹理特征一般包括点云分布的疏密分布规律等）
### 明确输入输出依赖

输入：RGB 图像 + 3D LiDAR 点云 + 标定参数
  ↓
处理：2D 图像纹理分割 → 2D-3D 映射 → 3D 点云扩散分割
  ↓
输出：带有类别标签的 3D 点云分割结果

### 核心方法流程

DTNLS 的流程：
1. 输入 2D 图像与 3D LiDAR 点云，通过**标定矩阵**建立 3D 点到 2D 投影关系
2. 图像纹理分割得到聚类中心与边界轮廓
3. 以聚类中心作为扩散源沿 LiDAR 环形扩散
4. 在边界附近搜索点云纹理边界
5. 输出三维点云分割结果 ![[Pasted image 20261009165331.png]]

创新点：
- 双纹理特征融合
- 图像引导点云分割
- 利用边界轮廓提升分割精度
### 实验怎么做、效果：

- **数据集**：KITTI (64线)、自采集 (16线)
- **指标**：Precision、Recall、IoU、分割速度
- **对比方法**：传统聚类方法 + 深度学习方法（PointNet系列、RangeNet++等）
- **结论**：
  - 行人分割：IoU +48.8%、Precision +32.2%、Recall +20.12%
  - 速度：KITTI 0.46s/帧、16线 0.36s/帧
  - **核心优势**：无需训练数据，跨硬件泛化
### 优点

- 利用图像纹理补足点云纹理不足
- 对边界区域更友好
- 思路直观，容易理解
- 可解释性相对较强
### 局限

- 依赖图像和点云的精确配准
- 对光照、遮挡、图像质量可能敏感
	（若一个物体有多个颜色，图像被分割为多个物体会导致点云也相应把一个物体分割为多个，分割失败）
	（距离相近的两个物体在 3D 点云边界处的纹理特征不明显，从而分割失败）
- 方法是否适用于不同类型 LiDAR 需要进一步验证

### 引用

#### 🎯 核心方法/创新点（引用率最高）

> "We present Double Texture Neighbor LiDAR Segmentation (DTNLS) in this letter. Double texture refers to the color texture of the image and the point cloud texture of the 3D LiDAR."

用途：介绍 DTNLS 方法定义时引用，一句话说清"双纹理"的含义。

> "3D LiDAR point cloud texture segmentation takes the clustering center obtained above as the diffusion source, diffuses outwards along the ring LiDAR line, finds the LiDAR point cloud texture boundary features near the image segmentation boundary contour, and finally realizes 3D point cloud segmentation."

用途：描述整个 pipeline 的核心机制（种子扩散 + 边界判断），方法综述里最好用。

#### 💡 无需训练数据（这是它最大卖点）

> "...without the need for any 2D images and 3D point cloud training data."

> "By eliminating the need for labeled 3D training data, DTNLS helps generalize to new environments, such as robot exploration of new objects and environments."

用途：讨论无监督/免标注方法的优势时引用，对比深度学习方法。