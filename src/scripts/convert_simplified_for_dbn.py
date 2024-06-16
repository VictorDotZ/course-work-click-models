def convert_session(line):
    session_id, query, clicks, serp = line.strip().split("\t")
    serp = serp.split(",")
    serp_result = "\t".join(serp)

    yield f"{session_id}\t0\tQ\t{query}\t0\t{serp_result}"

    clicks = list(map(int, clicks.split(",")))
    for click in clicks:
        yield f"{session_id}\t0\tC\t{serp[click]}"
        
with open("./data/iphone-dbn", "w", encoding="utf-8") as f_out:
    with open("./data/iphone-20240201", "r", encoding="utf-8") as f_in:
        for source_line in f_in:
            for result_line in convert_session(source_line):
                f_out.write(result_line)
                f_out.write("\n")
