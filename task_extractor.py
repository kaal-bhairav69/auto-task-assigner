import re
import spacy
import string

nlp = spacy.load("en_core_web_sm")

def extract_tasks_clean(text):
    task_keywords = {
        "do", "handle", "complete", "prepare", "finish", "send", "check", "make", "submit", "build",
        "should", "sleep", "write", "create", "turn", "fill", "open", "close", "clean", "start",
        "stop", "get", "go", "play", "review", "update", "schedule", "organize", "analyze", "call",
        "email", "discuss", "share", "present", "assign", "coordinate", "manage", "design", "plan",
        "follow", "implement", "arrange", "report", "remind", "collect", "connect", "finalize", "note",
        "attend", "resolve", "approve", "track", "push", "sync", "prioritize", "reach", "monitor",
        "deploy", "test", "investigate", "confirm", "brainstorm", "lead", "compile", "explain",
        "optimize", "validate", "lock", "troubleshoot", "draft"
    }

    confirmation_keywords = {
        "yes", "okay", "ok", "sure", "got it", "alright", "i will", "i’ll", "i'll", "on it",
        "working on it", "noted", "fair", "good enough", "cool", "yep", "chill", "will do"
    }

    tasks = []
    already_assigned = set()
    doc = nlp(text)

    for sent in doc.sents:
        sentence = sent.text.strip()

        # Skip short/incomplete sentences
        if len(sentence.split()) < 3:
            continue

        # Normalize punctuation for confirmation check
        lower_sentence = sentence.lower()
        normalized = re.sub(rf"[{re.escape(string.punctuation)}]", "", lower_sentence)

        if any(kw in normalized for kw in confirmation_keywords):
            continue

        assignee = None
        deadline = None

        # Named entity recognition
        for ent in sent.ents:
            if ent.label_ == "PERSON" and not assignee:
                assignee = ent.text
            elif ent.label_ in {"DATE", "TIME"}:
                deadline = ent.text

        # Fallback for names like "Name: ..."
        if not assignee:
            match = re.match(r"^([A-Z][a-z]+)[,:]", sentence)
            if match:
                assignee = match.group(1).strip()

        if not assignee:
            continue

        has_task = any(
            token.lemma_.lower() in task_keywords and token.pos_ == "VERB"
            for token in nlp(sentence)
        )

        if has_task:
            task_obj = {
                "assignee": assignee,
                "task": sentence
            }
            if deadline:
                task_obj["deadline"] = deadline
            tasks.append(task_obj)
            already_assigned.add(assignee)

    return tasks











