import xgboost as xgb
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 加载Iris数据集
iris = load_iris()
X = iris.data
y = iris.target

# 将数据集分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 将数据转换为DMatrix格式（XGBoost的数据格式）
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

# 设置XGBoost的参数
params = {
    "objective": "multi:softmax",  # 多分类问题
    "num_class": 3,  # 类别数
    "max_depth": 3,  # 树的最大深度
    "eta": 0.1,  # 学习率
    "subsample": 0.8,  # 每棵树随机采样的比例
    "colsample_bytree": 0.8,  # 每棵树随机采样的特征比例
    "seed": 42,  # 随机种子
}

# 训练模型
num_round = 100  # 迭代次数
bst = xgb.train(params, dtrain, num_round)

# 预测
y_pred = bst.predict(dtest)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
