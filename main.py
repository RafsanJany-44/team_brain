import spacy

nlp = spacy.load("en_core_web_sm")


def check_sent(sent):
    k = 0
    if sent[0].pos_ == "ADV":
        k = 1
    if sent[k].tag_ == "VB":
        return "This is a command sentence"
    elif sent[k].tag_ == "VBP" and sent[k].lemma_ != "be":
        if len(sent) > k + 1:
            if sent[k + 1].dep_ != "nsubj":
                return "This is a command sentence"
            else:
                return "other sentence"
        else:
            return "This is a command sentence"
    else:
        return "other sentence"


s = nlp("First Do it")

print(check_sent(s))
