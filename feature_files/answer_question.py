import wolframalpha


class AnswerQuestion:
    def __init__(self, path_to_api_key):
        with open(path_to_api_key, "r") as file:
            app_id = file.read().strip("\n")
            self.client = wolframalpha.Client(app_id)

    def search(self, query):
        response = self.client.query(query)
        answer = []
        for pod in response.pods:
            for subpod in pod.subpods:
                answer.append(subpod.plaintext)
        return "\n".join(answer)


if __name__ == "__main__":
    aq = AnswerQuestion("c:/API keys/wolframalpha.txt")
    print(aq.search("What is the weather like in London"))
