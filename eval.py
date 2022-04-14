class Evaluation:
    def __init__(self, tp, tn, fp, fn):
        self.tp = tp
        self.tn = tn
        self.fp = fp
        self.fn = fn

    def precision(self):
        return float(self.tp / (self.tp + self.fp))

    def recall(self):
        return float(self.tp / (self.tp + self.fn))

    def f_score(self):
        prec = self.recall()
        recall = self.precision()
        return float((2 * prec * recall) / (prec + recall))


eval = Evaluation(4, 6, 5, 1)
print(eval.precision())
print(eval.recall())
print(eval.f_score())