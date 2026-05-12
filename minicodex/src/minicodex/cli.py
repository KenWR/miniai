def main():
    print("Minicodex v1")
    print("Type 'quit' to stop.")

    while True:
        user_input = input("\nYou> ").strip()
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

        if not user_input:
            print("Please enter a command.")
            continue

        print(f"MiniCodex> You said: {user_input}")


if __name__ == "__main__":    
    main()