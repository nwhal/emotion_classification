class Evaluation:

    def confusion_matrix(self, predictions_on_test, real_test_label, emotion):
        tp = fp = fn = tn = 0

        for true, pred in zip(real_test_label, predictions_on_test):
            if true == emotion and pred > 0:
                tp = tp + 1
            if true != emotion and pred > 0:
                fp = fp + 1
            if true == emotion and not(pred > 0):
                fn = fn + 1
            if true != emotion and not(pred > 0):
                tn = tn + 1
        return tp, fp, fn, tn

    def precision(self, tp, fp, fn, tn):
        tp, fp, fn, tn = tp, fp, fn, tn
        return tp / (tp + fp) if (tp + fp) != 0 else 0

    def recall(self, tp, fp, fn, tn):
        tp, fp, fn, tn = tp, fp, fn, tn
        return tp / (tp + fn) if (tp + fp) != 0 else 0

    def f1score(self, recall, precision):
        r = recall
        p = precision
        return (2 * (p * r)) / (p + r) if p != 0 and r != 0 else 0
