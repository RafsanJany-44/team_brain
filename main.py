import spacy

nlp = spacy.load("en")


def check_sent(sent):
    aux = ["am", "is", "are", "was", "were", "have", "has", "had", "have been", "has been", "had been"]
    k = 0
    if sent[0].pos_ == "ADV":
        k = 1
    if sent[k].tag_ == "VB":
        return "This is a command sentence"
    elif sent[k].tag_ == "VBP" and str(sent[k]).lower() not in aux:
        if len(sent) > k + 1:
            if sent[k + 1].dep_ != "n su bj":
                return "This is a command sentence"
            else:
                return "other sentence"
        else:
            return "This is a command sentence"
    else:
        return "other sentence"


s = nlp("dance like a clown")
print(check_sent(s))
