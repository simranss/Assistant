import functions as f



if __name__ == "__main__":
    f.greet()
    listening = True
    while listening:
        data = f.listen().lower()
        listening = f.assistant(data)
