import lightgbm as lgb
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 加载数据
data = load_iris()
X, y = data.data, data.target

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 创建 LightGBM 数据集格式
train_data = lgb.Dataset(X_train, label=y_train)
test_data = lgb.Dataset(X_test, label=y_test, reference=train_data)

# 设置参数
params = {
    "objective": "multiclass",  # 多分类任务
    "num_class": 3,  # 类别数（鸢尾花有3类）
    "metric": "multi_logloss",  # 评估指标
    "boosting_type": "gbdt",  # 梯度提升决策树
    "num_leaves": 31,  # 单棵树的最大叶子数
    "learning_rate": 0.05,
    "feature_fraction": 0.9,  # 随机选择部分特征训练
}
from lightgbm.callback import log_evaluation, early_stopping

callbacks = [log_evaluation(period=100), early_stopping(stopping_rounds=50)]
# 训练模型
model = lgb.train(
    params,
    train_data,
    valid_sets=[test_data],
    num_boost_round=100,  # 迭代次数
    # early_stopping_rounds=10,  # 早停（防止过拟合）
    callbacks=callbacks,
)

# 预测
y_pred = model.predict(X_test, num_iteration=model.best_iteration)
y_pred = [list(x).index(max(x)) for x in y_pred]  # 将概率转化为类别

# 评估
print("准确率:", accuracy_score(y_test, y_pred))
