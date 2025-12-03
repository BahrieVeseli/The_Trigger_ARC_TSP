def log_progress(msg, logfile="run.log"):
    with open(logfile,"a") as f: f.write(msg+"\n")
    print(msg)
