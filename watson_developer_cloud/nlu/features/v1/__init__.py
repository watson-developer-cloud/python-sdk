class Feature(object):
    def toDict(self):
        res = {}
        if not hasattr(self, "_dataTuples"):
            return res

        for t in self._dataTuples:
            self.addKey(t[0], t[1], res)
        return res

    def name(self):
        return self._name

    def addKey(self, var, name, data_dict):
        if var is not None:
            data_dict[name] = var
        return data_dict


class Concepts(Feature):
    def __init__(self, limit=None):
        self._dataTuples = [(limit, "limit")]
        self._name = 'concepts'


class Entities(Feature):
    def __init__(self, limit=None, model=None, emotion=None, sentiment=None):
        self._dataTuples = [(limit, "limit"), (model, "model"),
                            (emotion, "emotion"), (sentiment, "sentiment")]
        self._name = 'entities'


class Keywords(Feature):
    def __init__(self, limit=None, emotion=None, sentiment=None):
        self._dataTuples = [(limit, "limit"), (emotion, "emotion"),
                            (sentiment, "sentiment")]
        self._name = 'keywords'


class Categories(Feature):
    def __init__(self):
        self._name = 'categories'


class Emotion(Feature):
    def __init__(self, document=None, targets=None):
        self._dataTuples = [(document, "document"), (targets, "targets")]
        self._name = 'emotion'


class MetaData(Feature):
    def __init__(self):
        self._name = "metadata"


class SemanticRoles(Feature):
    def __init__(self, limit=None, entities=None, keywords=None):
        self._dataTuples = [(limit, "limit"), (entities, "entities"),
                            (keywords, "keywords")]
        self._name = "semantic_roles"


class Relations(Feature):
    def __init__(self, model=None):
        self._dataTuples = [(model, "model")]
        self._name = 'relations'


class Sentiment(Feature):
    def __init__(self, document=None, targets=None):
        self._dataTuples = [(document, "document"), (targets, "targets")]
        self._name = 'sentiment'
