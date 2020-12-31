import functions as f


if __name__ == "__main__":
    while True:
        if f.listenForWakeWord():
            f.greet()
            listening = True
            while listening:
                data = f.listen().lower()
                questions = data.split(" and ")
                listening = f.assistant(questions)