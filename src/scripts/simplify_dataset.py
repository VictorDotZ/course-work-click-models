URL_TO_DOC_ID = {}
QUERY_TO_Q_ID = {}

SERP_LEN = 10

def update_dict(d, key):
    if key not in d:
        d[key] = len(d)

    return d

def update_doc_ids(d, serp):
    for url in serp:
        d = update_dict(d, url)

    return d

with open("./data/iphone-20240201", "w", encoding="utf-8") as f_out:
    with open("./data/iphone-20240201.tsv", "r", encoding="utf-8") as f_in:
        for line in f_in:
            line = line.strip()
            session_id, _, query, clicks, serp = line.split("\t")
            
            QUERY_TO_Q_ID = update_dict(QUERY_TO_Q_ID, query)
            URL_TO_DOC_ID = update_doc_ids(URL_TO_DOC_ID, serp.split(","))
            
            qid = QUERY_TO_Q_ID[query]
            
            serp= list(map(lambda url: str(URL_TO_DOC_ID[url]), serp.split(",")))

            clicks = list(map(int, clicks.split(",")))
            clicks = list(filter(lambda pos: pos < SERP_LEN, clicks))
            
            if len(clicks) == 0:
                continue
            
            clicks = list(map(str, clicks))
            
            serp = serp[:SERP_LEN]
            
            if len(serp) != 10:
                continue
            
            res_line = f'{session_id}\t{qid}\t{",".join(clicks)}\t{",".join(serp)}\n'
            
            f_out.write(res_line)
