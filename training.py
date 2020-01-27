#Решетчатый поиск значений гипрепараметров алгоритмов. Перекрестная
проверка. Масштабированные данные.

from sklearn.svm import SVC
for gamma in [0.001, 0.01, 0.1, 1, 10, 100]:
 for C in [0.001, 0.01, 0.1, 1, 10, 100]:
 #для каждой комбинации параметров обучаем SVC
 svm = SVC(gamma=gamma, C=C)
 #выполняем перекрестную проверку
 scores = cross_val_score(svm, X_train_scaled, y_train, cv=10)
 #вычисляем среднюю правильность перекрестной проверки
 score = np.mean(scores)
 #если получаем лучшее значение правильности, сохраняем значение и параметры
 if score > best_score:
  best_score = score
  best_parameters = {'C': C, 'gamma': gamma}
#заново строим модель на наборе, полученном в результате объединения обучающих и проверочных данных
svm = SVC(**best_parameters)
svm.fit(X_train_scaled, y_train)

#аналогично для k ближайших соседей
best_score = 0
for n_neighbors in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
 knn = KNeighborsClassifier(n_neighbors=n_neighbors)
 scores = cross_val_score(knn, X_train, y_train, cv=10)
 score = np.mean(scores)
 if score > best_score:
  best_score = score
  best_parameters = {'n_neighbors': n_neighbors}
knn = KNeighborsClassifier(**best_parameters)
knn.fit(X_train, y_train)

#для логистической регрессии
best_score = 0
for C in [0.001, 0.01, 0.1, 1, 10, 100]:
 LG = LogisticRegression(C=C)
 scores = cross_val_score(LG, X_train, y_train, cv=10)
 score = np.mean(scores)
 if score > best_score:
  best_score = score
  best_parameters = {'C': C}
LG = LogisticRegression(**best_parameters)
LG.fit(X_train, y_train)
