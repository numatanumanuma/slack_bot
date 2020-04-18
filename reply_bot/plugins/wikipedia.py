import wikipedia

class Wikipedia:
    def __init__(self, word):
        wikipedia.set_lang("ja")
        self.error = False
        try:
            self.search_results = wikipedia.search(word)
        except wikipedia.exceptions.DisambiguationError as e:
            self.error = True
        # 曖昧さ回避ページに飛ばされたときに対応

    def get_summary(self, sentences):
        if self.is_exists():
            return wikipedia.summary(self.search_results[0], sentences=sentences)

    def get_url(self):
        if self.is_exists():
            return wikipedia.page(self.search_results[0]).url

    def is_exists(self):
        if len(self.search_results) > 0:
            return not self.error
        else:
            return False
