from sklearn.metrics import accuracy_score, classification_report

def evaluate_model(model, X_test, y_test):
    pred = model.predict(X_test)

    acc = accuracy_score(y_test, pred)
    print("Accuracy:", acc)

    print("\nClassification Report:\n")
    print(classification_report(y_test, pred))
