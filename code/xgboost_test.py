import xgboost as xgb
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 加载数据
data = load_iris()
X, y = data.data, data.target

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 转换为 XGBoost 的 DMatrix 格式（优化数据存储）
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

# 设置参数
params = {
    "objective": "multi:softmax",  # 多分类任务
    "num_class": 3,  # 类别数（鸢尾花有3类）
    "eval_metric": "mlogloss",  # 评估指标
    "booster": "gbtree",  # 使用树模型
    "max_depth": 3,  # 树的最大深度
    "eta": 0.3,  # 学习率（类似 learning_rate）
    "subsample": 0.8,  # 随机采样数据（防止过拟合）
}

# 训练模型
model = xgb.train(
    params,
    dtrain,
    num_boost_round=100,  # 迭代次数
    evals=[(dtrain, "train"), (dtest, "test")],
    early_stopping_rounds=10,  # 早停（防止过拟合）
)

# 预测
y_pred = model.predict(dtest)

# 评估
print("准确率:", accuracy_score(y_test, y_pred))
