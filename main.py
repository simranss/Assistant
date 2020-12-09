import functions as f


if __name__ == "__main__":
    f.greet()
    listening = True
    while listening:
        data = f.listen().lower()
        questions = data.split(" and ")
        listening = f.assistant(questions)